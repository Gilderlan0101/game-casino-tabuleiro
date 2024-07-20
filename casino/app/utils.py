import random
from slot import Slot



slot_type = []
slot_type += [Slot(display="Carta", value=5)] * 10
slot_type += [Slot(display="Carta", value=5)] * 10
slot_type += [Slot(display="Moeda", value=1)] * 8
slot_type += [Slot(display="Moeda", value=1)] * 6
slot_type += [Slot(display="Moeda", value=1)] * 6
slot_type += [Slot(display="Moeda", value=3)] * 5
slot_type += [Slot(display="Moeda", value=3)] * 5
slot_type += [Slot(display="Uvas", value=2)] * 3
slot_type += [Slot(display="Uvas", value=2)] * 3
slot_type += [Slot(display="Uvas", value=2)] * 3
slot_type += [Slot(display="Uvas", value=2)] * 3
slot_type += [Slot(display="Uvas", value=2)] * 3
slot_type += [Slot(display="Uvas", value=2)] * 3
slot_type += [Slot(display="Uvas", value=2)] * 3
slot_type += [Slot(display="Uvas", value=2)] * 3


def random_slot():
    slot = random.choice(slot_type)
    return slot.copy(deep=True)