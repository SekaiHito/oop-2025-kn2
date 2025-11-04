function registerUserBad(name, email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        throw new Error("Невірний формат email");
    }

    if (!name || name.trim().length === 0) {
        throw new Error("Ім'я не може бути порожнім");
    }
    if (name.length < 2) {
        throw new Error("Ім'я занадто коротке");
    }

    console.log(`Збереження користувача ${name} в БД...`);
    const userId = Math.floor(Math.random() * 10000);
    console.log(`Користувач збережено з ID: ${userId}`);

    console.log(`Відправка привітального email на ${email}...`);
    console.log(`Email відправлено!`);

    console.log(`[LOG] Користувач ${userId} зареєстровано. Email: ${email}`);

    console.log(`Створення профілю для користувача ${name}...`);
    console.log(`Профіль створено!`);

    return userId;
}

try {
    registerUserBad("Іван Петренко", "ivan@example.com");
} catch (error) {
    console.log(`Помилка: ${error.message}`);
}

const EMAIL_REGEX = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
const MIN_NAME_LENGTH = 2;
const ERROR_MESSAGES = {
    INVALID_EMAIL: "Невірний формат email",
    EMPTY_NAME: "Ім'я не може бути порожнім",
    SHORT_NAME: "Ім'я занадто коротке"
};

function validateEmail(email) {
    if (!EMAIL_REGEX.test(email)) {
        throw new Error(ERROR_MESSAGES.INVALID_EMAIL);
    }
}

function validateName(name) {
    if (!name || name.trim().length === 0) {
        throw new Error(ERROR_MESSAGES.EMPTY_NAME);
    }
    if (name.length < MIN_NAME_LENGTH) {
        throw new Error(ERROR_MESSAGES.SHORT_NAME);
    }
}

function saveUser(name) {
    console.log(`Збереження користувача ${name} в БД...`);
    const userId = Math.floor(Math.random() * 10000);
    console.log(`Користувач збережено з ID: ${userId}`);
    return userId;
}

function sendWelcomeEmail(email) {
    console.log(`Відправка привітального email на ${email}...`);
    console.log(`Email відправлено!`);
}

function logUserRegistration(userId, email) {
    console.log(`[LOG] Користувач ${userId} зареєстровано. Email: ${email}`);
}

function createProfile(name) {
    console.log(`Створення профілю для користувача ${name}...`);
    console.log(`Профіль створено!`);
}

function registerUser(name, email) {
    validateEmail(email);
    validateName(name);

    const userId = saveUser(name);

    sendWelcomeEmail(email);

    logUserRegistration(userId, email);

    createProfile(name);

    return userId;
}

try {
    registerUser("Іван Петренко", "ivan@example.com");
} catch (error) {
    console.log(`Помилка: ${error.message}`);
}

