def check_done(log_list, num):
    """
    Checks if the given number of tasks have been completed.

    Args:
        log_list (list): A list of log messages.
        num (int): The number of tasks to check for.

    Returns:
        bool: True if the given number of tasks have been completed, False otherwise.
    """

    done_count = 0
    for log in log_list:
        if "done" in log:
            done_count += 1

    return done_count >= num

