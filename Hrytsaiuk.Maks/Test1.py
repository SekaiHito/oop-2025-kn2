class Database:
    _ins = None
    def __new__(cls,name):
        
        if cls._ins is None:
            cls._ins = super().__new__(cls)
            return cls._ins
        else:
            return cls._ins
    def __init__ (self,name):
        self.name = name
obj=Database("my db")
print(obj.name)
obj1 = Database("my db2")
print(id(obj))
print(obj.name)
print(id(obj1))
print(id(obj))

print(obj.name)