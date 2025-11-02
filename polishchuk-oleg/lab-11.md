# МІНІСТЕРСТВО ОСВІТИ ТА НАУКИ

## Львівський національний університет ветеринарії і біотехнологій імені С.З.Ґжицького

# Звіт

**про виконання лаборатоної роботи №11**

**з дисципліни "Об'єктно-орієнтоване програмування"**

**на тему**

**Твірні шаблони проєктування (декоратор )**

Виконав: студент групи КН-31 Поліщук Олег

Перевірив: ст. викладач Назар Заплатинський

### Львів 2025

**Мета роботи - Познайомитися з групою твірних шаблонів проєктування та реалізувати шаблон Singleton**

## Хід роботи

### Singleton - це твірний шаблон проєктування, який гарантує існування лише одного екземпляра класу та надає глобальну точку доступу до нього.

### Основна мета:

    - уникнути створення кількох екземплярів класу, які можуть конфліктувати між собою (наприклад, підключення до БД, логування, керування налаштуваннями тощо);
    - забезпечити централізоване керування спільним ресурсом.

### Основна ідея реалізації:

    - Конструктор класу роблять приватним, щоб заборонити створення об’єктів через new.
    - Створюють статичну приватну змінну для зберігання єдиного екземпляра.
    - Надають публічний статичний метод (getInstance()), який створює екземпляр при першому виклику і повертає його надалі.

### Приклад реалізації на пайтоні
import abc

class IPizza(abc.ABC):
    def __init__(self):
        self.description = "Невідома основа"
    
    def get_description(self) -> str:
        return self.description
    
    @abc.abstractmethod
    def get_cost(self) -> float:
        pass

class ThinCrustPizza(IPizza):
    def __init__(self):
        self.description = "Основа піци на тонкому тісті"
    
    def get_cost(self) -> float:
        return 5.99

class ThickCrustPizza(IPizza):
    def __init__(self):
        self.description = "Основа піци на товстому тісті"
    
    def get_cost(self) -> float:
        return 6.99

class ToppingDecorator(IPizza):
    def __init__(self, pizza: IPizza):
        self._wrapped_pizza = pizza
    
    @abc.abstractmethod
    def get_description(self) -> str:
        pass
    
    @abc.abstractmethod
    def get_cost(self) -> float:
        pass

class Cheese(ToppingDecorator):
    def get_description(self) -> str:
        return self._wrapped_pizza.get_description() + ", з сиром"
    
    def get_cost(self) -> float:
        return self._wrapped_pizza.get_cost() + 1.50

class Pepperoni(ToppingDecorator):
    def get_description(self) -> str:
        return self._wrapped_pizza.get_description() + ", з пепероні"
    
    def get_cost(self) -> float:
        return self._wrapped_pizza.get_cost() + 2.00

class Olives(ToppingDecorator):
    def get_description(self) -> str:
        return self._wrapped_pizza.get_description() + ", з оливками"
    
    def get_cost(self) -> float:
        return self._wrapped_pizza.get_cost() + 1.25

print("--- Створюємо просту піцу (лише основа) ---")
simple_pizza = ThinCrustPizza()
print(f"Піца: {simple_pizza.get_description()}")
print(f"Ціна: ${simple_pizza.get_cost():.2f}")

print("\n--- Створюємо Пепероні на товстому тісті ---")
my_pizza: IPizza = ThickCrustPizza()
my_pizza = Cheese(my_pizza)
my_pizza = Pepperoni(my_pizza)

print(f"Піца: {my_pizza.get_description()}")
print(f"Ціна: ${my_pizza.get_cost():.2f}")

print("\n--- Створюємо вегетаріанську з подвійним сиром та оливками ---")
complex_pizza = ThinCrustPizza()
complex_pizza = Cheese(complex_pizza)
complex_pizza = Cheese(complex_pizza)
complex_pizza = Olives(complex_pizza)

print(f"Піца: {complex_pizza.get_description()}")
print(f"Ціна: ${complex_pizza.get_cost():.2f}")
```

### Запуск прикладу:

```bash
node singleton.js
```

## Висновок:

В ході виконання лабораторної роботи було реалізовано шаблон Singleton, який необхідний для того, щоб у програмі існував лише один екземпляр певного класу, і щоб до нього можна було глобально звернутися. Шаблон особливо корисний для керування спільними ресурсами та забезпечення єдиної точки доступу до них.
