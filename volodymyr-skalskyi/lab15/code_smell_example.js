console.log("=== CODE SMELL: ДУЖЕ ДОВГА ФУНКЦІЯ ===\n");

// БРУДНИЙ КОД - одна велика функція з усіма діями
function registerUserBad(name, email) {
    // Валідація email
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        throw new Error("Невірний формат email");
    }

    // Валідація імені
    if (!name || name.trim().length === 0) {
        throw new Error("Ім'я не може бути порожнім");
    }
    if (name.length < 2) {
        throw new Error("Ім'я занадто коротке");
    }

    // Збереження в БД
    console.log(`Збереження користувача ${name} в БД...`);
    const userId = Math.floor(Math.random() * 10000);
    console.log(`Користувач збережено з ID: ${userId}`);

    // Відправка email
    console.log(`Відправка привітального email на ${email}...`);
    console.log(`Email відправлено!`);

    // Логування
    console.log(`[LOG] Користувач ${userId} зареєстровано. Email: ${email}`);

    // Створення профілю
    console.log(`Створення профілю для користувача ${name}...`);
    console.log(`Профіль створено!`);

    return userId;
}

console.log("Брудний код:");
try {
    registerUserBad("Іван Петренко", "ivan@example.com");
} catch (error) {
    console.log(`Помилка: ${error.message}`);
}

console.log("\n=== ЧИСТИЙ КОД: РОЗДІЛЕННЯ НА ЧАСТИНИ ТА ВИНЕСЕННЯ КОНСТАНТ ===\n");

// КОНСТАНТИ
const EMAIL_REGEX = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
const MIN_NAME_LENGTH = 2;
const ERROR_MESSAGES = {
    INVALID_EMAIL: "Невірний формат email",
    EMPTY_NAME: "Ім'я не може бути порожнім",
    SHORT_NAME: "Ім'я занадто коротке"
};

// Валідація email
function validateEmail(email) {
    if (!EMAIL_REGEX.test(email)) {
        throw new Error(ERROR_MESSAGES.INVALID_EMAIL);
    }
}

// Валідація імені
function validateName(name) {
    if (!name || name.trim().length === 0) {
        throw new Error(ERROR_MESSAGES.EMPTY_NAME);
    }
    if (name.length < MIN_NAME_LENGTH) {
        throw new Error(ERROR_MESSAGES.SHORT_NAME);
    }
}

// Збереження користувача
function saveUser(name) {
    console.log(`Збереження користувача ${name} в БД...`);
    const userId = Math.floor(Math.random() * 10000);
    console.log(`Користувач збережено з ID: ${userId}`);
    return userId;
}

// Відправка email
function sendWelcomeEmail(email) {
    console.log(`Відправка привітального email на ${email}...`);
    console.log(`Email відправлено!`);
}

// Логування
function logUserRegistration(userId, email) {
    console.log(`[LOG] Користувач ${userId} зареєстровано. Email: ${email}`);
}

// Створення профілю
function createProfile(name) {
    console.log(`Створення профілю для користувача ${name}...`);
    console.log(`Профіль створено!`);
}

// Головна функція реєстрації
function registerUser(name, email) {
    // Валідація
    validateEmail(email);
    validateName(name);

    // Збереження
    const userId = saveUser(name);

    // Відправка email
    sendWelcomeEmail(email);

    // Логування
    logUserRegistration(userId, email);

    // Створення профілю
    createProfile(name);

    return userId;
}

console.log("Чистий код:");
try {
    registerUser("Іван Петренко", "ivan@example.com");
} catch (error) {
    console.log(`Помилка: ${error.message}`);
}

