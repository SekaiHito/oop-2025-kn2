from abc import ABC, abstractmethod

class SortingStrategy(ABC):
    """Інтерфейс для всіх стратегій сортування."""
    @abstractmethod
    def sort(self, data):
        pass

class BubbleSortStrategy(SortingStrategy):
    """Конкретна стратегія: Сортування бульбашкою."""
    def sort(self, data):
        n = len(data)
        for i in range(n):
            for j in range(0, n - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
        print("Сортування бульбашкою:", data)
        return data

class QuickSortStrategy(SortingStrategy):
    """Конкретна стратегія: Швидке сортування."""
    def sort(self, data):
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        
        sorted_data = self.sort(left) + middle + self.sort(right)
        print("Швидке сортування:", sorted_data)
        return sorted_data

class Sorter:
    """Контекст: Використовує обрану стратегію."""
    def __init__(self, strategy: SortingStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: SortingStrategy):
        """Дозволяє змінити стратегію під час виконання."""
        self._strategy = strategy

    def execute_sort(self, data):
        """Делегує виконання обраній стратегії."""
        return self._strategy.sort(data)

data_set = [5, 1, 4, 2, 8]
print(f"Початковий масив: {data_set}")

bubble_sorter = Sorter(BubbleSortStrategy())
bubble_sorter.execute_sort(list(data_set)) 

quick_sorter = Sorter(QuickSortStrategy())
quick_sorter.execute_sort(list(data_set)) 

advanced_sorter = Sorter(QuickSortStrategy())
print("\nПочаткова стратегія: QuickSort")
advanced_sorter.execute_sort(list(data_set))

advanced_sorter.set_strategy(BubbleSortStrategy())
print("Зміна стратегії на: BubbleSort")
advanced_sorter.execute_sort(list(data_set))