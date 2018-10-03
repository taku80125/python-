class payment:
    increase = 2
    def __init__(self,pay,place,date):
        self.pay = pay
        self.place = place
        self.date = date

    def all(self):
        return f'{self.pay} {self.place} {self.date}'

    def plus(self):
        self.pay = int(self.pay * self.increase)


takuma =payment(2000,"yokohama","2018/03/09")

print(takuma.place)
print(takuma.pay)
takuma.plus()
print(takuma.pay)

