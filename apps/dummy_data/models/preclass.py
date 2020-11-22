import itertools
import random


class PreclassModel:
    def __init__(self, class_ids):
        self._class_ids = set(class_ids)

        _l0 = set(random.sample(self._class_ids, 5))
        self._class_ids -= _l0

        _l1 = set(random.sample(self._class_ids, 10))
        self._class_ids -= _l1

        _l2 = set(random.sample(self._class_ids, 10))
        self._class_ids -= _l2

        _l3 = set(random.sample(self._class_ids, 15))
        self._class_ids -= _l3

        self._levels = [_l0, _l1, _l2, _l3]

    def __iter__(self):
        return self

    def __next__(self):
        try:
            level = random.choices([0, 1, 2, 3], map(len, self._levels), k=1)[0]
            _class = random.sample(self._levels[level], 1)[0]
            self._levels[level] -= {_class}
            return (
            "_" if level == 0 else random.sample(set(itertools.chain.from_iterable(self._levels[:level])), 1)[0],
            _class)
        except ValueError:
            raise StopIteration from None
