from platform import system


# FIXME: icon needed 🔔
def notify(title, text):
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
        os.system('notify-send "{}" "{}"'.format(title, text))
    else:  # windows
        from winotify import Notification
        Notification(app_id="Break Reminder", title=f"{title}", msg=f"{text}")
