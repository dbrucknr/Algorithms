import threading
import time


def dummy():
    print("Dummy function: Start a thread")
    time.sleep(3)
    print("Dummy function: 3 seconds have passed - END!")


def run_functions_concurrently(function_array):
    threads = []
    for function in function_array:
        th = threading.Thread(target=function)
        th.start()
        threads.append(th)

    for thread in threads:
        thread.join()


fun_array = [dummy, dummy, dummy]

run_functions_concurrently(fun_array)
