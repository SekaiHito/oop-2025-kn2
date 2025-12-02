import json

class Car:
    def __init__(self, car_id, brand, model, year, available=True):
        self.car_id = car_id
        self.brand = brand
        self.model = model
        self.year = year
        self.available = available

    def to_dict(self):
        return {
            "car_id": self.car_id,
            "brand": self.brand,
            "model": self.model,
            "year": self.year,
            "available": self.available
        }

    @staticmethod
    def from_dict(data):
        return Car(
            car_id=data["car_id"],
            brand=data["brand"],
            model=data["model"],
            year=data["year"],
            available=data["available"]
        )
