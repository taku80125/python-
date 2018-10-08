menu = {
    'wine':150,
    'salad':100,
    'water':20,
    'beef':300
    'pork':250
}

def __init__(self):
    self.total =0
    self.items=[]

def add(self,items):
    self.items.append(item)
    self.total +=self.menu[item]

def printbill(self,tax,service):
    tax=(tax/100)*self.total
    service =(service/100)*self.total

    for item in self.items:
        print(f'{item} ${self.menu[item]}' )
    print(f'{Total} ${total})    


