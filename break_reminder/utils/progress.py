from tqdm import tqdm
from time import sleep


def progress(time_val: int, desc: str = "work", leave: bool = False):
    "create progress bar for desired session"
    for _ in (pbar := tqdm(range(time_val), leave=leave)):
        pbar.set_description_str(f"Single Session: {desc.upper()} : ")
        pbar.refresh()
        sleep(1)

    return True  # done
