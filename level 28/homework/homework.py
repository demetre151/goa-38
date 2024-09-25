# 1. .upper()
text = "hello world"
print("Upper:", text.upper()) 

# 2. .lower()
print("Lower:", text.lower())  

# 3. .capitalize()
print("Capitalize:", text.capitalize())  

# 4. .swapcase()
print("Swapcase:", text.swapcase())  

# 5. .find()
print("Find 'world' index:", text.find("world"))  
print("Find 'python' index:", text.find("python"))  

# 6. len() - თვლის რამდენი ელემენტია
print("Length of text:", len(text))  

# List Functions
my_list = [1, 2, 3]

# 1. .append() - list'ის ბოლოში ამატებს ელემენტს
my_list.append(4)
print("After append:", my_list) 

# 2. .insert() - list'ში ამატებს
my_list.insert(1, 5)  
print("After insert:", my_list) 

# 3. .pop() - შლის list'იდან ელემენტს
removed_element = my_list.pop()
print("Removed element:", removed_element)  
print("After pop:", my_list)
