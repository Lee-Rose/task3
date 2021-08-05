print('')
print('----------------- Task 1 ------------------')
print('')

a = ('name', 'last_name',)
b = 'age'
c = 'phone_number'
my_dict = {}
my_dict[a] = 'Liya Yoelson'
my_dict[b] = 30
my_dict[c] = '0506470815'
print(my_dict)

print('')
print('----------------- Task 2 ------------------')
print('')

def my_func(d):
    try:
        d[5] = '@'
        print(d)
    except IndexError:
        print('IndexError !')

my_func([1, 2, 3])
my_func([1, 2, 3, 6, 5, 4, 3])

print('')
print('----------------- Task 3 ------------------')
print('')

def my_func(d):
    assert len(d) >= 5
    d[5] = '@'
    print(d)

my_func([1, 2, 3, 6, 5, 4, 3])

print('')
print('----------------- Task 4 ------------------')
print('')

x_dict = {}

def add_key_and_value(a, s):
    x_dict[a] = s
    print(x_dict)
add_key_and_value(4, 10)
add_key_and_value(6, 10)
add_key_and_value(17, 'Hello_Alex')

print('')
print('----------------- Task 5 ------------------')
print('')

def dict1(n):
    r = {n: n + 3 for n in range(1, n)}
    print(r)

dict1(6)

print('')
print('----------------- Task 6 ------------------')
print('')

dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}
dic123 = dic1 | dic2 | dic3
print(dic123)

print('')
print('----------------- Task 7 ------------------')
print('')


def char_str(str1):
    dict2 = {}
    for i in str1:
        keys = dict2.keys()
        if i in keys:
            dict2[i] += 1
        else:
            dict2[i] = 1
    return dict2
print(char_str('Hellooooo'))


print('')
print('----------------- Task 8 ------------------')
print('')

from collections import Counter

def dict4():
    d1 = {'a': 100, 'b': 200, 'c': 300}
    d2 = {'a': 300, 'b': 200, 'd': 400}
    new_d1 = Counter(d1) + Counter(d2)
    print(new_d1)

dict4()



