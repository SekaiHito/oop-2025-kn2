from __future__ import annotations
from typing import Protocol


class PaymentInterface(Protocol):
    def process_payment(self, amount: float) -> bool:
        ...


class OldPaymentSystem:
    def execute(self, currency_code: str, amount_cents: int) -> dict:
        if amount_cents <= 0:
            return {'result': 'fail', 'reason': 'Amount must be positive'}
        return {'result': 'success', 'transaction': 'OLDPAY123'}


class OldPaymentAdapter:
    def __init__(self, old_system: OldPaymentSystem, currency: str = 'USD'):
        self._old_system = old_system
        self._currency = currency

    def process_payment(self, amount: float) -> bool:
        cents = int(round(amount * 100))
        response = self._old_system.execute(self._currency, cents)
        return response.get('result') == 'success'


class ClassStyleAdapter(OldPaymentSystem, PaymentInterface):
    def process_payment(self, amount: float) -> bool:
        cents = int(round(amount * 100))
        response = self.execute('USD', cents)
        return response.get('result') == 'success'


def run_payment(processor: PaymentInterface, amount: float):
    if processor.process_payment(amount):
        print(f"Payment of {amount:.2f} completed.")
    else:
        print(f"Payment of {amount:.2f} could not be processed.")


if __name__ == "__main__":
    legacy_system = OldPaymentSystem()
    adapter = OldPaymentAdapter(legacy_system, currency='EUR')
    run_payment(adapter, 12.34)

    class_adapter = ClassStyleAdapter()
    run_payment(class_adapter, 0)
