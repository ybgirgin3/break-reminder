from tqdm import tqdm
from time import sleep


def progress(time_val: int, desc: str = "Default Desc", leave: bool = False):

    for nth_time in (pbar := tqdm(range(time_val), leave=leave)):
        pbar.set_description_str(f"{nth_time} time: {desc}")
        pbar.refresh()
        sleep(1)

    # for _break in (pbar := tqdm(range(break_t), leave=False)):
    #     pbar.set_description_str(f"Work Time Session ({_break} seconds passed)")
    #     pbar.refresh()
    #     time.sleep(1)
