class Coffee {
    make () {
        return "La esspresso maciatto porfavore"
    }
}

function sugarDecorator (coffe) {
    const mainMake = coffe.make
     coffe.make = function () {
      const result = mainMake.apply(this)
       return result + " + sugarUUUUHH"
     }
    return coffe
}

let myCoffee = new Coffee()
console.log(myCoffee.make)

myCoffee = sugarDecorator(myCoffee);
console.log(myCoffee.make());