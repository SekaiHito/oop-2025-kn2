class Check_if_fasad_and_adapter_are_the_same:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Check_if_fasad_and_adapter_are_the_same, cls).__new__(cls)
        return cls._instance

    def __init__(self, real):
        self.real = real

fasad = Check_if_fasad_and_adapter_are_the_same("Adapter")
adapter = Check_if_fasad_and_adapter_are_the_same("Fasad")

print(f"{fasad is adapter}  Fasad is adapter")  # True
print(adapter.real)  # Fasad
print(fasad.real)  # Fasad

