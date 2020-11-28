import random
from collections import defaultdict


class GradeModel:
    def __init__(self, fake, class_ids, student_ids):
        self._fake = fake

        self._class_ids = defaultdict(list)
        for id_, year, quarter in class_ids:
            self._class_ids[year] += [(id_, quarter)]
        self._student_ids = student_ids

        self._added_grade = set()

    def _get_random_student_id(self):
        return random.sample(self._student_ids, 1)[0]

    def _get_random_class_keys(self, student_id):
        while True:
            year = int(student_id[:4])
            random_year = random.randint(year, year + 5)
            if random_year <= 2020:
                break
        return (student_id, random_year, *random.choice(self._class_ids[random_year]))

    def _get_random_retake(self):
        return self._fake.boolean(chance_of_getting_true=10)

    def _get_random_grade(self):
        return random.choice([4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0])

    def __iter__(self):
        return self

    def __next__(self):
        try:
            while True:
                student_id = self._get_random_student_id()
                key = self._get_random_class_keys(student_id)

                if key in self._added_grade:
                    continue
                self._added_grade |= {key}
                break

            return (*key, self._get_random_retake(), self._get_random_grade())
        except KeyError:
            raise StopIteration from None
