def say_hello():
    print("Hello!")

def run_twice(callback):
    callback()
    callback()

run_twice(say_hello)
