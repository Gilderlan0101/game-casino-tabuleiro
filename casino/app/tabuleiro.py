from utils import random_slot
from typing import List

class Game:
    slots: List[List[str]]
    logs: List[str]

    def __init__(self):
        self.slots = []

    def gira_roleta(self):
        self.slots = [
            [random_slot(), random_slot(), random_slot()],
            [random_slot(), random_slot(), random_slot()],
            [random_slot(), random_slot(), random_slot()],
        ]

    def desenho(self):
        for l in self.slots:
            row = ' '.join(f'[ {slot.display} ]' for slot in l)
            print(row)
        print()

    def verifica(self):
        list_results = []
        slot_horizoltal = 0

        for l in self.slots:
            if l[0].display == l[1].display and l[0].display == l[2].display:
                list_results.append(l[0])
                l[0].fill = True
                l[1].fill = True
                l[2].fill = True
                slot_horizoltal += 1

        count_diagonal = 0
        dlist = []
        for l in self.slots:
            dlist.append(l[count_diagonal])
            count_diagonal += 1

        if dlist[0].display == dlist[1].display and dlist[0].display == dlist[2].display:
            list_results.append(dlist[0])
            dlist[0].fill = True
            dlist[1].fill = True
            dlist[2].fill = True

        count_diagonal = 2
        dlist = []
        for l in self.slots:
            dlist.append(l[count_diagonal])
            count_diagonal -= 1

        if dlist[0].display == dlist[1].display and dlist[0].display == dlist[2].display:
            list_results.append(dlist[0])
            dlist[0].fill = True
            dlist[1].fill = True
            dlist[2].fill = True

        return list_results
