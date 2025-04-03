# project.py
import datetime

class Project:
    def __init__(self, name, start_date, priority, cost, completion):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost = float(cost)
        self.completion = int(completion)

    def is_completed(self):
        return self.completion == 100

    def __lt__(self, other):
        return self.priority < other.priority