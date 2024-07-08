import tkinter as tk
from datetime import datetime, timedelta

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

# Main function to set up the GUI
def main():
    birthdate = input("Enter your birthdate (YYYY-MM-DD): ")

    # Set up the Tkinter window
    root = tk.Tk()
    root.title("Your Life in Weeks")
    root.geometry("800x800")

    # Initial grid creation
    update_grid(root, birthdate)

    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
