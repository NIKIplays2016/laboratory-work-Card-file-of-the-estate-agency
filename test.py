from modules.db_manager import DBManager
from random import randint

manager = DBManager()

street_arr=["ул. Якуба коласа", "ул 1-го мая", "ул. Наполеона орды", "ул. Карла", "ул. Левина",]

for i in range(100):
    manager.add_data("квартира", "Минск", street_arr[randint(0,len(street_arr)-1)], 1, randint(30,250),
                     randint(45000, 300000), randint(1,6), randint(1,16),
                     f"+3754{randint(10000000,  99999999)}")