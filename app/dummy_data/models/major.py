import pathlib
import random

class MajorModel:
    _majors = open(pathlib.Path(__file__).parent / 'majors.txt').read().splitlines()

    def __init__(self):
        self._remain_majors = set(self._majors)
        self._remain_ids = set(random.choices(range(0, 9999), k=len(self._majors)))

    def __iter__(self):
        return self

    def __next__(self):
        try:
            id_ = random.sample(self._remain_ids, 1)[0]
            self._remain_ids -= {id_}

            major = random.sample(self._remain_majors, 1)[0]
            self._remain_majors -= {major}

            return (id_, major)
        except KeyError:
            raise StopIteration from None
