def change_difficulty(difficulty):
    """
    Change the difficulty of the game by changing distance between pipes
    :param difficulty: int, difficulty 1-4
    :return new_time_between_pipe: int, new time between pipes
    """
    new_time_between_pipe = 0
    if difficulty == 1:
        new_time_between_pipe = 1500
    if difficulty == 2:
        new_time_between_pipe = 1250
    if difficulty == 3:
        new_time_between_pipe = 1000
    if difficulty == 4:
        new_time_between_pipe = 750
    return new_time_between_pipe
