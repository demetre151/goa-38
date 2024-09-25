#სიების შექმნა
my_list = [10, 20, 30]
print("Initial list:", my_list) 

#.append() - სიაში ელემენტის დამატება
my_list.append(40) 
print("After append:", my_list)

#.insert() - სიაში ელემენტის დამატება
my_list.insert(1, 25) 
print("After insert:", my_list) 

#pop() - სიიდან ელემენტის ამოღება
removed_element = my_list.pop()
print("Removed element:", removed_element) 
print("After pop:", my_list) 

#find() - რადგან ეს ფუნქცია სიაზე არ ვრცელდება, შეიძლება გამოვიყენოთ სტრინგი, მაგრამ გამოვიყენოთ list.index()
index_20 = my_list.index(20) 
print("Index of 20:", index_20)

#len() - სიის სიგრძე
length = len(my_list)
print("Length of list:", length) 

#remove() - კონკრეტული ელემენტის ამოღება (თუ გვინდა, რომ არ ვიყენოთ pop())
my_list.remove(25) 
print("After remove 25:", my_list)