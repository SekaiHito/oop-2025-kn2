# МІНІСТЕРСТВО ОСВІТИ ТА НАУКИ

## Львівський національний університет ветеринарії і біотехнологій імені С.З.Ґжицького

# Звіт

**про виконання лаборатоної роботи №12**

**з дисципліни "Об'єктно-орієнтоване програмування"**

**на тему**

**Структурні шаблони проєктування (Decorator)**

Виконав: студент групи КН-31 Скальський Володимир

Перевірив: ст. викладач Назар Заплатинський

### Львів 2025

**Мета роботи - Познайомитися з групою структурних шаблонів проєктування та реалізувати шаблон Decorator**

## Хід роботи

### Структурні шаблони - це шаблони проєктування, які стосуються композиції класів та об'єктів. Вони допомагають формувати структуру програми, використовуючи наслідування та композицію для створення більш складних об'єктів.

### Decorator - це структурний шаблон, який дозволяє динамічно додавати нову функціональність до об'єктів, не змінюючи їх структуру. Він обгортає об'єкт у обгортку, яка надає додаткові можливості.

### Приклад реалізації шаблону Decorator для автомобіля:

```javascript
// Базовий клас автомобіля
class Car {
  constructor() {
    this.basePrice = 20000;
    this.features = ["Базове обладнання"];
  }

  getDescription() {
    return this.features.join(", ");
  }

  getPrice() {
    return this.basePrice;
  }
}

// Базовий клас декоратора
class CarDecorator {
  constructor(car) {
    this.car = car;
  }

  getDescription() {
    return this.car.getDescription();
  }

  getPrice() {
    return this.car.getPrice();
  }
}

// Декоратор кондиціонера
class AirConditioningDecorator extends CarDecorator {
  getDescription() {
    return this.car.getDescription() + ", Кондиціонер";
  }

  getPrice() {
    return this.car.getPrice() + 1500;
  }
}

// Декоратор шкіряних сидінь
class LeatherSeatsDecorator extends CarDecorator {
  getDescription() {
    return this.car.getDescription() + ", Шкіряні сидіння";
  }

  getPrice() {
    return this.car.getPrice() + 2000;
  }
}

// Використання
let myCar = new Car();
console.log(myCar.getDescription()); // "Базове обладнання"

myCar = new AirConditioningDecorator(myCar);
console.log(myCar.getDescription()); // "Базове обладнання, Кондиціонер"

myCar = new LeatherSeatsDecorator(myCar);
console.log(myCar.getDescription()); // "Базове обладнання, Кондиціонер, Шкіряні сидіння"
```

### Запуск прикладу:

```bash
node car_decorator_example.js
```

## Висновок:

### В ході виконання лабораторної роботи було реалізовано шаблон Decorator, який дозволяє динамічно додавати нову функціональність до об'єктів без зміни їх основної структури. Шаблон особливо корисний для розширення функціональності об'єктів у процесі виконання програми.
