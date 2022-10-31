from utils.time_extractor import lunch_time, time_extractor
from utils.notification import notify
from utils.progress import progress
from tqdm import tqdm
import time


def work_session(work_t: int):
    "work time session counter"

    notify(
        title="Work Time Starting",
        text=opt.session_name,
    )

    progress(time_val=work_t, desc="Work Time Session", leave=False)


def break_session(break_t: int, big_break: bool = False):
    "break time session counter"

    if big_break:
        break_t = 60

    notify(
        title="Break Time Starting",
        text=opt.session_name,
    )

    progress(time_val=break_t, desc="Break Time Session", leave=False)


def main(opt):
    "main"
    session_count = opt.session_time
    big_break = lunch_time(opt.session_time)
    work_t = time_extractor(opt.work_time)
    break_t = time_extractor(opt.break_time)
    if opt.full:
        print("full day of working starts..")

    # FIXME: ana progress bar iki tane zaman içeriyor bunları
    # harici fonksiyonla nasıl yapabiliriz ona bakmam lazım
    # progress(time_val=session_count, desc="Main Session", leave=True)

    for sess in (pbar := tqdm(range(session_count), leave=True)):
        if (sess == big_break) and opt.full:
            desc = f"{sess}. Lunch Timeeeee 🧆"
            progress(time_val=big_break, desc=desc, leave=False)

            notify(
                title=desc,
                text=opt.session_name,
            )

        pbar.set_description_str(
            f"{sess}. {opt.work_time} long work session started.. "
        )
        work_session(work_t)
        pbar.set_description_str(
            f"{sess}. {opt.break_time} break time session started.."
        )
        break_session(break_t)
        pbar.refresh()

    notify(
        title="All Sessions Are Done, Well Done 👏",
        text=opt.session_name,
    )


if __name__ == "__main__":
    # get info from user
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--session-name",
        type=str,
        default="Break-Reminder-Default-Session",  # 8 hours to default
        help="How many session do you plan to work (hour(s))",
    )
    parser.add_argument(
        "--full",
        action="store_true",
        default=False,  # 8 hours to default
        help="How many session do you plan to work (hour(s))",
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
        help="work session time in minute",
    )

    opt = parser.parse_args()
    main(opt)
