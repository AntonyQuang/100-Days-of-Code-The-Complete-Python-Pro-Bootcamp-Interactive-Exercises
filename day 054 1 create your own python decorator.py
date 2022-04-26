import time
current_time = time.time()
print(current_time)

def speed_calc_decorator(function):
    def speed_calc():
        function()
        finish_time = time.time()
        run_time = finish_time - current_time
        print(f"{function.__name__} run speed: {run_time}s")
    return speed_calc


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i

fast_function()
slow_function()
