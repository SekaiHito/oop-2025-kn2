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

    getInfo() {
        return `Автомобіль: ${this.getDescription()}\nЦіна: $${this.getPrice()}`;
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

    getInfo() {
        return `Автомобіль: ${this.getDescription()}\nЦіна: $${this.getPrice()}`;
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

function demonstrateCarDecorator() {
    console.log("=== Демонстрація шаблону Decorator з автомобілем ===\n");

    // Базовий автомобіль
    console.log("1. Базовий автомобіль:");
    let myCar = new Car();
    console.log(myCar.getInfo() + "\n");

    // Автомобіль з кондиціонером
    console.log("2. Автомобіль з кондиціонером:");
    myCar = new AirConditioningDecorator(new Car());
    console.log(myCar.getInfo() + "\n");

    // Автомобіль з кондиціонером та шкіряними сидіннями
    console.log("3. Автомобіль з кондиціонером та шкіряними сидіннями:");
    myCar = new LeatherSeatsDecorator(new AirConditioningDecorator(new Car()));
    console.log(myCar.getInfo() + "\n");

    // Динамічне додавання опцій
    console.log("4. Динамічне додавання опцій:");
    let dynamicCar = new Car();
    console.log(`Початковий: ${dynamicCar.getDescription()} - $${dynamicCar.getPrice()}`);

    dynamicCar = new AirConditioningDecorator(dynamicCar);
    console.log(`+ кондиціонер: ${dynamicCar.getDescription()} - $${dynamicCar.getPrice()}`);

    dynamicCar = new LeatherSeatsDecorator(dynamicCar);
    console.log(`+ шкіряні сидіння: ${dynamicCar.getDescription()} - $${dynamicCar.getPrice()}`);
}

// Запуск демонстрації
demonstrateCarDecorator();

console.log("\n=== Демонстрація завершена ===");