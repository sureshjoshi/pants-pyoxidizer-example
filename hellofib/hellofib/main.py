import time 

def run():
    def fib(n: int) -> int:
        if n <= 1:
            return n
        else:
            return fib(n - 2) + fib(n - 1)
    
    start_time = time.time()
    fib(34)
    print(f"Calculating fibs(34) took {time.time() - start_time} seconds")


# In .bzl config, setting python_config.run_module = "hellofib.main" should cause this to run as the entry point
if __name__ == "__main__":
    print("Launching HelloFib from __main__")
    run()
