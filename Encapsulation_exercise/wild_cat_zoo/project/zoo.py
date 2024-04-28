from typing import List
from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int) -> None:
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price: int) -> str:
        is_capacity_left = len(self.animals) < self.__animal_capacity
        is_budget_left = self.__budget >= price

        if is_capacity_left and is_budget_left:
            self.animals.append(animal)
            self.__budget -= price

            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        elif is_capacity_left and not is_budget_left:
            return "Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker: Worker) -> str:
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)

            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name: str) -> str:
        try:
            check_worker = next(filter(lambda w: w.name == worker_name, self.workers))
        except StopIteration:

            return f"There is no {worker_name} in the zoo"

        self.workers.remove(check_worker)

        return f"{worker_name} fired successfully"

    def pay_workers(self) -> str:
        summed_salaries = sum([worker.salary for worker in self.workers])

        if self.__budget >= summed_salaries:
            self.__budget -= summed_salaries

            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        summed_budget_for_care = sum([animal.money_for_care for animal in self.animals])

        if self.__budget > summed_budget_for_care:
            self.__budget -= summed_budget_for_care

            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self):
        lions = [animal.__repr__() for animal in self.animals if animal.__class__.__name__ == 'Lion']
        joined_lions = '\n'.join(lions)
        tigers = [animal.__repr__() for animal in self.animals if animal.__class__.__name__ == 'Tiger']
        joined_tigers = '\n'.join(tigers)
        cheetahs = [animal.__repr__() for animal in self.animals if animal.__class__.__name__ == 'Cheetah' ]
        joined_cheetahs = '\n'.join(cheetahs)
        result = f"You have {len(self.animals)} animals\n"
        result += f"----- {len(lions)} Lions:\n{joined_lions}\n"
        result += f"----- {len(tigers)} Tigers:\n{joined_tigers}\n"
        result += f"----- {len(cheetahs)} Cheetahs:\n{joined_cheetahs}"

        return result

    def workers_status(self):
        keepers = [worker.__repr__() for worker in self.workers if worker.__class__.__name__ == 'Keeper']
        joined_keepers = '\n'.join(keepers)
        caretakers = [worker.__repr__() for worker in self.workers if worker.__class__.__name__ == 'Caretaker']
        joined_caretakers = '\n'.join(caretakers)
        vets = [worker.__repr__() for worker in self.workers if worker.__class__.__name__ == 'Vet']
        joined_vets = '\n'.join(vets)
        result = f"You have {len(self.workers)} workers\n"
        result += f"----- {len(keepers)} Keepers:\n{joined_keepers}\n"
        result += f"----- {len(caretakers)} Caretakers:\n{joined_caretakers}\n"
        result += f"----- {len(vets)} Vets:\n{joined_vets}"

        return result
