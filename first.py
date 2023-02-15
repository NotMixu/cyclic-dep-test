from second import seconddep
from third import third

def first():
    seconddep()

def firstdep():
    third()
    print("firstdep")
