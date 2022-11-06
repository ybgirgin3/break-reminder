import subprocess
import os

# call main function

ROOT = os.path.dirname(os.path.abspath(__file__))
# print(ret)

# python main.py --session-time 2 --work-time 5_sec --break-time 3_sec --session-name Bekocan
subprocess.Popen(
    [
        "python",
        f"{ROOT}/break_reminder/main.py",
        "--session-time",
        "2",
        "--work-time",
        "5_sec",
        "--break-time",
        "3_sec",
        "--session-name",
        "Bekocan",
    ]
)
