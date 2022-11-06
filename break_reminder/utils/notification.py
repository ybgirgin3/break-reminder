from platform import system
from utils.alert import alert


# FIXME: icon needed 🔔
def notify(title, text, alert_sound):
    "system notification when session starts or ends"
    if system().lower() == "darwin":
        import os

        os.system(
            """
                  osascript -e 'display notification "{}" with title "{}"'
            """.format(
                text, title
            )
        )
    elif system().lower() == "linux":
        import os

        os.system('notify-send "{}" "{}" -t 500'.format(title, text))
    else:  # windows
        from winotify import Notification

        Notification(app_id="Break Reminder", title=f"{title}", msg=f"{text}")

    alert(alert=alert_sound)  ## play sound for notification
