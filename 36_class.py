class family :
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def fullname(self):
        return '{}  {} '.format(self.name, self.age)


brother = family("masaki",22)
father = family("kazuyoshi",50)

print(brother.name)

print(family.fullname(brother))

print(father.name)

