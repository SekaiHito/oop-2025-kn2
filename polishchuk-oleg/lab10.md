
## Міністерство освіти і науки України

## Львівський національний університет ветеринарії і біотехнологій імені С.З.Ґжицького

# Звіт

про виконання лаборатоної роботи №10 з дисципліни ***Об'єктно-орієнтоване програмування*** на тему **Використання декораторів методів**

Виконала: студент групи КН-21 **Поліщук Олег**

Прийняв: доц. А.Татомир

## Львів 2025

Мета: освоїти роботу з декораторами в Python 3.

## Хід роботи

1. Навчилися використовувати декоратор “@property”. Написали принаймні один метод з його використанням.

2. Ознайомилися з концепцією getter’ів, setter’ів і delete’рів. Реалізували хоча б один метод з їх використанням.

```py

class Profile:

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def contact(self):
        return f"{self._first_name}.{self._last_name}@profile.net"

    @property
    def full_identity(self):
        return f"{self._first_name} {self._last_name}"

    @full_identity.setter
    def full_identity(self, new_name):
        names = new_name.split(' ')
        if len(names) == 2:
            self._first_name, self._last_name = names
        else:
            raise ValueError("Invalid format. Provide 'First Last'.")

    @full_identity.deleter
    def full_identity(self):
        print("Clearing identity...")
        self._first_name = "Unknown"
        self._last_name = "User"

# Створення екземпляра
profile_1 = Profile("Echo", "Storm")
profile_1.full_identity = "Nova Pulse"

print(profile_1._first_name)  
print(profile_1.contact)  
print(profile_1.full_identity)  

del profile_1.full_identity  
```
## Висновки

дівзнався по таку річ як директори 
