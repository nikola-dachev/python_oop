from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price: int):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        if self.__animal_capacity > len(self.animals) and self.__budget < price:
            return "Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name: str):
        try:
            worker = next(filter(lambda x: x.name == worker_name, self.workers))
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"

        except StopIteration:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_worker_salaries = sum([worker.salary for worker in self.workers])

        if self.__budget >= total_worker_salaries:
            self.__budget -= total_worker_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        animals_expenses = sum([animal.money_for_care for animal in self.animals])
        if self.__budget >= animals_expenses:
            self.__budget -= animals_expenses
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int):
        self.__budget += amount

    def animals_status(self):
        lions_list = [animal for animal in self.animals if animal.__class__.__name__ == 'Lion']
        lion_info = '\n'.join([lion.__repr__() for lion in lions_list])

        tigers_list = [animal for animal in self.animals if animal.__class__.__name__ == 'Tiger']
        tiger_info = '\n'.join([tiger.__repr__() for tiger in tigers_list])

        cheetahs_list = [animal for animal in self.animals if animal.__class__.__name__ == 'Cheetah']
        cheetah_info = '\n'.join([cheetah.__repr__() for cheetah in cheetahs_list])
        return f"You have {len(self.animals)} animals\n" + \
            f"----- {len(lions_list)} Lions:\n" + \
            f"{lion_info}\n" + \
            f"----- {len(tigers_list)} Tigers:\n" + \
            f"{tiger_info}\n" + \
            f"----- {len(cheetahs_list)} Cheetahs:\n" + \
            f"{cheetah_info}"

    def workers_status(self):
        keepers_list = [worker for worker in self.workers if worker.__class__.__name__ == 'Keeper']
        keeper_info = '\n'.join([keeper.__repr__() for keeper in keepers_list])

        caretakers_list = [worker for worker in self.workers if worker.__class__.__name__ == 'Caretaker']
        caretaker_info = '\n'.join([caretaker.__repr__() for caretaker in caretakers_list])

        vets_list = [worker for worker in self.workers if worker.__class__.__name__ == 'Vet']
        vet_info = '\n'.join([vet.__repr__() for vet in vets_list])

        return f"You have {len(self.workers)} workers\n" + \
            f"----- {len(keepers_list)} Keepers:\n" + \
            f"{keeper_info}\n" + \
            f"----- {len(caretakers_list)} Caretakers:\n" + \
            f"{caretaker_info}\n" + \
            f"----- {len(vets_list)} Vets:\n" + \
            f"{vet_info}"
