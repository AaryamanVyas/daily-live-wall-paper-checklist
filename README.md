Live Wallpaper with Daily Updates

This project is a Python script that creates a dynamic live wallpaper for your laptop. The wallpaper updates daily, displaying a grid of 21,915 boxes where each box represents a day. The script automatically marks a box as checked each day.

### Features

- **Daily Updates**: The wallpaper updates itself every day at midnight.
- **Grid Display**: Displays a grid of 21,915 boxes, each representing a day.
- **Auto-Check**: Automatically marks a box as checked based on the number of days passed since a specified start date.

### Requirements

- Python 3.x
- [Pillow](https://python-pillow.org/)
- [Schedule](https://schedule.readthedocs.io/)

### Installation

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/your-username/live-wallpaper-daily-updates.git
    cd live-wallpaper-daily-updates
    ```

2. **Install the Required Libraries**:
    ```sh
    pip install pillow schedule
    ```

### Usage

1. **Edit the Script**:
    - Open `live_wallpaper.py` and modify the `start_date` variable in the `update_wallpaper` function to your desired start date.

2. **Run the Script**:
    ```sh
    python live_wallpaper.py
    ```

The script will:
- Generate an image with a grid of boxes.
- Update the image daily, marking the appropriate boxes as checked.
- Set the updated image as your desktop wallpaper.

### Project Structure

```plaintext
live-wallpaper-daily-updates/
│
├── live_wallpaper.py    # Main script for generating and updating the wallpaper
└── README.md            # Project description and instructions
```

### Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

