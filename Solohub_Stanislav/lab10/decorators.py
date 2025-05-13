class Circle:
    def __init__(self, radius):
        self._radius = radius  # захищене поле

    # Getter — декоратор @property
    @property
    def radius(self):
        return self._radius

    # Setter — перевіряє, що радіус додатній
    @radius.setter
    def radius(self, value):
        if value > 0:
            self._radius = value
        else:
            raise ValueError("Радіус має бути додатним числом.")

    # Deleter — дозволяє видалити радіус
    @radius.deleter
    def radius(self):
        print("Радіус видалено.")
        del self._radius

    # Властивість — площа кола (тільки для читання)
    @property
    def area(self):
        from math import pi
        return pi * self._radius ** 2

    # Властивість — діаметр кола (тільки для читання)
    @property
    def diameter(self):
        return self._radius * 2


# Демонстрація використання декораторів
def main():
    c = Circle(5)
    print(f"Початковий радіус: {c.radius}")
    print(f"Діаметр: {c.diameter}")
    print(f"Площа: {c.area:.2f}")

    print("\nЗміна радіуса на 10...")
    c.radius = 10
    print(f"Новий радіус: {c.radius}")
    print(f"Нова площа: {c.area:.2f}")

    print("\nСпроба задати недопустиме значення...")
    try:
        c.radius = -3
    except ValueError as e:
        print("Помилка:", e)

    print("\nВидалення радіуса...")
    del c.radius


if __name__ == "__main__":
    main()