from queue import Queue
from threading import Lock
from time import sleep
from Classes.Customer import Customer
from colorama import Fore, init

init(autoreset=True)


class Cafe:
    def __init__(self, tables):
        self.queue = Queue()
        self.tables = tables
        self.visitor_count = 0
        self.lock = Lock()

    def customer_arrival(self):
        for i in range(1, 21):
            with self.lock:
                visitors_number = i
            print(f'{Fore.WHITE}Посетитель номер {visitors_number} прибыл')
            customer = Customer(visitors_number, self)
            self.serve_customer(customer)
            sleep(1)

    def serve_customer(self, customer):
        with self.lock:
            for table in self.tables:
                if not table.is_busy:
                    table.is_busy = True
                    print(f'{Fore.YELLOW}Посетитель номер {customer.number} сел за стол {table.number}')
                    customer.table = table
                    customer.start()
                    return
            self.queue.put(customer)
            print(f"{Fore.RED}Посетитель номер {customer.number} ожидает свободный стол")

    def free_table(self, table, customer):
        with self.lock:
            table.is_busy = False
            print(f"{Fore.GREEN}Посетитель номер {customer.number} покушал и ушел")
            if not self.queue.empty():
                next_customer = self.queue.get()
                print(f'{Fore.YELLOW}Посетитель номер {next_customer.number} сел за стол {table.number}')
                table.is_busy = True
                next_customer.table = table
                next_customer.start()

