import os
from datetime import datetime
from PIL import Image, ImageDraw
import ctypes

# Function to calculate the number of weeks since the birthdate
def weeks_since_birth(birthdate):
    birth_date = datetime.strptime(birthdate, '%Y-%m-%d')
    current_date = datetime.now()
    delta = current_date - birth_date
    return delta.days // 7

# Function to create the life weeks image
def create_life_image(birthdate, output_path):
    weeks_passed = weeks_since_birth(birthdate)
    
    # Get screen resolution
    user32 = ctypes.windll.user32
    screen_width = user32.GetSystemMetrics(0)
    screen_height = user32.GetSystemMetrics(1)
    
    # Calculate cell size based on screen resolution
    cell_size = min(screen_width // 52, screen_height // 100)
    
    img_width = cell_size * 52
    img_height = cell_size * 100

    img = Image.new('RGB', (img_width, img_height), color='white')
    draw = ImageDraw.Draw(img)

    for year in range(100):
        for week in range(52):
            x0 = week * cell_size
            y0 = year * cell_size
            x1 = x0 + cell_size
            y1 = y0 + cell_size
            color = "green" if (year * 52 + week) < weeks_passed else "white"
            draw.rectangle([x0, y0, x1, y1], fill=color, outline="black")

    img.save(output_path)

# Function to set the image as wallpaper
def set_wallpaper(image_path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)

# Main function to generate the image and set it as wallpaper
def main():
    birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
    output_path = os.path.join(os.getcwd(), 'life_in_weeks_wallpaper.bmp')

    create_life_image(birthdate, output_path)
    set_wallpaper(output_path)

if __name__ == "__main__":
    main()
