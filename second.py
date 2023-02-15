from first import firstdep

def second():
    firstdep()

def seconddep():
    print("seconddep")
