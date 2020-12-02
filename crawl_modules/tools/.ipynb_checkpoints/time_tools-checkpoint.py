# tools.time_tools.py

import random
import time


def random_sleep(min, max):
    """
    This function sleeps for a random random duration between min and max.
    Unit of variable is miliseconds
    """
    time.sleep(random.randint(min, max) / 1000)
