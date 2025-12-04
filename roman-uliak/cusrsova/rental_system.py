import json
import os
from car import Car
from rental_request import RentalRequest
from datetime import date

class RentalSystem:
    def __init__(self, data_file="data.json"):
        self.data_file = data_file
        self.cars = []
        self.requests = []
        self.load_data()

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.cars = [Car.from_dict(d) for d in data.get("cars", [])]
                self.requests = [RentalRequest.from_dict(r) for r in data.get("requests", [])]

    def save_data(self):
        with open(self.data_file, "w", encoding="utf-8") as f:
            json.dump({
                "cars": [c.to_dict() for c in self.cars],
                "requests": [r.to_dict() for r in self.requests]
            }, f, ensure_ascii=False, indent=4)

    # --- Операції з автомобілями ---
    def add_car(self, car):
        self.cars.append(car)
        self.save_data()

    def remove_car(self, car_id):
        self.cars = [c for c in self.cars if c.car_id != car_id]
        self.requests = [r for r in self.requests if r.car_id != car_id]
        self.save_data()

    def list_cars(self, only_available=False):
        cars = self.cars
        if only_available:
            cars = [c for c in self.cars if c.available]
        return cars

    # --- Операції з орендою ---
    def create_request(self, request):
        for r in self.requests:
            if r.overlaps(request):
                print("⚠️ Конфлікт оренди! Авто вже зайняте в цей період.")
                return False
        self.requests.append(request)
        for c in self.cars:
            if c.car_id == request.car_id:
                c.available = False
        self.save_data()
        print("✅ Заявку створено успішно!")
        return True
