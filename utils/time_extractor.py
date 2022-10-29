def time_extractor(str_time: str):
    """default time definition: 10_min/10_MIN"""

    time_definitions = {
        "sec": 1,
        "min": 60,
        "hrs": 60 * 60,
    }

    time_int, time_str = str_time.split("_")

    return eval(f"{time_int} * {time_definitions[time_str.lower()]}")
