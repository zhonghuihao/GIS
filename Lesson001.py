## 【Lesson001】DataTypes
## List
# stack = [3, 4, 5]
# stack.append(6)
# stack.append(7)
# stack2 = [x**2 for x in stack if x <= 3]
# stack2 = stack2 + [x for x in stack if x > 3]
# print(stack)
# print(stack2)

## Matrix
# matrix = [
# [1, 2, 3, 4],
# [5, 6, 7, 8],
# [9, 10, 11, 12]
# ]
#
# print(matrix)
# print([[row[i] for row in matrix] for i in range(4)])
#
# transposed = []
# for i in range(4):
#     transposed.append([row[i] for row in matrix])
# print(transposed)

## Tuple
# t = 12345, 456, 'hello'
# print(type(t))

## Set
# basket = {'ab', 'b', 'c', 'd', '1', '2', '3'}
# print(basket)
#
# b = set('abcd3f')
# print(b)
#
# print('【-】: ', basket - b)
# print('【|】: ', basket | b)
# print('【&】: ', basket & b)
# print('【^】: ', basket ^ b)
#
# a = {x for x in basket if x not in '123'}
# print('【a】: ', a)

## Dict
# tel = {'jack': 101, 'tim': 102, 'gre': 103}
# print('【tel】：', tel)
#
# del tel['jack']
# tel['jack2'] = 106
# tel['jack3'] = 107
# print('【tel】：', tel)
#
# print(list(tel.keys()), list(tel.values()))
# print('【sorted】：', sorted(list(tel.keys())))
#
# telA = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
# print('【telA】：', telA)
#
# telB = {x: x**2 for x in (2, 4, 6)}
# print('【telB】：', telB)
#
# telC = dict(sape=4139, guido=4127, jack=4098)
# print('【telC】：', telC)
#
# for nm, cd in tel.items():
#     print(nm, cd)













