
total = 0
inv = []

def valueadding(x):
    global total
    
    
    total = total + x
    
    
    print(total)
    return total


def printval():
    
    print(total)
    return total
    
def delval():
    global total
    total = 0
    return total
    


def addinginv(x):
    
    inv.append(x)
    


def printinv():
    print(inv)
    
    return inv

def delinv():
    
    for i in range(len(inv)):
        inv.pop()
    return inv
    
    

# while True:
#     x = input(">")
    
#     if x == "a":
#         addinginv("a")
#     elif x == "b":
#         printinv()
#     elif x == "c":
#         delinv()
        
#     else:
#         break
    
   


