
def log(opt) -> None:
    "info about work session"
    print(
        f"""
        Session Name: {opt.session_name}
        Total Work Time: {" ".join(opt.work_time.split("_"))}
        Total Break Time: {" ".join(opt.break_time.split("_"))}
        Full Day Of Work?: {'Yes' if opt.full else 'No'}
    """
    )


