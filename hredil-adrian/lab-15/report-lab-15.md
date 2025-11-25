# МІНІСТЕРСТВО ОСВІТИ ТА НАУКИ

## Львівський національний університет ветеринарії і біотехнологій імені С.З.Ґжицького

# Звіт

**про виконання лаборатоної роботи №15**

**з дисципліни "Об'єктно-орієнтоване програмування"**

**на тему** 

**Структурний патерн Decorator **

Виконав: студент групи КН-21 Греділь Адріан

Перевірив: ст. викладач Назар Заплатинський

### Львів 2025




## Хід роботи

### У роботі було розглянуто два варіанти реалізації класів Car та SportCar. Перший варіант містив типові помилки проєктування, недоліки структури та порушення принципів ООП. Другий варіант — відрефакторований, з виправленими недоліками та покращеною архітектурою. Нижче наведено детальний аналіз відмінностей між цими реалізаціями.


## Need refactoring
```js 

class Car {
    constructor(model, speed) {
        this.model = model
        this.speed = speed || 0
        this.type = "car"
    }

    drive() {
        console.log(this.model + " driving at " + this.speed)
    }
}

class SportCar extends Car {
    constructor(model, speed, turbo) {
        super(model, speed)
        this.turbo = turbo
        this.type = "car" 
    }

    drive() {
        console.log("SPORT: " + this.model + " driving at " + this.speed)
        if (this.turbo) console.log("Turbo ON")
    }
}

const c = new Car("BMW")
c.drive()

const s = new SportCar("Ferrari", -200, true)
s.drive()

    
```

## Refactored

```js
class Car {
    constructor(model, speed = 0) {
        this.model = model
        this._speed = speed
        this.type = "car"
    }

    drive() {
        console.log(`${this.model} driving at ${this._speed} km/h`)
    }

    set speed(value) {
        if (value < 0) throw new Error("Speed cannot be negative")
        this._speed = value
    }

    get speed() {
        return this._speed
    }
}

class SportCar extends Car {
    constructor(model, speed = 0, turbo = false) {
        super(model, speed)
        this.turbo = turbo
        this.type = "sportcar"
    }

    drive() {
        super.drive()
        if (this.turbo) {
            console.log("Turbo BOOST activated!")
        }
    }
}

const car = new Car("BMW")
car.drive()

const sport = new SportCar("Ferrari", -222, true)
sport.drive()

```

## Висновок:

 ### У ході виконання роботи було проаналізовано вихідний варіант ООП-коду та проведено його рефакторинг. Початкова реалізація містила низку типових недоліків: дублювання логіки, відсутність інкапсуляції, некоректне наслідування та відсутність валідації даних. Після рефакторингу код став більш структурованим і відповідним принципам об’єктно-орієнтованого програмування.