from threading import Thread
from Classes.Cafe import Cafe
from Classes.Table import Table

tables = list()
for i in range(1, 4):
    tables.append(Table(i))

cafe = Cafe(tables)

customer_arrival_tgread = Thread(target=cafe.customer_arrival)
customer_arrival_tgread.start()
