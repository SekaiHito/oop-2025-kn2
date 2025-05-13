class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature can't be below absolute zero (-273.15°C)")
        self._celsius = value

    @celsius.deleter
    def celsius(self):
        print("Deleting temperature...")
        del self._celsius

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32

temp = Temperature(25)

print(f"Celsius: {temp.celsius}")       
print(f"Fahrenheit: {temp.fahrenheit}")  

temp.celsius = 30                       
print(f"Updated Celsius: {temp.celsius}")
print(f"Updated Fahrenheit: {temp.fahrenheit}")

del temp.celsius                       

