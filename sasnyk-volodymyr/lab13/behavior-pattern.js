class NewAgancy {
  constructor() {
    this.subscribers = [];
  }

  subscribe(observer) {
    this.subscribers.push(observer);
  }

  unsubscribe(observer) {
    this.subscribers = this.subscribers.filter((sub) => sub !== observer);
  }

  notify(news) {
    this.subscribers.forEach((sub) => sub.update(news));
  }
}

class User {
  constructor(name) {
    this.name = name;
  }

  update(news) {
    console.log(`${this.name} отримав новину: "${news}"`);
  }
}

//-----Використання------

const agency = new NewAgancy();

const user1 = new User("Іван");
const user2 = new User("Марія");
const user3 = new User("Олег");

agency.subscribe(user1);
agency.subscribe(user2);
agency.subscribe(user3);

agency.notify("Сьогодні знижки до 50%!");

// Виведе:
// Іван отримав новину: "Сьогодні знижки до 50%!"
// Марія отримав новину: "Сьогодні знижки до 50%!"
// Олег отримав новину: "Сьогодні знижки до 50%!"

agency.unsubscribe(user2);

agency.notify("Завтра нова колекція!");

// Іван отримав новину: "Завтра нова колекція!"
// Олег отримав новину: "Завтра нова колекція!"

//Бонус ----Memento---

// --- Memento: знімок стану ---
class TextMemento {
  constructor(content) {
    this.content = content;
  }

  getContent() {
    return this.content;
  }
}

// --- Originator: об'єкт, який створює знімки ---
class TextEditor {
  constructor() {
    this.content = "";
  }

  type(words) {
    this.content += words;
  }

  getContent() {
    return this.content;
  }

  save() {
    return new TextMemento(this.content);
  }

  restore(memento) {
    this.content = memento.getContent();
  }
}

// --- Caretaker: зберігає історію станів ---
class History {
  constructor() {
    this.mementos = [];
  }

  push(memento) {
    this.mementos.push(memento);
  }

  pop() {
    return this.mementos.pop();
  }
}

// --- Використання ---
const editor = new TextEditor();
const history = new History();

editor.type("Hello ");
editor.type("world!");
history.push(editor.save()); // Зберігаємо стан

editor.type(" More text...");
console.log("Поточний текст:", editor.getContent());
// Поточний текст: Hello world! More text...

editor.restore(history.pop()); // Відновлюємо попередній стан
console.log("Після Undo:", editor.getContent());
// Після Undo: Hello world!
