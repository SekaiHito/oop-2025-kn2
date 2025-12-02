## Міністерство освіти і науки України
## Львівський національний університет ветеринарії і біотехнологій імені С.З.Ґжицького

# Звіт
про виконання лабораторної роботи №4 з дисципліни "**Об'єктно орієнтоване програмування**"  
на тему: **Принципи SOLID в об’єктно-орієнтованому програмуванні**

Виконав: студент групи **КН-31** Салтиков Павло  
Прийняв: викл. **Н.Заплатинський**

Львів 2025

---

## **Мета**
Ознайомитися з основними принципами SOLID у об’єктно-орієнтованому програмуванні та реалізувати декілька із них — (SRP, OCP) — на прикладі коду мовою Python.

---

## **Хід роботи**

1. **Ознайомився з теоретичними основами.**  
    S - Single Responsibility Principle

    Клас повинен виконувати тільки одну логічну задачу.
    Чим менше відповідальностей у класу тим легше змінювати код.

    O - Open/Closed Principle

    Код має бути відкритий для розширення, але закритий для змін.
    Ідея: ти не лізеш переписувати старий код, а додаєш нові класи.

    L - Liskov Substitution Principle

    Похідний клас повинен повністю замінювати базовий.
    Тобто де очікується батьківський клас - дочірній повинен працювати без проблем.

    I - Interface Segregation Principle

    Великі інтерфейси погано.
    Краще багато маленьких, ніж один універсальний з купою непотрібних методів.

    D - Dependency Inversion Principle

    Залежати потрібно від абстракцій, а не від конкретних реалізацій.
    Тобто використовуємо інтерфейси, а не жорсткі прив’язки до класів.

2. **SRP (Single Responsibility Principle).**  
    Клас повинен виконувати тільки одну логічну задачу.
    Чим менше відповідальностей у класу - тим легше змінювати код.

   ```python
    # Погана реалізація, різні задачі виконує один клас
    class Order:
        def calculate_total(self):
            pass
        def save_to_db(self):
            pass
        def send_email(self):
            pass
    
    # SRP
    class Order:
        def calculate_total(self):
            print("Calculating total")

    class OrderSaving:
        def save(self, order):
            print("Saving order to database")

    class EmailSend:
        def send(self, order):
            print("Sending email about order")
   ```

3. **OCP (Open/Closed Principle).**  
    Код має бути відкритий для розширення, але закритий для змін.

   ```python
    # Погана реалізація, якщо хочемо додати нову форму платежу, треба міняти код.
    class PaymentProcessor:
        def pay(self, payment_type):
            if payment_type == "card":
                print("Paying by card")
            elif payment_type == "applepay":
                print("Paying by ApplePay")

    # OCP
    class PaymentMethod:
        def pay(self):
            pass

    class CardPayment(PaymentMethod):
        def pay(self):
            print("Paying by card")

    class ApplePayPayment(PaymentMethod):
        def pay(self):
            print("Paying by ApplePay")

    class PaymentProcessor:
        def process(self, method: PaymentMethod):
            method.pay()
    
    # Тепер щоб додати новий метод робимо віддільний клас не змінюючи основний код
    class GooglePayPayment(PaymentMethod):
        def pay(self):
            print("Paying by GooglePay")

   ```

5. **Запустив програму.**  
   ```

    Calculating total
    Saving order to database
    Sending email about order

    Paying by card
    Paying by ApplePay
    Paying by GooglePay


   ```

---

## **Висновки**

Принципи SOLID допомагають створювати зрозумілий, гнучкий і легкий у підтримці код.
Вони зменшують залежності між класами, спрощують розширення функціоналу та покращують структуру програм.
Практичні приклади показали, що застосування SOLID робить систему більш надійною та зручною для подальшого розвитку.