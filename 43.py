from random import shuffle
def arrange (name):
    changer = list(name)
    shuffle(changer)
    return ''.join(changer)

names = ['takuma', 'lohit', 'yota' ]
changer = []
for name in names:
    changer.append(arrange(name))
print(changer)


print(list(map(arrange,names)))
