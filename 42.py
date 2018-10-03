numbers = [1,2,3,4,5,6,7,8,9,10]


# add = []

# for number in numbers:
#     if number %2 ==0:
#         add.append(number +1)
# print(add)        
        
add = [number+1 for number in numbers if number %2 ==0]
print(add)

