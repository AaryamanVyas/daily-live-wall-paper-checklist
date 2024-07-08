import os
import datetime
from PIL import Image, ImageDraw
import ctypes
import schedule
import time

# Constants
NUM_COLUMNS = 6
BOXES_PER_COLUMN = 6345 // NUM_COLUMNS  # 6,345 boxes divided into 6 columns
GRID_SIZE = (NUM_COLUMNS, BOXES_PER_COLUMN)
BOX_SIZE = 5  # Reduce box size to fit more boxes
MARGIN = 1  # Reduce margin to fit more boxes
COLUMN_MARGIN = 20  # Margin between columns
WALLPAPER_PATH = 'wallpaper.png'

def generate_grid_image(days_passed):
    img_width = NUM_COLUMNS * (BOX_SIZE + MARGIN) + (NUM_COLUMNS - 1) * COLUMN_MARGIN
    img_height = BOXES_PER_COLUMN * (BOX_SIZE + MARGIN)
    image = Image.new('RGB', (img_width, img_height), color='white')
    draw = ImageDraw.Draw(image)

    for col in range(NUM_COLUMNS):
        col_offset = col * (BOX_SIZE + MARGIN + COLUMN_MARGIN)
        for i in range(BOXES_PER_COLUMN):
            box_number = col * BOXES_PER_COLUMN + i
            if box_number < days_passed:
                color = (0, 128, 255)  # Checked box color (blue)
            else:
                color = (200, 200, 200)  # Unchecked box color (light gray)
            top_left = (col_offset, i * (BOX_SIZE + MARGIN))
            bottom_right = (top_left[0] + BOX_SIZE, top_left[1] + BOX_SIZE)
            draw.rectangle([top_left, bottom_right], fill=color)
            draw.rectangle([top_left, bottom_right], outline=(128, 128, 128), width=1)  # Add gridlines

    image.save(WALLPAPER_PATH)

def set_wallpaper():
    ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.abspath(WALLPAPER_PATH), 0)

def update_wallpaper():
    birth_date = datetime.date(2006, 1, 11)
    today = datetime.date.today()
    days_passed = (today - birth_date).days
    generate_grid_image(days_passed)
    set_wallpaper()

def schedule_daily_update():
    schedule.every().day.at("00:00").do(update_wallpaper)
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    update_wallpaper()
    schedule_daily_update()