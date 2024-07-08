import os
import datetime
from PIL import Image, ImageDraw
import ctypes

# Constants
NUM_COLUMNS = 105
NUM_ROWS = 60
BOXES_PER_ROW = 6345 // (NUM_COLUMNS * NUM_ROWS)  # 6,345 boxes divided into columns and rows
GRID_SIZE = (NUM_COLUMNS, NUM_ROWS)
BOX_SIZE = 10  # Adjust box size to fit more boxes
MARGIN = 2  # Adjust margin to fit more boxes
COLUMN_MARGIN = 5  # Margin between columns
ROW_MARGIN = 5  # Margin between rows
WALLPAPER_PATH = 'wallpaper.png'

def generate_grid_image(days_passed):
    # Calculate the width and height of the wallpaper
    img_width = (NUM_COLUMNS * BOX_SIZE + (NUM_COLUMNS - 1) * COLUMN_MARGIN)
    img_height = (NUM_ROWS * BOX_SIZE + (NUM_ROWS - 1) * ROW_MARGIN)
    print(f"Image dimensions: {img_width}x{img_height}")

    # Calculate the rectangle dimensions
    rect_width = img_width
    rect_height = img_height
    rect_x1 = 0
    rect_y1 = 0
    rect_x2 = rect_width - 1
    rect_y2 = rect_height - 1
    print(f"Rectangle coordinates: ({rect_x1}, {rect_y1}) - ({rect_x2}, {rect_y2})")

    image = Image.new('RGB', (img_width, img_height), color='white')
    draw = ImageDraw.Draw(image)

    # Draw the full-screen rectangle
    draw.rectangle([rect_x1, rect_y1, rect_x2, rect_y2], outline=(128, 128, 128), width=2)

    # Draw the checklist boxes inside the rectangle
    for col in range(NUM_COLUMNS):
        col_offset = col * (BOX_SIZE + MARGIN + COLUMN_MARGIN)
        for row in range(NUM_ROWS):
            row_offset = row * (BOX_SIZE + MARGIN + ROW_MARGIN)
            for i in range(BOXES_PER_ROW):
                box_number = col * (NUM_ROWS * BOXES_PER_ROW) + row * BOXES_PER_ROW + i
                if box_number < days_passed:
                    color = (0, 128, 255)  # Checked box color (blue)
                else:
                    color = (200, 200, 200)  # Unchecked box color (light gray)
                top_left = (col_offset + i * (BOX_SIZE + MARGIN), row_offset)
                bottom_right = (top_left[0] + BOX_SIZE, top_left[1] + BOX_SIZE)
                print(f"Box {box_number}: ({top_left[0]}, {top_left[1]}) - ({bottom_right[0]}, {bottom_right[1]})")
                draw.rectangle([top_left, bottom_right], fill=color)
                draw.rectangle([top_left, bottom_right], outline=(128, 128, 128), width=1)  # Add gridlines

    image.save(WALLPAPER_PATH)

def set_wallpaper():
    ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.abspath(WALLPAPER_PATH), 0)

def update_wallpaper():
    birth_date = datetime.date(2006, 1, 11)
    today = datetime.date.today()
    days_passed = 3000  # Use 3000 instead of 6340
    generate_grid_image(days_passed)
    set_wallpaper()

if __name__ == "__main__":
    update_wallpaper()
