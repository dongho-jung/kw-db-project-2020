import random


class GradeModel:
    def __init__(self, fake, class_ids, student_ids):
        self._fake = fake

        self._class_ids = class_ids
        self._student_ids = student_ids

        self._added_grade = set()

    def _get_random_student_id(self):
        return random.sample(self._student_ids, 1)[0]

    def _get_random_class_keys(self):
        return random.sample(self._class_ids, 1)[0]

    def _get_random_retake(self):
        return self._fake.boolean()

    def _get_random_grade(self):
        return random.choice(["F", "D", "D+", "C", "C+", "B", "B+", "A", "A+"])

    def __iter__(self):
        return self

    def __next__(self):
        try:
            while True:
                key = (self._get_random_student_id(), *self._get_random_class_keys())

                if key in self._added_grade:
                    continue
                self._added_grade |= {key}
                break

            return (*key, self._get_random_retake(), self._get_random_grade())
        except KeyError:
            raise StopIteration from None
