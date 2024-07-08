import os
import datetime
from PIL import Image, ImageDraw
import ctypes

# Constants
NUM_COLUMNS = 6
NUM_ROWS = 6
BOXES_PER_ROW = 6345 // (NUM_COLUMNS * NUM_ROWS)  # 6,345 boxes divided into 6 columns and 6 rows
GRID_SIZE = (NUM_COLUMNS, NUM_ROWS)
BOX_SIZE = 10  # Adjust box size to fit more boxes
MARGIN = 2  # Adjust margin to fit more boxes
COLUMN_MARGIN = 5  # Margin between columns
ROW_MARGIN = 5  # Margin between rows
WALLPAPER_PATH = 'wallpaper.png'

def generate_grid_image(days_passed):
    # Calculate the width and height of the wallpaper
    img_width = 1920
    img_height = 1080
    image = Image.new('RGB', (img_width, img_height), color='white')
    draw = ImageDraw.Draw(image)

    # Calculate the dimensions of the left and right rectangles
    rect_width = (img_width // 2) - 50
    rect_height = img_height - 100
    left_rect_x1 = 50
    left_rect_y1 = 50
    left_rect_x2 = left_rect_x1 + rect_width
    left_rect_y2 = left_rect_y1 + rect_height
    right_rect_x1 = img_width - left_rect_x2 - 50
    right_rect_y1 = 50
    right_rect_x2 = right_rect_x1 + rect_width
    right_rect_y2 = right_rect_y1 + rect_height

    # Draw the left rectangle
    draw.rectangle([left_rect_x1, left_rect_y1, left_rect_x2, left_rect_y2], outline=(128, 128, 128), width=2)

    # Draw the right rectangle
    draw.rectangle([right_rect_x1, right_rect_y1, right_rect_x2, right_rect_y2], outline=(128, 128, 128), width=2)

    # Draw the checklist boxes in the left rectangle
    for col in range(NUM_COLUMNS):
        col_offset = left_rect_x1 + col * (BOX_SIZE + MARGIN + COLUMN_MARGIN)
        for row in range(NUM_ROWS):
            row_offset = left_rect_y1 + row * (BOX_SIZE + MARGIN + ROW_MARGIN)
            box_number = col * (NUM_ROWS * BOXES_PER_ROW) + row * BOXES_PER_ROW
            for i in range(BOXES_PER_ROW):
                if box_number < days_passed:
                    color = (0, 128, 255)  # Checked box color (blue)
                else:
                    color = (200, 200, 200)  # Unchecked box color (light gray)
                top_left = (col_offset + i * (BOX_SIZE + MARGIN), row_offset)
                bottom_right = (top_left[0] + BOX_SIZE, top_left[1] + BOX_SIZE)
                draw.rectangle([top_left, bottom_right], fill=color)
                draw.rectangle([top_left, bottom_right], outline=(128, 128, 128), width=1)  # Add gridlines
                box_number += 1

    # Draw the checklist boxes in the right rectangle
    for col in range(NUM_COLUMNS):
        col_offset = right_rect_x1 + col * (BOX_SIZE + MARGIN + COLUMN_MARGIN)
        for row in range(NUM_ROWS):
            row_offset = right_rect_y1 + row * (BOX_SIZE + MARGIN + ROW_MARGIN)
            box_number = (col + NUM_COLUMNS) * (NUM_ROWS * BOXES_PER_ROW) + row * BOXES_PER_ROW
            for i in range(BOXES_PER_ROW):
                if box_number < days_passed:
                    color = (0, 128, 255)  # Checked box color (blue)
                else:
                    color = (200, 200, 200)  # Unchecked box color (light gray)
                top_left = (col_offset + i * (BOX_SIZE + MARGIN), row_offset)
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
