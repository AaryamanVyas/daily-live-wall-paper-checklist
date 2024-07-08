import tkinter as tk
from datetime import datetime, timedelta
import win32api
import win32con
import win32gui

# Function to calculate the number of weeks since the birthdate
def weeks_since_birth(birthdate):
    birth_date = datetime.strptime(birthdate, '%Y-%m-%d')
    current_date = datetime.now()
    delta = current_date - birth_date
    return delta.days // 7

# Function to create the grid and update it
def create_life_grid(root, weeks_passed):
    for year in range(100):
        for week in range(52):
            color = "green" if (year * 52 + week) < weeks_passed else "white"
            frame = tk.Frame(
                master=root,
                relief=tk.RAISED,
                borderwidth=1,
                width=10,
                height=10,
                bg=color
            )
            frame.grid(row=year, column=week)

# Function to update the grid regularly
def update_grid(root, birthdate):
    weeks_passed = weeks_since_birth(birthdate)
    create_life_grid(root, weeks_passed)
    root.after(86400000, update_grid, root, birthdate)  # Update every day (86400000 ms)

# Main function to set up the GUI and set as wallpaper
def main():
    birthdate = input("Enter your birthdate (YYYY-MM-DD): ")

    # Set up the Tkinter window
    root = tk.Tk()
    root.title("Your Life in Weeks")
    root.geometry("800x800")

    # Set the window as a desktop widget
    hwnd = root.winfo_id()
    win32gui.SetParent(hwnd, win32gui.FindWindow("Progman", None))
    win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, win32con.WS_CHILD | win32con.WS_VISIBLE)
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

    # Initial grid creation
    update_grid(root, birthdate)

    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
