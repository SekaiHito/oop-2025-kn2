from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional

# --- Mediator Interface ---
class Mediator(ABC):
    """
    Інтерфейс Посередника.
    Оголошує метод, який використовують компоненти для сповіщення про різні події.
    Посередник може реагувати на ці події та передавати виконання іншим компонентам.
    """
    @abstractmethod
    def notify(self, sender: object, event: str) -> None:
        pass


# --- Base Component ---
class BaseComponent:
    """
    Базовий компонент.
    Забезпечує базову функціональність зберігання посилання на екземпляр Посередника.
    """
    def __init__(self, mediator: Optional[Mediator] = None) -> None:
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator


# --- Concrete Components ---
class Component1(BaseComponent):
    """
    Конкретний компонент 1.
    Реалізує бізнес-логіку та повідомляє медіатора про свої дії.
    Він НЕ знає про існування Component2.
    """
    def do_a(self) -> None:
        print("🔹 Component 1 виконує дію A.")
        # Компонент просто каже: "Я зробив А". Йому байдуже, хто і як на це відреагує.
        if self.mediator:
            self.mediator.notify(self, "A")

    def do_b(self) -> None:
        print("🔹 Component 1 виконує дію B.")


class Component2(BaseComponent):
    """
    Конкретний компонент 2.
    """
    def do_c(self) -> None:
        print("🔸 Component 2 виконує дію C.")

    def do_d(self) -> None:
        print("🔸 Component 2 виконує дію D.")
        if self.mediator:
            self.mediator.notify(self, "D")


# --- Concrete Mediator ---
class ConcreteMediator(Mediator):
    """
    Конкретний Посередник.
    Координує взаємодію між кількома компонентами.
    Тут зосереджена логіка керування потоком (Control Flow).
    """
    def __init__(self, component1: Component1, component2: Component2) -> None:
        self._component1 = component1
        self._component1.mediator = self
        
        self._component2 = component2
        self._component2.mediator = self

    def notify(self, sender: object, event: str) -> None:
        if event == "A":
            print("📣 Медіатор реагує на 'A' -> запускає Component 2:")
            self._component2.do_c()
            
        elif event == "D":
            print("📣 Медіатор реагує на 'D' -> запускає ланцюжок дій:")
            self._component1.do_b()
            self._component2.do_c()


# --- Client Code ---
if __name__ == "__main__":
    # Створення компонентів
    c1 = Component1()
    c2 = Component2()
    
    # Ініціалізація медіатора (зв'язуємо компоненти)
    mediator = ConcreteMediator(c1, c2)

    print("--- Клієнт ініціює операцію A ---")
    c1.do_a()

    print("\n--- Клієнт ініціює операцію D ---")
    c2.do_d()