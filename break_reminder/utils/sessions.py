from utils.notification import notify
from utils.progress import progress


def session(
    session_name: str,
    desc: str,
    time_val: int,
    # if break time
    leave: bool = False,
):
    "session time controller"

    _title = f"{session_name}"
    _text = f"Break Reminder: {_title}"

    notify(
        title=desc,
        text=_text,
    )

    if progress(time_val=time_val, desc=desc, leave=leave):
        return True
