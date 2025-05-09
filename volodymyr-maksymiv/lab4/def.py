
def list_benefits():
    return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit


def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

def apply_to_list(func, data):
    return [func(x) for x in data]

def square(x):
    return x * x

numbers = [1, 2, 3, 4]
print(apply_to_list(square, numbers))

name_the_benefits_of_functions()