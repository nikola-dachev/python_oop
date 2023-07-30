class Car():
    def __init__(self, name, model, engine):
        self.name = name
        self.model = model
        self.engine = engine

    def get_info(self):
        return f'This is {self.name} {self.model} with engine {self.engine}'


first_car = Car('opel', 'astra', '1.6V')

print(first_car.model)
print(first_car.get_info())