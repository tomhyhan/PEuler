import time 
def time_checker(func):
    def inner():
        start_time = time.time()
        func()
        end_time = time.time()
        print("Execution time: ", f"{end_time - start_time:.2f}", "seconds")
    return inner    
