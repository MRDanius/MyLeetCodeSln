# from datetime import datetime
# minute_alarm_clock = [0, 15, 30, 45]
# alarm_clock = datetime.today().minute

# for i in range(5):
#     if alarm_clock in minute_alarm_clock:
#         print("Сигнал в ", alarm_clock, " мин.")
#     else:
#         print("Пока еще не настало время, сейчас ", alarm_clock, " мин.") 


# import random
# for i in range(5):
#     print("Случайное число от 1 до 60: ", random.randint(1,60))  

# var1 = "Hello"  
# var1 = 12  
# print(var1) 

#######################################################################
#                            СПИСКИ (list)                            #
#                  Гибкие массивы с обратным индексом                 #
#######################################################################
# - Обратное индексирование: lst[-1] → последний элемент (счёт с -1)  #
# - Могут содержать любые типы: числа, строки, другие списки и т.д.   #
# - Методы:                                                           #
#   • lst.index(x)    - индекс первого вхождения x                    #
#   • lst.clear()     - полная очистка списка                         #
#   • lst.reverse()   - разворот порядка элементов                    #
#   • lst.count(x)    - кол-во вхождений x                            #
# - Функции:                                                          #
#   • min(lst)/max(lst) - минимальное/максимальное значение           #
#   • random.shuffle(lst) - перемешивание элементов (import random)   #
#######################################################################

# # Примеры:
# mixed_list = [10, "текст", True, [1, 2]]  # Неоднородный список
# print(mixed_list[-1])      # Обращение к последнему элементу → [1, 2]
# print(mixed_list.index(10)) # Поиск индекса элемента → 0

# Примеры использования:
# my_list = [1, 2, 3, 'текст', True]  # Создание списка
# my_list.append(42)                   # Добавление элемента
# length = len(my_list)                # Длина списка



# letters = ["а", "е", "и", "о", "у", "э", "ю", "я"]
# word = "список – это массив"

# for item in word:
#     if item in letters:
#         print(item)  


# letters = ["а", "е", "и", "о", "у", "э", "ю", "я"]
# word = "список – это массив"
# found = []

# for item in word:
#     if item in letters:
#         if item not in found:
#             found.append(item)
# print(found)
# for item in found:       
#     print(item) 


'''УДАЛЕНИЕ ПО ЗНАЧЕНИЮ'''
# list1 = [4, 3, 2, 1]
# list1.remove(3)  


'''Метод pop удаляет элемент по индексу и возвращает его. Если не указывать параметры, то будет удален последний элемент:'''
# list1 = [4, 3, 2, 1]
# d = list1.pop()
# print(d)  


'''Чтобы добавить в конец списка еще один список, используйте метод extend.'''
# list1 = [4, 3, 2, 1]
# list1.extend([5, 6])

# for i in list1:
#     print(i) 

'''Метод insert похож на append, но только первым параметром указывается индекс элемента, перед которым будет вставка'''

# list1 = [2, 3, 4]  
# list1.insert(0, 1) # => [1, 2, 3, 4] 


# a = [1, 2, 3, 4, 5]
# b = a
# b[0] = 5

# print(a,b)

# a = [1, 2, 3, 4, 5]
# b = a.copy()
# b[0] = 5


# print(a, b)


#######################################################################
#  ██████  ██████  ██╗   ██╗ █████╗ ██████╗ ██╗  ████████╗███████╗   #
#  ██╔══██╗██╔══██╗██║   ██║██╔══██╗██╔══██╗██║  ╚══██╔══╝██╔════╝   #
#  ██║  ██║██████╔╝██║   ██║███████║██████╔╝██║     ██║   █████╗     #
#  ██║  ██║██╔══██╗╚██╗ ██╔╝██╔══██║██╔══██╗██║     ██║   ██╔══╝     #
#  ██████╔╝██║  ██║ ╚████╔╝ ██║  ██║██║  ██║███████╗██║   ███████╗   #
#  ╚═════╝ ╚═╝  ╚═╝  ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝   ╚══════╝   #
#######################################################################
#  key: value хранилище с мгновенным доступом по ключу (хеш-таблица)  #
#  - Ключи: любые НЕИЗМЕНЯЕМЫЕ типы (числа, строки, кортежи)          #
#  - Значения: любые типы данных                                      #
#  - Порядок сохраняется (начиная с Python 3.7+)                      #
#                                                                     #
#  ◈ Основные операции:                                               #
#    • d[key] - получить значение по ключу                            #
#    • d[key] = value - изменить/добавить пару                        #
#    • key in d - проверить наличие ключа                             #
#    • len(d) - количество пар                                        #
#                                                                     #
#  ◈ Полезные методы:                                                 #
#    • d.get(key[, default]) - безопасное получение значения          #
#    • d.pop(key[, default]) - удалить пару и вернуть значение       #
#    • d.update(other_d) - объединить словари                         #
#    • d.keys()/d.values()/d.items() - итераторы ключей/значений/пар #
#    • dict.fromkeys(keys[, value]) - создать словарь с общим значением
#                                                                     #
#  ◈ Особые приемы:                                                   #
#    • {k:v for k,v in ...} - генераторы словарей                     #
#    • dict(zip(keys, values)) - создание из двух списков              #
#######################################################################

# # Примеры:
# user = {
#     "id": 42,
#     "name": "Иван",
#     "skills": ["Python", "SQL"],
#     "active": True
# }

# # Доступ к элементам
# print(user["name"])  # → "Иван"
# print(user.get("age", "N/A"))  # → "N/A" (безопасный доступ)

# # Добавление/изменение
# user["email"] = "ivan@example.com"
# user.update({"city": "Москва", "age": 30})

# # Итерация
# for key, value in user.items():
#     print(f"{key}: {value}")

# person = {"firstname": "Ivan",
#           "lastname": "Ivanov",
#           "age": 30,}
# print(person)
# person["id"] = 1
# print(person) 


# word = "словарь - это не список"
# letters = {"а": 0, "е": 0, "и": 0, "о": 0}

# for character in word:
#     if character in letters:
#         letters[character] = letters[character] + 1
    
# print(letters) 


'''word = "словарь - это не список"
letters = {}'''

# for character in word:
#     if character in letters:
#         letters[character] += 1
#     else:
#         letters[character] = 1
    
# print(letters)  

# for character in word:
#     if character not in letters:
#         letters[character] = 0
#     letters[character] += 1 
# print(letters)  

# for character in word:
#     letters.setdefault(character, 0)
#     letters[character] += 1 


'''
a = [] # == a = list()
b = {} # == b = dict()''' 



# class Solution():
#     def mergeTwoLists(self, list1, list2):
# list1 = [1, 2, 4]
# list2 = [1, 3, 4]
       
# class ListNode: 
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# node1 = ListNode(1)
# node2 = ListNode(2) 

# node1.next = node2
# node3 = ListNode(4)

# node2.next = node3 

# head = node1
# current = head 

# while current:
#     print(current.val)
#     current = current.next