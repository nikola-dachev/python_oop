from abc import ABC, abstractmethod
import math


class Computer(ABC):
    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0

    @property
    @abstractmethod
    def available_processors(self):
        pass

    @property
    @abstractmethod
    def max_ram(self):
        pass

    @property
    @abstractmethod
    def type(self):
        pass

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if value.strip() == '':
            raise ValueError("Manufacturer name cannot be empty.")
        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if value.strip() == '':
            raise ValueError("Model name cannot be empty.")

        self.__model = value

    def configure_computer(self, processor: str, ram: int):

        if processor not in self.available_processors:
            raise ValueError(f"{processor} is not compatible with {self.type} {self.manufacturer} {self.model}!")

        ram_memory = math.log2(ram)

        if ram_memory % 2 != 0 or ram > self.max_ram:
            raise ValueError(f"{ram}GB RAM is not compatible with {self.type} {self.manufacturer} {self.model}!")

        price = 100 * ram_memory

        self.price += self.available_processors[processor] + int(price)
        self.processor = processor
        self.ram = ram
        return f"Created {self.__repr__()} for {self.price}$."

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"
