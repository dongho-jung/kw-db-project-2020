import random
from datetime import datetime


class PostModel:
    def __init__(self, fake, class_ids, student_ids):
        self._fake = fake

        self._class_ids = set(class_ids)
        self._student_ids = set(student_ids)
        self._id = -1

    def _get_board_id(self):
        self._id += 1
        return self._id

    def _get_random_created_time(self, year, quarter):
        return datetime(
            year,
            random.randint(1, 3) + (3 * (quarter - 1)),
            random.randint(1, 28),
            random.randint(0, 23),
            random.randint(0, 59),
            random.randint(0, 59),
        )

    def __iter__(self):
        return self

    def __next__(self):
        try:
            board_id = self._get_board_id()
            title = self._fake.sentence()
            content = "\n".join(self._fake.sentences(random.randint(1, 10)))
            like_, hate = random.randint(0, 1000), random.randint(0, 1000)
            hits = random.randint(0, 10000)
            category = self._fake.boolean()
            class_id, year, quarter = random.sample(self._class_ids, 1)[0]

            author = random.sample(self._student_ids, 1)[0]
            created_time = self._get_random_created_time(year, quarter)

            return (
                board_id,
                title,
                content,
                like_,
                hate,
                hits,
                category,
                class_id,
                year,
                quarter,
                author,
                created_time,
            )
        except KeyError:
            raise StopIteration from None
