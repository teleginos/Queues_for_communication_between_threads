import time
from threading import Thread


class Customer(Thread):
    def __init__(self, number, cafe):
        Thread.__init__(self)
        self.number = number
        self.cafe = cafe
        self.table = None

    def run(self):
        time.sleep(5)
        self.cafe.free_table(self.table, self)
