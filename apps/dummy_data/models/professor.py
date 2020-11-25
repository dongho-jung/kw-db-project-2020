import random


class ProfessorModel:
    def __init__(self, fake, department_ids):
        self._fake = fake

        self._remain_names = {fake.name() for _ in range(200)}
        self._id = -1

        self._remain_department_ids = set(department_ids)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self._id += 1

            name = random.sample(self._remain_names, 1)[0]
            self._remain_names -= {name}

            department_id = random.sample(self._remain_department_ids, 1)[0]
            self._remain_department_ids -= {department_id}

            return (self._id, name, department_id)
        except KeyError:
            raise StopIteration from None
