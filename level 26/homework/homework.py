#ფუნქცია, რომელიც გამოიტანს 2 რიცხვის ჯამს
def sum_two_numbers(a, b):
    return("Sum:", a + b)
sum_two_numbers(5, 10)
#ფუნქცია, რომელიც გამოიტანს 3 რიცხვის ნამრავლს
def multiply_three_numbers(x, y, z):
    return("Product:", x * y * z)
multiply_three_numbers(2, 3, 4)
#ფუნქცია, რომელიც არგუმენტად მიიღებს სახელს და გვარს და გამოიტანს მისალმებას
def greet(first_name, last_name):
    return(f"Hello, {first_name} {last_name}!")
greet("John", "Doe")
#ფუნქცია, რომელიც დააბრუნებს 2 რიცხვის ჯამს
def return_sum(a, b):
    return a + b
result_sum = return_sum(7, 8)
print("The sum is:", result_sum)
#ფუნქცია, რომელიც დააბრუნებს 3 რიცხვის ნამრავლს
def return_product(x, y, z):
    return x * y * z
result_product = return_product(2, 5, 6)
print("The product is:", result_product)

