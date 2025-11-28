from datetime import date

class RentalRequest:
    def __init__(self, request_id, car_id, start_date, end_date):
        self.request_id = request_id
        self.car_id = car_id
        self.start_date = start_date
        self.end_date = end_date

    def overlaps(self, other):
        """Перевірка конфліктів за датами."""
        return (
            self.car_id == other.car_id and
            not (self.end_date < other.start_date or self.start_date > other.end_date)
        )

    def to_dict(self):
        return {
            "request_id": self.request_id,
            "car_id": self.car_id,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat()
        }

    @staticmethod
    def from_dict(data):
        return RentalRequest(
            request_id=data["request_id"],
            car_id=data["car_id"],
            start_date=date.fromisoformat(data["start_date"]),
            end_date=date.fromisoformat(data["end_date"])
        )
