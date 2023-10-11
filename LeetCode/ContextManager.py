import os
import time
from contextlib import contextmanager

# @contextmanager
# def change_dir(destination):
#     try:
#         cwd = os.getcwd()
#         os.chdir(destination)
#         yield
#     finally:
#         os.chdir(cwd)

# with change_dir('LeetCode'):
#     print(os.listdir())

def check():
    time.sleep(1)

@contextmanager
def timer():
    start = time.perf_counter()
    try:
        yield
    finally:
        end = time.perf_counter()
        print(f"{end - start:.3f} secs")

with timer():
    check()