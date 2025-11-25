from __future__ import annotations
from typing import Protocol, Any, TypedDict

# --- Target Interface ---
class PaymentProcessor(Protocol):
    """
    Target (Цільовий інтерфейс).
    Описує інтерфейс, який очікує наш сучасний клієнтський код.
    """
    def pay(self, amount: float) -> bool:
        """Виконує платіж на суму (у звичайних одиницях, наприклад, 10.50)."""
        ...

# --- Adaptee (Legacy Code) ---
class LegacyGateway:
    """
    Adaptee (Адаптований клас).
    Стара платіжна система. Вона не сумісна з новим кодом, бо:
    1. Приймає суму в копійках/центах (int), а не в валюті (float).
    2. Повертає словник, а не булеве значення.
    """
    def make_payment(self, currency: str, cents: int) -> dict[str, Any]:
        print(f"🔌 [Legacy System] Processing transaction: {cents} cents ({currency})")
        
        if cents <= 0:
            return {'status': 'error', 'message': 'Invalid amount'}
        
        # Імітація успішної транзакції
        return {'status': 'ok', 'tx_id': 'LEGACY_TX_999'}

# --- Adapter via Composition (Object Adapter) ---
class LegacyGatewayAdapter:
    """
    Adapter (Об'єктний адаптер).
    Використовує композицію: зберігає посилання на об'єкт старої системи
    і трансформує виклики. Це найбільш рекомендований підхід.
    """
    def __init__(self, gateway: LegacyGateway, currency: str = 'USD') -> None:
        self._gateway = gateway
        self._currency = currency

    def pay(self, amount: float) -> bool:
        # Адаптація даних: конвертуємо float (долари) в int (центи)
        cents = int(round(amount * 100))
        
        # Делегування виклику старій системі
        result = self._gateway.make_payment(self._currency, cents)
        
        # Адаптація відповіді: перетворюємо словник у bool
        return result.get('status') == 'ok'

# --- Adapter via Inheritance (Class Adapter) ---
class ClassAdapter(LegacyGateway, PaymentProcessor):
    """
    Class Adapter (Адаптер класу).
    Використовує множинне успадкування.
    Одночасно є і 'LegacyGateway' і 'PaymentProcessor'.
    Менш гнучкий, але іноді використовується.
    """
    def pay(self, amount: float) -> bool:
        # Тут ми звертаємось до методу make_payment через self, бо ми його успадкували
        cents = int(round(amount * 100))
        result = self.make_payment('USD', cents) 
        return result.get('status') == 'ok'

# --- Client Code ---
def client_code(processor: PaymentProcessor, amount: float) -> None:
    """
    Клієнтський код працює лише з типом PaymentProcessor.
    Він не знає про існування LegacyGateway.
    """
    print(f"\n💳 Спроба оплати: {amount:.2f}...")
    
    success = processor.pay(amount)
    
    if success:
        print(f"✅ Успіх: Платіж на суму {amount:.2f} проведено.")
    else:
        print(f"❌ Помилка: Платіж на суму {amount:.2f} відхилено.")

if __name__ == "__main__":
    # 1. Використання Object Adapter (Рекомендовано)
    print("--- Сценарій 1: Object Adapter ---")
    legacy_system = LegacyGateway()
    # "Обгортаємо" стару систему в адаптер
    adapter = LegacyGatewayAdapter(legacy_system, currency='EUR')
    
    client_code(adapter, 12.34)

    # 2. Використання Class Adapter
    print("\n--- Сценарій 2: Class Adapter ---")
    # Створюємо гібридний об'єкт
    class_adapter = ClassAdapter()
    
    # Тест з помилкою (сума 0)
    client_code(class_adapter, 0)