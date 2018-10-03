numbers = [123,54,45,34,57,78]

# square = []

# for number in numbers:
#     if number % 2 ==0:
#         square.append(number**2)
# print(square)

square = [number**2 for number in numbers if number %2 ==0 ]
print(square)