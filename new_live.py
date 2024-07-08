import os
from datetime import datetime
from PIL import Image, ImageDraw
import ctypes

# Function to calculate the number of days since the birthdate
def days_since_birth(birthdate):
    birth_date = datetime.strptime(birthdate, '%Y-%m-%d')
    current_date = datetime.now()
    delta = current_date - birth_date
    return delta.days

# Function to create the life days image
def create_life_image(birthdate, output_path):
    days_passed = days_since_birth(birthdate)

    # Get screen resolution
    user32 = ctypes.windll.user32
    screen_width = 1920
    screen_height = 1080

    # Calculate the cell size to fit the desired image size
    cell_size = min(screen_width // 365, screen_height // 100)

    img_width = screen_width
    img_height = screen_height

    img = Image.new('RGB', (img_width, img_height), color='white')
    draw = ImageDraw.Draw(img)

    # Add padding around the image
    padding = 50
    inner_width = img_width - 2 * padding
    inner_height = img_height - 2 * padding

    for year in range(100):
        for day in range(365):
            x0 = padding + day * cell_size
            y0 = padding + year * cell_size
            x1 = x0 + cell_size
            y1 = y0 + cell_size
            color = "green" if (year * 365 + day) < days_passed else "red"
            draw.rectangle([x0, y0, x1, y1], fill=color, outline="black")

    img.save(output_path)

# Function to set the image as wallpaper
def set_wallpaper(image_path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)

# Main function to generate the image and set it as wallpaper
def main():
    # Set the default birthdate to 2006-01-11
    birthdate = "2006-01-11"
    output_path = os.path.join(os.getcwd(), 'life_in_days_wallpaper.bmp')

    create_life_image(birthdate, output_path)
    set_wallpaper(output_path)

if __name__ == "__main__":
    main()
