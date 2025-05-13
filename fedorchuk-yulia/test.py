class Love:
    raise_of_love = 100

    def __init__(self, first_love, last_love, pay_of_love):
        self.first_love = first_love
        self.last_love = last_love
        self.email_of_love = f"{first_love}.{last_love}@it.is.love"
        self.pay_of_love = pay_of_love

    def fulllove(self):
        return f"{self.first_love} {self.last_love}"

    def apply_raise_of_love(self):
        self.pay_of_love = round(self.pay_of_love * self.raise_of_love, 2)

    def __repr__(self):
        return f"Love('{self.first_love}', '{self.last_love}', {self.pay_of_love})"

    def __str__(self):
        return f"{self.fulllove()} - {self.email_of_love}"

    def __add__(self, other):
        return self.pay_of_love + other.pay_of_love

    def __len__(self):
        return len(self.fulllove())

lov_1 = Love('Fairy', 'Fly', 5000)
lov_2 = Love('Mermeid', 'Water', 6000)

print(lov_1 + lov_2)  # 11000
print(len(lov_1))  # 9