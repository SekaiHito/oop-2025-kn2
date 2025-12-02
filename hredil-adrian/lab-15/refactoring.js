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
