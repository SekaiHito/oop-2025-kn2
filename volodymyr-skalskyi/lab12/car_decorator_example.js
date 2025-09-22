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

function demonstrateCarDecorator() {
    console.log("=== Демонстрація шаблону Decorator з автомобілем ===\n");

    // Базовий автомобіль
    console.log("1. Базовий автомобіль:");
    let myCar = new Car();
    console.log(myCar.getInfo() + "\n");

    // Автомобіль з кондиціонером
    console.log("2. Автомобіль з кондиціонером:");
    myCar = airConditioningDecorator(new Car());
    console.log(myCar.getInfo() + "\n");

    // Автомобіль з кондиціонером та шкіряними сидіннями
    console.log("3. Автомобіль з кондиціонером та шкіряними сидіннями:");
    myCar = leatherSeatsDecorator(airConditioningDecorator(new Car()));
    console.log(myCar.getInfo() + "\n");

    // Динамічне додавання опцій
    console.log("4. Динамічне додавання опцій:");
    let dynamicCar = new Car();
    console.log(`Початковий: ${dynamicCar.getDescription()} - $${dynamicCar.getPrice()}`);

    dynamicCar = airConditioningDecorator(dynamicCar);
    console.log(`+ кондиціонер: ${dynamicCar.getDescription()} - $${dynamicCar.getPrice()}`);

    dynamicCar = leatherSeatsDecorator(dynamicCar);
    console.log(`+ шкіряні сидіння: ${dynamicCar.getDescription()} - $${dynamicCar.getPrice()}`);
}

// Запуск демонстрації
demonstrateCarDecorator();

console.log("\n=== Демонстрація завершена ===");