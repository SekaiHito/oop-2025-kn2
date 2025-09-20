class NewsAgency {
    constructor() {
        this.observers = [];
        this.news = "";
    }

    addObserver(observer) {
        this.observers.push(observer);
        console.log(`Додано спостерігача: ${observer.name}`);
    }

    removeObserver(observer) {
        this.observers = this.observers.filter(obs => obs !== observer);
        console.log(`Видалено спостерігача: ${observer.name}`);
    }

    notifyObservers() {
        console.log(`\nРозсилка новин до ${this.observers.length} спостерігачів:`);
        this.observers.forEach(observer => observer.update(this.news));
    }

    setNews(news) {
        this.news = news;
        console.log(`\nАгентство новин отримало: "${news}"`);
        this.notifyObservers();
    }
}

class NewsChannel {
    constructor(name) {
        this.name = name;
        this.receivedNews = [];
    }

    update(news) {
        this.receivedNews.push(news);
        console.log(`${this.name}: "${news}"`);
    }

    getNewsCount() {
        return this.receivedNews.length;
    }
}

function demonstrateObserver() {
    console.log("=== Демонстрація шаблону Observer ===\n");

    // Створюємо агентство новин
    const agency = new NewsAgency();

    // Створюємо спостерігачів
    const cnn = new NewsChannel("CNN");
    const bbc = new NewsChannel("BBC");

    // Додаємо спостерігачів
    agency.addObserver(cnn);
    agency.addObserver(bbc);

    // Розсилаємо новини
    agency.setNews("Важливі новини: відкриття нового технологічного центру");
    agency.setNews("Спорт: фінал чемпіонату світу з футболу");

    // Видаляємо одного спостерігача
    agency.removeObserver(bbc);

    // Розсилаємо ще одну новину
    agency.setNews("Економіка: зростання ВВП на 3%");

    // Показуємо статистику
    console.log("\n📊 Статистика отриманих новин:");
    console.log(`CNN отримав ${cnn.getNewsCount()} новин`);
    console.log(`BBC отримав ${bbc.getNewsCount()} новин`);
}

// Запуск демонстрації
demonstrateObserver();

console.log("\n=== Демонстрація завершена ===");
