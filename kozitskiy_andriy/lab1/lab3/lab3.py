from __future__ import annotations
from abc import ABC, abstractmethod

# Інтерфейс посередника
class Coordinator(ABC):
    @abstractmethod
    def handle(self, sender: object, action: str) -> None:
        pass

# Конкретний посередник
class SystemCoordinator(Coordinator):
    def __init__(self, part1: Part1, part2: Part2) -> None:
        self._part1 = part1
        self._part1.coordinator = self
        self._part2 = part2
        self._part2.coordinator = self

    def handle(self, sender: object, action: str) -> None:
        if action == "X":
            print("Coordinator responds to X and triggers subsequent actions:")
            self._part2.perform_c()
        elif action == "Y":
            print("Coordinator responds to Y and triggers subsequent actions:")
            self._part1.perform_b()
            self._part2.perform_c()

# Базовий компонент
class ComponentBase:
    def __init__(self, coordinator: Coordinator = None) -> None:
        self._coordinator = coordinator

    @property
    def coordinator(self) -> Coordinator:
        return self._coordinator

    @coordinator.setter
    def coordinator(self, coordinator: Coordinator) -> None:
        self._coordinator = coordinator

# Перший компонент
class Part1(ComponentBase):
    def perform_a(self) -> None:
        print("Part1 performs A.")
        self.coordinator.handle(self, "X")

    def perform_b(self) -> None:
        print("Part1 performs B.")

# Другий компонент
class Part2(ComponentBase):
    def perform_c(self) -> None:
        print("Part2 performs C.")

    def perform_d(self) -> None:
        print("Part2 performs D.")
        self.coordinator.handle(self, "Y")

# Клієнтський код
if __name__ == "__main__":
    p1 = Part1()
    p2 = Part2()
    system = SystemCoordinator(p1, p2)

    print("Client triggers action X.")
    p1.perform_a()

    print("\nClient triggers action Y.")
    p2.perform_d()
