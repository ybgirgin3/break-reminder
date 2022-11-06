from utils.time_extractor import lunch_time, time_extractor
from utils.notification import notify
from utils.sessions import session
from utils.progress import progress
from utils import log
from termcolor import colored
from tqdm import tqdm


def main(opt):
    "main"
    log(opt)
    session_count = opt.session_time
    lunch_break = lunch_time(opt.session_time)
    work_time = time_extractor(opt.work_time)
    break_time = time_extractor(opt.break_time)

    # * session starts..
    for sess in (
        pbar := tqdm(range(session_count), leave=True)
    ):  ## * main pbar always on the top

        # lunch break 🥞
        if (sess == lunch_break) and opt.full:
            print("full of day of working starting....")

            # create progress bar for lunch_break
            pbar_desc = f"{sess}. lunch break 🥞"
            progress(time_val=lunch_break, desc=pbar_desc, leave=False)

            # notify
            notify(
                title=pbar_desc,
                text=opt.session_name,
                alert_sound=opt.custom_alert_sound,
            )

        # start work sessions
        pbar.set_description_str(
            f"{sess}. {' '.join(opt.work_time.split('_'))} long work session progress: "
        )

        if session(
            session_name=opt.session_name, desc="Work Time", time_val=work_time
        ):  ## work time
            print(colored("\nWork session done", "yellow"))

        # start break session
        pbar.set_description_str(
            f"{sess}. {' '.join(opt.break_time.split('_'))} long break session progress: "
        )

        if session(
            session_name=opt.session_name, desc="Break Time", time_val=break_time
        ):  ## break time
            print(colored("\nBreak session done", "yellow"))


def save_args(opt) -> bool:
    """
    import json

    # Data to be written
    dictionary ={
        "name" : "sathiyajith",
        "rollno" : 56,
        "cgpa" : 8.6,
        "phonenumber" : "9976770500"
    }

    with open("sample.json", "w") as outfile:
        json.dump(dictionary, outfile)

    """
    fn = "argparse.json"

    ret = {
        "session_name": opt.session_name,
        "full": opt.full,
        "session_time": opt.session_time,
        "work_time": opt.work_time,
        "break_time": opt.break_time,
        "custom_alert_sound": opt.custom_alert_sound,
    }

    from pprint import pprint
    import json

    pprint(str(ret))
    with open(fn, "w") as outfile:
        json.dump(ret, outfile)


if __name__ == "__main__":
    # get info from user
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--session-name",
        type=str,
        default="Break-Reminder-Default-Session",  # 8 hours to default
        help="Custom Session Name)",
    )
    parser.add_argument(
        "--full",
        action="store_true",
        default=False,  # 8 hours to default
        help="Do you plan to work in full day row)",
    )
    parser.add_argument(
        "--session-time",
        type=int,
        default=8,  # 8 hours to default
        help="How many session do you plan to work (hour(s))",
    )
    parser.add_argument(
        "--work-time",
        type=str,
        default="50_min",  # 50 min for default
        help="work session time in minute",
    )
    parser.add_argument(
        "--break-time",
        type=str,
        default="10_min",  # 10 min for default
        help="break session time in minute",
    )
    parser.add_argument(
        "--custom-alert-sound",
        type=str,
        default="break_reminder/utils/media/alert.wav",  # 10 min for default
        help="Custom alert sound to play with system notification",
    )

    opt = parser.parse_args()
    save_args(opt)
    # main(opt)
