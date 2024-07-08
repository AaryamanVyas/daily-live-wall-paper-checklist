import os
import datetime
from PIL import Image, ImageDraw
import ctypes
import schedule
import time

# Constants
GRID_SIZE = (165, 133)  # Approximate to fit 21915 boxes
BOX_SIZE = 10  # Size of each box in pixels
MARGIN = 2  # Margin between boxes
WALLPAPER_PATH = 'wallpaper.png'  # Path to save the generated wallpaper

def generate_grid_image(days_passed):
    # Calculate dimensions
    img_width = GRID_SIZE[0] * (BOX_SIZE + MARGIN)
    img_height = GRID_SIZE[1] * (BOX_SIZE + MARGIN)
    
    # Create image
    image = Image.new('RGB', (img_width, img_height), color='white')
    draw = ImageDraw.Draw(image)
    
    for i in range(GRID_SIZE[1]):
        for j in range(GRID_SIZE[0]):
            box_number = i * GRID_SIZE[0] + j
            color = 'black' if box_number < days_passed else 'gray'
            top_left = (j * (BOX_SIZE + MARGIN), i * (BOX_SIZE + MARGIN))
            bottom_right = (top_left[0] + BOX_SIZE, top_left[1] + BOX_SIZE)
            draw.rectangle([top_left, bottom_right], fill=color)
    
    image.save(WALLPAPER_PATH)

def set_wallpaper():
    # Set wallpaper for Windows
    ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.abspath(WALLPAPER_PATH), 0)

def update_wallpaper():
    # Calculate days passed since a specific start date
    start_date = datetime.date(2023, 1, 1)
    today = datetime.date.today()
    days_passed = (today - start_date).days
    
    # Generate and set wallpaper
    generate_grid_image(days_passed)
    set_wallpaper()

def schedule_daily_update():
    # Schedule daily update at midnight
    schedule.every().day.at("00:00").do(update_wallpaper)

    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    update_wallpaper()  # Initial update
    schedule_daily_update()
