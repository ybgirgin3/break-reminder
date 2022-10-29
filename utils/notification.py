import os
from platform import system


def notify(title, text):
    if system() == "darwin":
        os.system(
            """
                  osascript -e 'display notification "{}" with title "{}"'

            """.format(
                text, title
            )
        )
    elif system() == "linux":
        os.system('notify-send "{}" "{}"'.format(title, text))
