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
