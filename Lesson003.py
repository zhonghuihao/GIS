# Operate On Lists, Sets, Tubes
# Lists
# x = ['1', '2', '3', '4', '5', '6', '7']
# y = range(20)
# print(len(x), x[0:len(x)])  # index , 0 : len()-1
# print(x[:-1])
# print(x[::2], x[::-1])
# [x for x in y if x%2 == 0]  # >> [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# n = 25
# print ([(x, y, z) for x in range(1, n ) for y in range(x, n) for z in range(y, n) if x*x + y*y == z*z ])

## zip Function
# names = ['a', 'b', 'c', 'd']
# ages = [10, 11, 12, 13]
# for name, age in zip(names, ages):
#     print(name, age)

## Sets
# x = {3, 1, 2}
# print(x, type(x))

## Strings
# a = 'hello world'
# b = 'python'
# 'hello' in a                  # >>True
# a.split()                     # >>['hello', 'world']
# ",".join(a.split())           # >>'hello,world'
# ' hello Jim '.strip()         # >>'hello Jim'
# 'hello Jim'.strip('Jim')      # >>'hello '
# "%s %s" % (a, b)              # >>'hello world python'
# 'Chapter %d: %s' % (2, 'Data Structures')  # >>'Chapter 2: Data Structures'

## Files
# f = open('file\\foo.txt', 'a')  # w:write mode, r:read mode, a:append mode
# f.writelines(['line4\n', 'line5\n', 'line6\n'])
# f.close()

# g = open('file\\foo.txt', 'r')
# g.read()        # >>
# g.readline()        # >>'line1'
# g.readlines()       # >>['line1\n', 'line2\n', 'line3\n']
# len(g.read())    # >>18, num of words of file
# len(g.read().split())    # >>3, num of words by split
# len(g.readline())    # >>6, num of words of FirstLine
# len(g.readlines())  # >>3, num of lines of file
# g.close()

## Grep
# from module import txt_grep
# lns = txt_grep('file\\foo.txt', 'she')
# print(''.join(lns))

## Wrap
# from module import txt_wrap1
# lns = txt_wrap1('file\\foo.txt', 0)
# print(''.join(lns))

## Wrap2
# from module import txt_wrap2
# lns = txt_wrap2('file\\foo.txt', 50)
# print(''.join(lns))

## Dictionaries
# a = {'x': 1, 'y': 2, 'z': 3}
# a.keys()
# a.values()
# a.items()
# print(a.get('k', 5), a)
# print(a.setdefault('k', 6), a)

# b = 'x'
# b in a
# print('hello %(name)s' % {'name': 'python'})
# print('Chapter %(index)d: %(name)s' % {'index': 2, 'name': 'Data Structures'})

# from module import txt_freq
# dic = txt_freq('file\\foo.txt')
# for wd , num in sorted(dic.items(), key = lambda x : - x[1]):
#     print(wd, num)
