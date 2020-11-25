import random
from collections import Counter
from hashlib import sha256


class StudentModel:
    def __init__(self, fake, major_ids, professor_ids):
        self._fake = fake

        self._major_ids = set(major_ids)
        self._professor_ids = set(professor_ids)

        self._student_id = Counter()

    def _get_random_student_id(self, year, major_id):
        key = str(year) + major_id
        id_ = self._student_id[key]
        self._student_id[key] += 1

        return f"{year:04}{major_id}{id_:02}"

    def _get_random_name(self):
        return self._fake.name()

    def _get_random_major_id(self):
        return random.sample(self._major_ids, 1)[0]

    def _get_random_year(self):
        return random.randint(1990, 2021)

    def _get_random_semester(self):
        return random.randint(0, 1)

    def _get_random_phone(self):
        return f"010{random.randint(0, 9999)}{random.randint(0, 9999)}"

    def _get_random_email(self, name):
        emails = ["gmail.com", "naver.com", "outlook.kr", "kw.ac.kr", "icloud.com"]
        refined_name = name.lower().replace(" ", "_")
        return f"{refined_name}@{random.choice(emails)}"

    def _get_random_professor_id(self):
        return random.sample(self._professor_ids, 1)[0]

    def _get_random_pw(self):
        return sha256(self._fake.password().encode()).hexdigest()

    def __iter__(self):
        return self

    def __next__(self):
        try:
            name = self._get_random_name()
            year = self._get_random_year()
            semeseter = self._get_random_semester()
            phone = self._get_random_phone()
            email = self._get_random_email(name)
            professor_id = self._get_random_professor_id()
            pw = self._get_random_pw()

            while True:
                major_id = self._get_random_major_id()
                id_ = self._get_random_student_id(year, major_id)
                if len(id_) == 10:
                    break

            return (
                id_,
                name,
                major_id,
                year,
                semeseter,
                phone,
                email,
                professor_id,
                pw,
            )
        except KeyError:
            raise StopIteration from None
