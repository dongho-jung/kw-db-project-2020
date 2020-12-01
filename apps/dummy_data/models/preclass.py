import itertools
import random


class PreclassModel:
    def __init__(self, class_ids):
        self._class_ids = set(class_ids)

        _l0 = set(random.sample(self._class_ids, 4))
        self._class_ids -= _l0

        _l1 = set(random.sample(self._class_ids, 7))
        self._class_ids -= _l1

        _l2 = set(random.sample(self._class_ids, 6))
        self._class_ids -= _l2

        _l3 = set(random.sample(self._class_ids, 5))
        self._class_ids -= _l3

        _l4 = set(random.sample(self._class_ids, 6))
        self._class_ids -= _l4

        _l5 = set(random.sample(self._class_ids, 5))
        self._class_ids -= _l5

        self._levels = [_l0, _l1, _l2, _l3, _l4, _l5]
        self._added_keys = set()

    def __iter__(self):
        return self

    def __next__(self):
        try:
            while True:
                level = random.choices([0, 1, 2, 3, 4, 5], k=1)[0]
                _class = random.sample(self._levels[level], 1)[0]
                key = (
                    "_" if level == 0 else random.sample(set(itertools.chain.from_iterable(self._levels[:level])), 1)[
                        0],
                    _class)
                if key[0] and key[1] and key not in self._added_keys:
                    self._added_keys |= {key}
                    if random.random() > 0.8:
                        self._levels[level] -= {_class}
                    return key
        except ValueError:
            raise StopIteration from None
