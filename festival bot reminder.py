import datetime
from plyer import notification
import time

def get_festivals():
    """
    Returns a dictionary of festivals with their dates.
    You can expand this with more festivals.
    For demonstration, we'll use a few examples.
    Note: For recurring annual festivals, you'd typically adjust the year
          dynamically or use a more sophisticated festival data source.
          Here, we're hardcoding for simplicity.
    """
    current_year = datetime.date.today().year
    festivals = {
        "Independence Day": datetime.date(current_year, 8, 15),
        "Diwali": datetime.date(current_year, 10, 31), # Example date, will vary
        "Christmas": datetime.date(current_year, 12, 25),
        "New Year's Day": datetime.date(current_year + 1, 1, 1),
        "Republic Day": datetime.date(current_year + 1, 1, 26),
        # Add a festival that might be today or very soon for testing
        
    }
    return festivals

def send_festival_notification(festival_name, festival_date, days_left):
    """Sends a desktop notification for an upcoming festival."""
    title = f"Festival Reminder: {festival_name}"
    if days_left == 0:
        message = f"🎉 Today is {festival_name}! Enjoy the celebrations!"
    elif days_left == 1:
        message = f"Tomorrow is {festival_name}! Get ready!"
    else:
        message = f"{festival_name} is in {days_left} days ({festival_date.strftime('%B %d, %Y')})."

    try:
        notification.notify(
            title=title,
            message=message,
            app_name="Festival Bot",
            timeout=10  # Notification will disappear after 10 seconds
        )
        print(f"Notification sent for: {festival_name} - {message}")
    except Exception as e:
        print(f"Error sending notification for {festival_name}: {e}")
        print("Please ensure your system supports plyer notifications (e.g., `pip install plyer` and appropriate backend like `kivy` or `WinRT` on Windows, `dbus` on Linux).")


def check_festivals():
    """Checks for upcoming festivals and sends notifications."""
    today = datetime.date.today()
    festivals = get_festivals()
    print(f"Checking festivals for today: {today}")

    found_upcoming_festival = False
    for festival_name, festival_date in festivals.items():
        delta = festival_date - today
        days_left = delta.days

        # Trigger notification if festival is today, tomorrow, or within the next 7 days
        if 0 <= days_left <= 7:
            send_festival_notification(festival_name, festival_date, days_left)
            found_upcoming_festival = True

    if not found_upcoming_festival:
        print("No upcoming festivals within the next 7 days.")

def main_loop(check_interval_seconds=3600): # Check every hour (3600 seconds)
    """
    Main loop to periodically check for festivals.
    In a real-world bot, you'd typically use a system scheduler (Cron/Task Scheduler).
    """
    print("Festival Bot started. Checking for festivals...")
    print(f"Will check every {check_interval_seconds / 60} minutes.")
    while True:
        check_festivals()
        print(f"Next check in {check_interval_seconds / 60} minutes...")
        time.sleep(check_interval_seconds)

if __name__ == "__main__":
    # You can choose to run it once or in a continuous loop
    # For a quick test, just run once:
    check_festivals()

    # To run as a continuous bot (uncomment the line below):
    # main_loop(check_interval_seconds=60) # For testing, check every minute
    # main_loop(check_interval_seconds=24 * 3600) # For daily checks, run once a day

