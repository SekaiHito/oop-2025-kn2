//O — Open/Closed Principle (Принцип відкритості/закритості)

// Клас порушує принцип Open/Closed,
// бо кожен новий тип знижки вимагає змін у цьому методі

class DiscountService {
  calculate(price, customerType) {
    if (customerType === "regular") {
      return price;
    } else if (customerType === "vip") {
      return price * 0.9;
    } else if (customerType === "student") {
      return price * 0.85;
    } else {
      throw new Error("Невідомий тип клієнта");
    }
  }
}

// --- Використання ---
const service = new DiscountService();

console.log("Звичайний клієнт:", service.calculate(1000, "regular"));
console.log("VIP клієнт:", service.calculate(1000, "vip"));
console.log("Студент:", service.calculate(1000, "student"));

// =======================================================================================================

// Кожен тип знижки реалізує власну логіку.
// Ми просто додаємо новий клас без зміни існуючого коду.

class RegularDiscount {
  getDiscount(price) {
    return price;
  }
}

class VipDiscount {
  getDiscount(price) {
    return price * 0.9;
  }
}

class StudentDiscount {
  getDiscount(price) {
    return price * 0.85;
  }
}

// Клас DiscountService відкритий для розширення, але закритий для змін.
// Він працює з будь-яким типом знижки, що має метод getDiscount().
class DiscountService {
  constructor(discountStrategy) {
    this.discountStrategy = discountStrategy;
  }

  calculate(price) {
    return this.discountStrategy.getDiscount(price);
  }
}

// --- Використання ---
const vipDiscount = new VipDiscount();
const studentDiscount = new StudentDiscount();

const vipOrder = new DiscountService(vipDiscount);
const studentOrder = new DiscountService(studentDiscount);

console.log("Ціна для VIP:", vipOrder.calculate(1000));
console.log("Ціна для студента:", studentOrder.calculate(1000));

// Додаємо новий тип без змін старого коду
class NewUserDiscount {
  getDiscount(price) {
    return price * 0.95;
  }
}

const newUserOrder = new DiscountService(new NewUserDiscount());
console.log("Ціна для нового користувача:", newUserOrder.calculate(1000));
