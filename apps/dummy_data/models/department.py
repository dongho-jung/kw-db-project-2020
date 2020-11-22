import random


class DepartmentModel:
    def __init__(self, fake):
        self._fake = fake

        self._remain_names = {fake.slug() for _ in range(50)}
        self._remain_places = {fake.address() for _ in range(50)}
        self._id = -1

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self._id += 1

            name = random.sample(self._remain_names, 1)[0]
            self._remain_names -= {name}

            place = random.sample(self._remain_places, 1)[0]
            self._remain_places -= {place}

            return (self._id, name, place)
        except KeyError:
            raise StopIteration from None
