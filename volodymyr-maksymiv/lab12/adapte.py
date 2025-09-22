from __future__ import annotations
from typing import Protocol



class PaymentProcessor(Protocol):
    def pay(self, amount: float) -> bool:
       
        ...



class LegacyGateway:
    
    def make_payment(self, currency: str, cents: int) -> dict:
       
       
        if cents <= 0:
            return {'status': 'error', 'message': 'Invalid amount'}
        return {'status': 'ok', 'tx_id': 'LEGACY1234'}



class LegacyGatewayAdapter:
    def __init__(self, gateway: LegacyGateway, currency: str = 'USD'):
        self._gateway = gateway
        self._currency = currency

    def pay(self, amount: float) -> bool:
       
        cents = int(round(amount * 100))
        result = self._gateway.make_payment(self._currency, cents)
        return result.get('status') == 'ok'



class ClassAdapter(LegacyGateway, PaymentProcessor):
    def pay(self, amount: float) -> bool:
        cents = int(round(amount * 100))
        result = self.make_payment('USD', cents) 
        return result.get('status') == 'ok'



def client_code(processor: PaymentProcessor, amount: float):
    success = processor.pay(amount)
    if success:
        print(f"Payment of {amount:.2f} succeeded.")
    else:
        print(f"Payment of {amount:.2f} failed.")


if __name__ == "__main__":
 
    legacy = LegacyGateway()
    adapter = LegacyGatewayAdapter(legacy, currency='EUR')
    client_code(adapter, 12.34)  

  
    class_adapter = ClassAdapter()
    client_code(class_adapter, 0)
  
