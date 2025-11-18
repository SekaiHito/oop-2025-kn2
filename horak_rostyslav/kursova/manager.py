import json
from typing import List, Optional
from models import Equipment, RentalRequest

DATA_FILE = "rental_data.json"

class RentalManager:
    def __init__(self, data_file=DATA_FILE):
        self.equipments: List[Equipment] = []
        self.rentals: List[RentalRequest] = []
        self.data_file = data_file
        self._next_equip_id = 1
        self._next_rental_id = 1
        self.load()

    def add_equipment(self, name: str, type_: str) -> Equipment:
        eq = Equipment(id=self._next_equip_id, name=name, type=type_)
        self.equipments.append(eq)
        self._next_equip_id += 1
        self.save()
        return eq

    def remove_equipment(self, equip_id: int) -> bool:
        self.equipments = [e for e in self.equipments if e.id != equip_id]
        self.rentals = [r for r in self.rentals if r.equipment_id != equip_id]
        self.save()
        return True

    def create_rental(self, equipment_id: int, client: str, start_iso: str, end_iso: str) -> Optional[RentalRequest]:
        new = RentalRequest(id=self._next_rental_id, equipment_id=equipment_id, client=client, start=start_iso, end=end_iso)
        for r in self.rentals:
            if new.conflicts_with(r):
                return None
        self.rentals.append(new)
        self._next_rental_id += 1
        self.save()
        return new

    def delete_rental(self, rental_id: int):
        self.rentals = [r for r in self.rentals if r.id != rental_id]
        self.save()

    def save(self):
        data = {
            "equipments": [e.to_dict() for e in self.equipments],
            "rentals": [r.to_dict() for r in self.rentals],
            "_next_equip_id": self._next_equip_id,
            "_next_rental_id": self._next_rental_id
        }
        with open(self.data_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load(self):
        try:
            with open(self.data_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.equipments = [Equipment.from_dict(d) for d in data.get("equipments", [])]
            self.rentals = [RentalRequest.from_dict(d) for d in data.get("rentals", [])]
            self._next_equip_id = data.get("_next_equip_id", max([e.id for e in self.equipments], default=0)+1)
            self._next_rental_id = data.get("_next_rental_id", max([r.id for r in self.rentals], default=0)+1)
        except FileNotFoundError:
            self.equipments = []
            self.rentals = []
            self._next_equip_id = 1
            self._next_rental_id = 1
