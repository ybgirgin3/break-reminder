from utils.notification import notify
from utils.progress import progress


def session(
    session_name: str,
    time_val: int,
    # if break time
    leave: bool = False,
):
    "session time controller"

    _title = f"{session_name}"

    notify(
        title=_title,
        text=session_name,
    )

    if progress(time_val=time_val, desc=_title, leave=leave):
        return True
