from first import firstdep
from third import thirddep

def second():
    firstdep()

def seconddep():
    thirddep()
    print("seconddep")
