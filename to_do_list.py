"""
File: ____________________
Author: Christopher Reid
CSC 120 Spring 2022
Purpose: __________________
"""

class TODO_List:
    def __init__(self):
        self._urgent = []
        self._counter = 1

    def add_urgent(self, msg):
        my_id = self._counter
        self._counter += 1
        self._urgent.append(msg)
        tmp = (my_id, msg)

    def get_first_ten(self):
        return self._urgent[:10]

    def complete(self, id):
        for i in range(len(self._urgent)):
            my_id = self._urgent[i][0]
            msg = self._urgent[i][1]
            if my_id == id:
                self._urgent.pop(i)
                return

chris = TODO_List()

chris.add_urgent('Go to class')
chris.add_urgent('Fill up gas tank')
chris.add_urgent('Grocery shop')

print(chris.get_first_ten())
