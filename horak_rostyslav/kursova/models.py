from dataclasses import dataclass, asdict
from datetime import datetime

@dataclass
class Equipment:
    id: int
    name: str
    type: str

    def to_dict(self):
        return asdict(self)

    @staticmethod
    def from_dict(d):
        return Equipment(id=d["id"], name=d["name"], type=d["type"])


@dataclass
class RentalRequest:
    id: int
    equipment_id: int
    client: str
    start: str   # ISO format
    end: str     # ISO format

    def conflicts_with(self, other: "RentalRequest") -> bool:
        if self.equipment_id != other.equipment_id:
            return False
        a1 = datetime.fromisoformat(self.start)
        a2 = datetime.fromisoformat(self.end)
        b1 = datetime.fromisoformat(other.start)
        b2 = datetime.fromisoformat(other.end)
        return not (a2 < b1 or b2 < a1)

    def to_dict(self):
        return asdict(self)

    @staticmethod
    def from_dict(d):
        return RentalRequest(
            id=d["id"],
            equipment_id=d["equipment_id"],
            client=d["client"],
            start=d["start"],
            end=d["end"]
        )
