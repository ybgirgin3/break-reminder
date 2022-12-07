from utils.time_extractor import lunch_time, time_extractor
from utils.notification import notify
from utils.sessions import session
from utils.progress import progress
from termcolor import colored
from tqdm import tqdm


def log(opt) -> str:
    "info about work session"
    # _ret = f"""
    # Total Work Time: {" ".join(opt.work_time.split("_"))}
    # Total Break Time: {" ".join(opt.break_time.split("_"))}
    # Full Day Of Work?: {'Yes' if opt.full else 'No'}
    # """

    ret = f"""
    Session Name: {opt.session_name}
    Total Work Time: {" ".join(opt.work_time.split("_"))}
    Total Break Time: {" ".join(opt.break_time.split("_"))}
    Full Day Of Work?: {'Yes' if opt.full else 'No'}
    """
    print(ret)
    return ret


def main(opt):
    "main"
    startapp_message = log(opt)
    session_count = opt.session_time
    lunch_break = lunch_time(opt.session_time)
    work_time = time_extractor(opt.work_time)
    break_time = time_extractor(opt.break_time)

    notify(title="Starting", text=startapp_message)

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


if __name__ == "__main__":
    # get info from user
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--session-name",
        type=str,
        default="Break-Reminder-Default-Session",  # 8 hours to default
        help="What is your desired session name (default: Break-Reminder-Default-Session)",
    )
    parser.add_argument(
        "--full",
        action="store_true",
        default=False,  # 8 hours to default
        help="Full Day of Work (8 hours default))",
    )
    parser.add_argument(
        "--session-time",
        type=int,
        default=1,  # 8 hours to default
        help="How many time you want to iterate over session",
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

    opt = parser.parse_args()
    main(opt)
