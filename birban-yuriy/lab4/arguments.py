def greet(name):  # name — параметр

    greet("Ivan")  # "Ivan" — аргумент
    
def greet(name="Guest"):
    return f"Hi, {name}"
