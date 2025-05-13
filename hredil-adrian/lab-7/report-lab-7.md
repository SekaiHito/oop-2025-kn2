# МІНІСТЕРСТВО ОСВІТИ ТА НАУКИ

## Львівський національний університет ветеринарії і біотехнологій імені С.З.Ґжицького

# Звіт

**про виконання лаборатоної роботи №7**

**з дисципліни "Об'єктно-орієнтоване програмування"**

**на тему** 

**Створення та використання класів.**

Виконав: студент групи КН-21 Греділь Адріан

Перевірив: доц. А.Татомир

### Львів 2025

Мета роботи полягає в ознайомленні з різними типами методів у об’єктно-орієнтованому програмуванні.

## Хід роботи

1. Засвоїв різницю між звичайними методами, методами класу та статичними методами.

```py

class Phone:
    default_os = "Android"

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show_info(self):
        return f"Phone: {self.brand} {self.model} with {Phone.default_os} OS"

    @classmethod
    def change_default_os(cls, new_os):
        cls.default_os = new_os
        print(f"Default OS changed to: {cls.default_os}")

    @staticmethod
    def is_valid_year(year):
        return 1990 <= year <= 2025


phone1 = Phone("Samsung", "Galaxy S21")
print(phone1.show_info())

Phone.change_default_os("HarmonyOS")
print(phone1.show_info())

print(Phone.is_valid_year(2021))
print(phone1.is_valid_year(1980))


```

2. Навчився створювати альтернативні конструктори.
Для цього я використовував метод класу, який повертає новий екземпляр класу, зазвичай після певної попередньої обробки даних.

```py

class Phone:
    default_os = "Android"

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @classmethod
    def from_string(cls, data_str):
        brand, model = data_str.split('-')
        return cls(brand.strip(), model.strip())

    def show_info(self):
        return f"Phone: {self.brand} {self.model} with {Phone.default_os} OS"


phone2 = Phone.from_string("Apple - iPhone 13")
print(phone2.show_info())


```

3. Реалізував метод класу для створеного раніше класу, який працює зі змінними класу.
Це дало змогу змінювати або використовувати загальні для всіх об'єктів дані, що зберігаються у змінних класу.

```py

class Phone:
    default_os = "Android"

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @classmethod
    def change_default_os(cls, new_os):
        cls.default_os = new_os
        print(f"Default OS changed to: {cls.default_os}")

    def show_info(self):
        return f"Phone: {self.brand} {self.model} with {Phone.default_os} OS"


Phone.change_default_os("iOS")

phone3 = Phone("Apple", "iPhone 14")
print(phone3.show_info())


```

4. Реалізував альтернативний конструктор класу за допомогою методу класу.
Такий підхід зручний, коли потрібно створювати об'єкти на основі даних з іншого формату, наприклад, зі словника чи рядка.

```py

class Phone:
    default_os = "Android"

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @classmethod
    def from_dict(cls, data):
        return cls(data["brand"], data["model"])

    def show_info(self):
        return f"Phone: {self.brand} {self.model} with {Phone.default_os} OS"


phone_data = {
    "brand": "Xiaomi",
    "model": "Redmi Note 12"
}

phone4 = Phone.from_dict(phone_data)
print(phone4.show_info())

```

5. Створив статичний метод і перевірив його роботу.
Цей метод виконував логічну операцію, яка не залежала від конкретного стану об’єкта або класу, та успішно виконувався як через сам клас, так і через екземпляр.

```py

class Phone:
    default_os = "Android"

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @staticmethod
    def is_valid_model_name(name):
        return isinstance(name, str) and len(name.strip()) > 0

    def show_info(self):
        return f"Phone: {self.brand} {self.model} with {Phone.default_os} OS"


print(Phone.is_valid_model_name("Galaxy S24"))

phone5 = Phone("Samsung", "Galaxy S24")
print(phone5.is_valid_model_name(""))

```

## Висновок:

У ході виконання даної роботи я навчився розрізняти звичайні методи, методи класа і статичні методи. Я поняв, як можна створювати альтернативні конструктори для зручності ініціалізації об'єктів з інших форматів, таких як рядок або словник. Також реалізував метод класу, який міняє змінну класа, і зробив статичний метод, який працює незалежно від об'єкта. Було цікаво, місцями складно, але в загальному все понятно.