# 2) შექმენით ცვლადი num, რომლის მნიშვნელობასაც შემოიტანს მომხმარებელი (გამოიყენეთ input() ფუნქცია). თუ ეს რიცხვი ტოლი იქნება 18ის მაშინ გამოუტანეთ რომ მან მოიგო სათამაშო დინოზავრი, თუ ეს რიცხვი ტოლი იქნება 33ის მაშინ გამოუტანეთ რომ მან მოიგო სათამაშო კურდღელი, ყველა სხვა შემთხვევაში გამოუტანეთ რომ ვერაფერი ვერ მოიგო და მომავალში თავიდან სცადოს.
num = int(input("enter number: "))
if num == 18:
   print ("man moigo dinozavri ")
elif num == 33:
   print("man moigo kurdgeli")
else:
   print("man veraferi ver moigo tavidan scados")
# 3) დაწერეთ if-else condition კოდი: თუ მომხმარებლის შემოტანილი ასაკი ნაკლებია 13ზე, დაუპრინტეთ "You are kid",  თუ მეტია 13ზე და ნაკლებია 20ზე, დაუპრინტეთ "You are teenager", თუ მეტია 20'ზე, დაუპრინტეთ "You are grown up".
aqlemi = int(input("enter your age: "))
if aqlemi > 13:
   print("you are kid")
elif aqlemi < 20:
   print("you are teenager")
else:
   print("you are grow up")
   
#4) შექმენით for loop'ი (range(20)'ით), შიგნით კი დაწერეთ ასეთი if-else condition'ი: თუ i (საიტერაციო ცვლადი) ნაკლებია ან ტოლია 10'ის მაშინ გამოიტანოს "Hello world"ები, თუ მეტია 10'ზე მაშინ გამოიტანოს "Goodbye world"ები.
for i in range(20):
   if i <= 10:
      print("Hello world")
    
