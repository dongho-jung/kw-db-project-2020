import random

class ScholarshipModel:
    def __init__(self):
        self._added_scholarship = set()

    def __iter__(self):
        return self

    def __next__(self):
        try:
            while True:
                year = random.randint(1990, 2020)
                semester = random.randint(1, 2)

                if (year, semester) in self._added_scholarship:
                    continue
                self._added_scholarship |= {(year, semester)}
                break

            won = round(random.randint(1_000_000, 10_000_000), -3)
            return (year, semester, won)

        except KeyError:
            raise StopIteration from None
