class Apparel {
  cost() {
    return 100;
  }

  description() {
    return "Basic Black T-Shirt";
  }
}

class ApparelDecorator {
  constructor(apparel) {
    this.apparel = apparel;
  }

  cost() {
    return this.apparel.cost();
  }

  description() {
    return this.apparel.description();
  }
}

class PackagingDecorator extends ApparelDecorator {
  cost() {
    return super.cost() + 5;
  }

  description() {
    return super.description() + ", packaging";
  }
}

class DiscountDecorator extends ApparelDecorator {
  constructor(apparel, percent) {
    super(apparel);
    this.percent = percent;
  }

  cost() {
    const basicCost = super.cost();
    return basicCost * (this.percent / 100);
  }
  description() {
    return super.description() + `, discount ${this.percent}%`;
  }
}

// ----Використання----

let apparel = new Apparel();
console.log(apparel.cost(), apparel.description());

apparel = new PackagingDecorator(apparel);
console.log(apparel.cost(), apparel.description());

apparel = new DiscountDecorator(apparel, 20);
console.log(apparel.cost(), apparel.description());
