from first import firstdep
from third import thirddep

def thirddep():
    firstdep()
    print('third')
    print(thirddep)
