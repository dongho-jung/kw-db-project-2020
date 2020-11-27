import random


class ClassModel:
    def __init__(self, fake, department_ids, professor_ids):
        self._fake = fake

        self._department_ids = set(department_ids)
        self._professor_ids = set(professor_ids)

        self._added_class = set()

    def _get_random_class_id(self):
        return self._fake.numerify("####-##")

    def _get_random_year(self):
        return random.randint(2005, 2020)

    def _get_random_quarter(self):
        return random.randint(1, 4)

    def _get_random_is_copmleted(self):
        return self._fake.boolean()

    def _get_random_name(self):
        return self._fake.catch_phrase()

    def _get_random_place(self):
        return self._fake.address()

    def _get_random_period(self, credit):
        dow = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

        res = set()
        while True:
            res |= {random.choice(dow) + str(random.randint(1, 8))}
            if len(res) == credit:
                break
        return ' '.join(sorted(res))

    def _get_random_class_professor(self):
        professor = random.sample(self._professor_ids, 1)[0]
        return professor

    def _get_random_credit(self):
        return random.randint(1, 3)

    def _get_random_capacity(self):
        return random.randint(10, 70)

    def _get_random_is_pass(self):
        return self._fake.boolean()

    def _get_random_classification(self):
        return random.choice(
            ["GE", "ME", "GR", "MR", "BR"]
        )  # General Elective Major Required Basic

    def _get_random_department(self):
        department = random.sample(self._department_ids, 1)[0]
        return department

    def __iter__(self):
        return self

    def __next__(self):
        try:
            while True:
                class_id = self._get_random_class_id()
                year = self._get_random_year()
                quarter = self._get_random_quarter()

                if (class_id, year, quarter) in self._added_class:
                    continue
                self._added_class |= {(class_id, year, quarter)}
                break

            credit = self._get_random_credit()

            return (
                class_id,
                year,
                quarter,
                self._get_random_is_copmleted(),
                self._get_random_name(),
                self._get_random_place(),
                self._get_random_period(credit),
                self._get_random_class_professor(),
                credit,
                self._get_random_capacity(),
                self._get_random_is_pass(),
                self._get_random_classification(),
                self._get_random_department(),
            )
        except KeyError:
            raise StopIteration from None
