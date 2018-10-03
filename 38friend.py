class friend:
    add_friend = 0

    def __init__(self,name,age,uni):
        self.name = name
        self.age = age
        self.uni = uni
    
        friend.add_friend +=1

f1 = friend("yota",22,"keio")
print(friend.add_friend)

f2 = friend("ken",21,"waseda")
print(friend.add_friend)

print(f1.name)
print(f2.age)
