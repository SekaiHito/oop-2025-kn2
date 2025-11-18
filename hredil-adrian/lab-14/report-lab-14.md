# МІНІСТЕРСТВО ОСВІТИ ТА НАУКИ

## Львівський національний університет ветеринарії і біотехнологій імені С.З.Ґжицького

# Звіт

**про виконання лаборатоної роботи №14**

**з дисципліни "Об'єктно-орієнтоване програмування"**

**на тему** 

**Структурний патерн Decorator **

Виконав: студент групи КН-21 Греділь Адріан

Перевірив: ст. викладач Назар Заплатинський

### Львів 2025

**Мета роботи - познайомитися з SOLID**


## Хід роботи

### Нижче є 2 приклади використання першого принципу SOLID(single responsability), в неправильному, всі дії відбуваються безпосередньо у одному класі, а саме валідація, розсилка, збереження у базу даних, а у дрогому у кожного класу є своя конкретна відповідальність, тобто всі дії виконуютсья окремо у кожному класі, це дозволяє мені уникнути певних проблем, а саме,  проблеми з тестуванням, якщо щось міняю у мене нее все ламається.


### Правельний варіант, де кожен клас має свою конкретну відповідальність

```js 

class UserValidator {
  static validate(data) {
    if (!data.email.includes("@")) {
      throw new Error("Invalid email");
    }
  }
}

class UserRepository {
  save(data) {
    console.log("Saving user to DB:", data);
  }
}

class EmailService {
  send(email) {
    console.log("Sending email to:", email);
  }
}

class UserService {
  constructor(repository, emailService) {
    this.repository = repository;
    this.emailService = emailService;
  }

  createUser(data) {
    UserValidator.validate(data);
    this.repository.save(data);
    this.emailService.send(data.email);
  }
}

const repo = new UserRepository();
const mailer = new EmailService();
const userService = new UserService(repo, mailer);

userService.createUser({ email: "test@gmail.com" });

```
### Не правильний варіант де в одному класі виконуються всі маніпуляції
```js
class UserService {
  createUser(data) {
    if (!data.email.includes("@")) {
      throw new Error("Invalid email");
    }
    console.log("Saving user to DB:", data);
    console.log("Sending email to:", data.email);
  }
}
const service = new UserService();
service.createUser({ email: "test@gmail.com" });

```

## Висновок:

### Виконучи лабораторну роботу я попрацював з принципами проектування  SOLID, ці знання піддались практичному використанню, а саме, було створено демо-апп з використанням першого принципу(принцип одиночної відповідальность).