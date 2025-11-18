class Logger {
    constructor() {
        this.initialized = false;
        this.logs = [];
        this.logLevel = "INFO";

        if (!this.initialized) {
            this.initialized = true;
            this.logs = [];
            this.logLevel = "INFO";
            console.log("Logger: Ініціалізація логера");
        }

        Logger.instance = this;
    }

    static getInstance() {
        if (!Logger.instance) {
            Logger.instance = new Logger();
        }
        return Logger.instance;
    }

    setLogLevel(level) {
        this.logLevel = level;
        this.log(`Рівень логування змінено на: ${level}`);
    }

    log(message) {
        const logEntry = `[${this.logLevel}] ${message}`;
        this.logs.push(logEntry);
        console.log(`Logger: ${logEntry}`);
    }

    getLogs() {
        return [...this.logs];
    }

    clearLogs() {
        this.logs = [];
        this.log("Лог очищено");
    }

    getLogCount() {
        return this.logs.length;
    }

    getLogLevel() {
        return this.logLevel;
    }
}

function demonstrateSingleton() {
    console.log("=== Демонстрація шаблону Singleton ===\n");

    // Створюємо кілька "різних" екземплярів
    console.log("1. Створення екземплярів:");
    const logger1 = Logger.getInstance();
    const logger2 = Logger.getInstance();
    const logger3 = new Logger();

    // Перевіряємо, що це один і той же об'єкт
    console.log("\n2. Перевірка єдиності екземпляра:");
    console.log(`logger1 === logger2: ${logger1 === logger2}`);
    console.log(`logger1 === logger3: ${logger1 === logger3}`);
    console.log(`logger2 === logger3: ${logger2 === logger3}`);

    // Демонструємо роботу з логуванням
    console.log("\n3. Робота з логуванням:");
    logger1.log("Перше повідомлення");
    logger2.log("Друге повідомлення");
    logger3.log("Третє повідомлення");

    // Змінюємо рівень логування
    console.log("\n4. Зміна рівня логування:");
    logger1.setLogLevel("WARNING");
    logger2.log("Повідомлення після зміни рівня");

    // Показуємо всі логи
    console.log("\n5. Всі записи логу:");
    const logs = logger1.getLogs();
    logs.forEach((log, index) => {
        console.log(`  ${index + 1}. ${log}`);
    });

    // Показуємо кількість записів
    console.log(`\n6. Кількість записів у лозі: ${logger1.getLogCount()}`);

    // Очищаємо лог
    console.log("\n7. Очищення логу:");
    logger2.clearLogs();
    console.log(`Кількість записів після очищення: ${logger3.getLogCount()}`);
}

demonstrateSingleton();

console.log("\n=== Демонстрація завершена ===");
