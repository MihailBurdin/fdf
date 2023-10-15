#1
# def is_prome(x):
#     if x == 1:
#         return False
#     if x == 2 or x % 2 != 0:
#         for i in range(3, int(x ** 0.5), 2):
#             if x % i == 0:
#                 return False
#         return True
#     return False
# z = int(input('Введите число: '))
# print(is_prome(z))

# 2
# m = [64, 25, 12, 22, 11, 1,2,44,3,122, 23, 34]
# for f in range(len(m)):
#     for f in range(f + 1, len(m)):
#        if m[f] > m[f]:
#            m[f], m[f] = m[f], m[f]
# print l

# 3
# def max_green_apple(apple):
#     apple_max = 0
#     for i in range(0, len(apple)):
#         if apple[i] > apple_max:
#             apple_max = apple[i]
#     return 'Наибольшее число: ' + str(apple_max)
# apple = []
# apple_size = int(input('Введите количество элементов массива: '))
# for i in range(0, apple_size):
#     apple.append(int(input('Введите число для элемента массива ' + str(i)+': ')))
# print(max_green_apple(apple))

#  4
# fib_1 = 1
# fib_2 = 1
# n = input("Элемент Фибоначчи: ")
# n = int(n)
# i = 0
# while i < n - 2:
#     fib_3 = fib_1 + fib_2
#     fib_1 = fib_2
#     fib_2 = fib_3
#     i = i + 1
# print("Значение этого элемента:", fib_2)

# 5
 #def repeat_words(array_):
     #repeat_words = []
     #for i in range(0, array_size):
         #repeat_words.append(0)
    #for i in range(0, len(array_)):
        #for j in range(0, len(array_)):
            # if array_[i] == array_[j]:
                 #repeat_words[i] += 1
     #index_repeat_word = -1
     #for i in range(0, len(array_)):
         #if repeat_words[i] > index_repeat_word:
             #index_repeat_word = i
     #if index_repeat_word == -1:
         #return 'Строки не повторяются'
     #else:
         #return index_repeat_word
# array = []
#array_size = int(input('Введите количество элементов массива: '))
#for i in range(0, array_size):
    #array.append(input('Введите строку для элемента массива ' + str(i)+': '))
#print(array[repeat_words(array)])