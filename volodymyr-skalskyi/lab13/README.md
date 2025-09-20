# МІНІСТЕРСТВО ОСВІТИ ТА НАУКИ

## Львівський національний університет ветеринарії і біотехнологій імені С.З.Ґжицького

# Звіт

**про виконання лаборатоної роботи №13**

**з дисципліни "Об'єктно-орієнтоване програмування"**

**на тему**

**Поведінкові шаблони проєктування (Observer)**

Виконав: студент групи КН-31 Скальський Володимир

Перевірив: ст. викладач Назар Заплатинський

### Львів 2025

**Мета роботи - Познайомитися з групою поведінкових шаблонів проєктування та реалізувати шаблон Observer**

## Хід роботи

### Поведінкові шаблони - це шаблони проєктування, які стосуються алгоритмів та розподілу відповідальностей між об'єктами. Вони описують не тільки структуру об'єктів, але й паттерни їх взаємодії.

### Observer - це поведінковий шаблон, який визначає залежність "один до багатьох" між об'єктами. Коли один об'єкт змінює свій стан, всі залежні об'єкти автоматично отримують сповіщення та оновлюються.

### Приклад реалізації шаблону Observer для системи новин:

```javascript
class NewsAgency {
  constructor() {
    this.observers = [];
    this.news = "";
  }

  addObserver(observer) {
    this.observers.push(observer);
  }

  removeObserver(observer) {
    this.observers = this.observers.filter((obs) => obs !== observer);
  }

  notifyObservers() {
    this.observers.forEach((observer) => observer.update(this.news));
  }

  setNews(news) {
    this.news = news;
    this.notifyObservers();
  }
}

class NewsChannel {
  constructor(name) {
    this.name = name;
  }

  update(news) {
    console.log(`${this.name}: ${news}`);
  }
}

// Використання
const agency = new NewsAgency();
const cnn = new NewsChannel("CNN");
const bbc = new NewsChannel("BBC");

agency.addObserver(cnn);
agency.addObserver(bbc);

agency.setNews("Важливі новини!");
```

### Запуск прикладу:

```bash
node observer_example.js
```

## Висновок:

### В ході виконання лабораторної роботи було реалізовано шаблон Observer, який забезпечує слабке зв'язування між об'єктами та дозволяє автоматично сповіщати залежні об'єкти про зміни стану. Шаблон особливо корисний для реалізації систем подій та сповіщень.
