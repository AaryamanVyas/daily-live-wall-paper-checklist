import os
import datetime
from PIL import Image, ImageDraw
import ctypes

# Constants
NUM_COLUMNS = 6
NUM_ROWS = 6
BOXES_PER_ROW = 6345 // (NUM_COLUMNS * NUM_ROWS)  # 6,345 boxes divided into 6 columns and 6 rows
GRID_SIZE = (NUM_COLUMNS, NUM_ROWS)
BOX_SIZE = 50  # Increase box size to fit more boxes
MARGIN = 10  # Increase margin to fit more boxes
COLUMN_MARGIN = 20  # Margin between columns
ROW_MARGIN = 20  # Margin between rows
WALLPAPER_PATH = 'wallpaper.png'

def generate_grid_image(days_passed):
    img_width = NUM_COLUMNS * BOX_SIZE + (NUM_COLUMNS - 1) * COLUMN_MARGIN
    img_height = NUM_ROWS * BOX_SIZE + (NUM_ROWS - 1) * ROW_MARGIN
    image = Image.new('RGB', (img_width, img_height), color='white')
    draw = ImageDraw.Draw(image)

    for col in range(NUM_COLUMNS):
        col_offset = col * (BOX_SIZE + COLUMN_MARGIN)
        for row in range(NUM_ROWS):
            row_offset = row * (BOX_SIZE + ROW_MARGIN)
            box_number = col * (NUM_ROWS * BOXES_PER_ROW) + row * BOXES_PER_ROW
            for i in range(BOXES_PER_ROW):
                if box_number < days_passed:
                    color = (0, 128, 255)  # Checked box color (blue)
                else:
                    color = (200, 200, 200)  # Unchecked box color (light gray)
                top_left = (col_offset, row_offset + i * BOX_SIZE)
                bottom_right = (top_left[0] + BOX_SIZE, top_left[1] + BOX_SIZE)
                draw.rectangle([top_left, bottom_right], fill=color)
                draw.rectangle([top_left, bottom_right], outline=(128, 128, 128), width=1)  # Add gridlines
                box_number += 1

    image.save(WALLPAPER_PATH)

def set_wallpaper():
    ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.abspath(WALLPAPER_PATH), 0)

def update_wallpaper():
    birth_date = datetime.date(2006, 1, 11)
    today = datetime.date.today()
    days_passed = (today - birth_date).days
    generate_grid_image(days_passed)
    set_wallpaper()

if __name__ == "__main__":
    update_wallpaper()
