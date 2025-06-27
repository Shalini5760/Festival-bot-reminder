import datetime
from plyer import notification
import time

def get_festivals():
    current_year = datetime.date.today().year
    festivals = {
        "Independence Day": datetime.date(current_year, 8, 15),
        "Diwali": datetime.date(current_year, 10, 31), 
        "Christmas": datetime.date(current_year, 12, 25),
        "New Year Day": datetime.date(current_year + 1, 1, 1),
        "Republic Day": datetime.date(current_year + 1, 1, 26),
        "vinayagar chadurti":datetime.date(current_year + 1, 8, 27),
        "ponga":datetime.date(current_year + 1, 1, 15),
        "Tamil new_year":datetime.date(current_year + 1, 4, 14),
        "labours day":datetime.daye(current_year + 1, 5, 1),
        "gandhi jayanthi":datetime.date(current_year + 1, 10, 2)
        
    }
    return festivals

def send_festival_notification(festival_name, festival_date, days_left):
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
            timeout=10 
        )
        print(f"Notification sent for: {festival_name} - {message}")
    except Exception as e:
        print(f"Error sending notification for {festival_name}: {e}")
        print("Please ensure your system supports plyer notifications (e.g., `pip install plyer` and appropriate backend like `kivy` or `WinRT` on Windows, `dbus` on Linux).")


def check_festivals():
    today = datetime.date.today()
    festivals = get_festivals()
    print(f"Checking festivals for today: {today}")

    found_upcoming_festival = False
    for festival_name, festival_date in festivals.items():
        delta = festival_date - today
        days_left = delta.days

        if 0 <= days_left <= 7:
            send_festival_notification(festival_name, festival_date, days_left)
            found_upcoming_festival = True

    if not found_upcoming_festival:
        print("No upcoming festivals within the next 7 days.")

def main_loop(check_interval_seconds=3600):
    print("Festival Bot started. Checking for festivals...")
    print(f"Will check every {check_interval_seconds / 60} minutes.")
    while True:
        check_festivals()
        print(f"Next check in {check_interval_seconds / 60} minutes...")
        time.sleep(check_interval_seconds)

if __name__ == "__main__":
   
    check_festivals()
