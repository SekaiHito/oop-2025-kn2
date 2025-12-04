# До рефакторингу
def calculate_area(width, height):
    area = width * height
    print("Площа:", area)
    return area

# Після рефакторингу
def calculate_area(width, height):
    return width * height

def print_area(width, height):
    area = calculate_area(width, height)
    print("Площа:", area)

