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

function airConditioningDecorator(car) {
  const originalGetDescription = car.getDescription;
  const originalGetPrice = car.getPrice;

  car.getDescription = function () {
    return originalGetDescription.call(this) + ", Кондиціонер";
  };

  car.getPrice = function () {
    return originalGetPrice.call(this) + 1500;
  };

  return car;
}

function leatherSeatsDecorator(car) {
  const originalGetDescription = car.getDescription;
  const originalGetPrice = car.getPrice;

  car.getDescription = function () {
    return originalGetDescription.call(this) + ", Шкіряні сидіння";
  };

  car.getPrice = function () {
    return originalGetPrice.call(this) + 2000;
  };

  return car;
}

// Використання
let myCar = new Car();
console.log(myCar.getDescription()); // "Базове обладнання"

myCar = airConditioningDecorator(myCar);
console.log(myCar.getDescription()); // "Базове обладнання, Кондиціонер"

myCar = leatherSeatsDecorator(myCar);
console.log(myCar.getDescription()); // "Базове обладнання, Кондиціонер, Шкіряні сидіння"
```

### Запуск прикладу:

```bash
node car_decorator_example.js
```

## Висновок:

### В ході виконання лабораторної роботи було реалізовано шаблон Decorator, який дозволяє динамічно додавати нову функціональність до об'єктів без зміни їх основної структури. Шаблон особливо корисний для розширення функціональності об'єктів у процесі виконання програми.
