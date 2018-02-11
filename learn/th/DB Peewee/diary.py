from datetime import datetime
from collections import OrderedDict
import sys

from  peewee import *

db = SqliteDatabase('entries.db')

class Entry(Model):
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db

def initialize():
    """Create the database and the table if they don't exist."""
    db.connect()
    db.create_tables([Entry], safe=True)

def add_entry():
    """add an entry"""
    print("pls add entry, Ctrl+D for finish")
    data = sys.stdin.read().strip()
    if data:
        if input("save entry, y/n") != 'n':
            Entry.create(content=data)
            # Entry.save
            print("well done")

def view_entries():
    """view the previous entries"""
    for e in Entry.select():
        print("{}".format(e.entry))

menu = OrderedDict(
    [
    ('a', add_entry),
    ('v', view_entries),
    ]
)

def menu_loop():
    """Show the menu"""
    choice = None
    while choice != 'q':
        for key, value in menu.items():
            print("pls input your choice, 'q' for quit")
            print('{} : {}'.format(key, value.__doc__))
        choice = input("-->").lower().strip()
        if choice in menu.keys():
            print("{}".format(menu[choice].__doc__))
            menu[choice]()

if __name__ == '__main__':
    initialize()
    menu_loop()
