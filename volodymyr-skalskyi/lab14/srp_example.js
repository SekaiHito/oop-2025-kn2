console.log("=== ПОРУШЕННЯ SRP ===\n");

class UserBad {
    constructor(name, email) {
        this.name = name;
        this.email = email;
    }

    validateEmail() {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(this.email)) {
            throw new Error("Невірний формат email");
        }
    }

    saveToDatabase() {
        console.log(`Збереження користувача ${this.name} в БД`);
    }

    sendWelcomeEmail() {
        console.log(`Відправка email на ${this.email}`);
    }
}

const badUser = new UserBad("Іван Петренко", "ivan@example.com");
badUser.validateEmail();
badUser.saveToDatabase();
badUser.sendWelcomeEmail();

console.log("\n=== ДОТРИМАННЯ SRP ===\n");

class User {
    constructor(name, email) {
        this.name = name;
        this.email = email;
    }
}

class EmailValidator {
    static validate(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            throw new Error("Невірний формат email");
        }
    }
}

class UserRepository {
    static save(user) {
        console.log(`Збереження користувача ${user.name} в БД`);
    }
}

class EmailService {
    static sendWelcomeEmail(user) {
        console.log(`Відправка email на ${user.email}`);
    }
}

const user = new User("Іван Петренко", "ivan@example.com");
EmailValidator.validate(user.email);
UserRepository.save(user);
EmailService.sendWelcomeEmail(user);
