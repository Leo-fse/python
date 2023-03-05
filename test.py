import datetime
import os

"wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww"


def func(a: int, b: str, c: list) -> dict:
    """_summary_

    Args:
        a (int): _description_
        b (str): _description_
        c (list): _description_

    Returns:
        dict: _description_
    """
    return {}


files = os.listdir("../")

a = 1
sample_list = range(0, 100, 5)
for val in sample_list:
    if val // 2 == 0:
        print(val)

print(files)
print(datetime.datetime.now())
