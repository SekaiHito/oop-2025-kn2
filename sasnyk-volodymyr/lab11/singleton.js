class AppState {
  static instance;

  user = null;
  theme = "light";

  constructor() {
    if (AppState.instance) {
      throw new Error("Use AppState.getInstance() instead of new.");
    }
  }

  static getInstance() {
    if (!AppState.instance) {
      AppState.instance = new AppState();
    }
    return AppState.instance;
  }

  setUser(user) {
    this.user = user;
  }

  getUser() {
    return this.user;
  }

  setTheme(theme) {
    this.theme = theme;
  }

  getTheme() {
    return this.theme;
  }
}

// --- Використання ---
const state1 = AppState.getInstance();
state1.setUser({ id: "1", name: "Volodymyr" });
state1.setTheme("dark");

const state2 = AppState.getInstance();

console.log(state2.getUser()); // { id: '1', name: 'Volodymyr' }
console.log(state2.getTheme()); // "dark"
console.log(state1 === state2); // true — це один і той самий об'єкт
