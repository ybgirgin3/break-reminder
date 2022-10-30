from utils.time_extractor import time_extractor
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

    # for work in (pbar := tqdm(range(work_t), leave=False)):
    #     pbar.set_description_str(f"Work Time Session ({work} seconds passed)")
    #     pbar.refresh()
    #     time.sleep(1)


def break_session(break_t: int):
    "break time session counter"

    notify(
        title="Break Time Starting",
        text=opt.session_name,
    )

    progress(time_val=break_t, desc="Break Time Session", leave=False)

    # for _break in (pbar := tqdm(range(break_t), leave=False)):
    #     pbar.set_description_str(f"Break Time Session ({_break} seconds passed)")
    #     pbar.refresh()
    #     time.sleep(1)


def main(opt):
    "main"
    session_count = opt.session_time
    work_t = time_extractor(opt.work_time)
    break_t = time_extractor(opt.break_time)

    for sess in (pbar := tqdm(range(session_count), leave=True)):
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
