import os
from platform import system


def notify(title, text):
    if system().lower() == "darwin":
        os.system(
            """
                  osascript -e 'display notification "{}" with title "{}"'

            """.format(
                text, title
            )
        )
    elif system().lower() == "linux":
        os.system('notify-send "{}" "{}" --expire-time 500'.format(title, text))
