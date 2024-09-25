#დავალება 2: შექმენით 10 ელემენტიანი list'ი და კომენტარის სახით დანომრეთ (მიუწერეთ ინდექსები). შემდეგ კი უბრალოდ გამოიტანეთ ეკრანზე
my_list = [
    10,  # Index 0
    20,  # Index 1
    30,  # Index 2
    40,  # Index 3
    50,  # Index 4
    60,  # Index 5
    70,  # Index 6
    80,  # Index 7
    90,  # Index 8
    100  # Index 9
]

print(my_list)


#დავალება 3: პირველ დავალებაში შექმნილი List'იდან გამოიტანეთ პირველი სამი, ბოლო სამი და შუა 4 დადებითი ინდექსებით
first_three = my_list[0:3] 

last_three = my_list[-3:] 

middle_four = my_list[3:7] 

print(first_three)
print(last_three)
print(middle_four)

#დავალება 4: პირველ დავალებაში შექმნილი List'იდან გამოიტანეთ პირველი სამი, ბოლო სამი და შუა 4 უარყოფითი ინდექსებით
first_three_negative = my_list[-10:-7] 

last_three_negative = my_list[-3:]

middle_four_negative = my_list[-7:-3]

print(first_three_negative)
print(last_three_negative)
print(middle_four_negative)

#დავალება 5: შექმენით 5 სიტყვიანი სტრინგი, შექმენით კიდევ 5 ახალი ცვლადი და ინდექსინგის მეშვეობით თითოეულს მიანიჭეთ პირველი სტრინგიდან სიტყვები
sentence = "Learn coding every single day"

word1 = sentence[0:5]
word2 = sentence[6:12]
word3 = sentence[13:18]
word4 = sentence[19:25]
word5 = sentence[26:29] 

print(word1) 
print(word2) 
print(word3)
print(word4) 
print(word5)

#დავალება 6: შექმენით for loop'ი თითოეული სიმბოლოს დასაბეჭდად სტრინგში -> "Hello, World!"

string = "Hello, World!"
for char in string:
    print(char)
#დავალება 7: შექმენით while loop'ი 1-დან 10-მდე რიცხვების დასაბეჭდად

i = 1
while i <= 10:
    print(i)
    i += 1

#დავალება 8: შექმენით while loop'ი რომელიც დათვლის რიცხვებს 1-დან 100-მდე, თუმცა გამოტოვებს რიცხვებს 50-დან 60-მდე

i = 1
while i <= 100:
    if i >= 50 and i <= 60:
        i += 1
        continue
    print(i)
    i += 1

#დავალება 9: შექმენით while loop'ი, რომელიც დაიწყებს რიცხვების შეკრებას 1-დან, სანამ ჯამი არ გაუტოლდება 50-ს
total = 0
i = 1

while total < 50:
    total += i
    i += 1

print("Final total:", total)