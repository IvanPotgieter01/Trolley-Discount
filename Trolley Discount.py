import random
final_amount = 0
end = False
customers = 0
total_trolley = 0
name = input("Enter name: ")
trolleys = int(input("How many trolleys? "))
discount = 0
discount_percentage = 0
discount_amount = 0
amount = trolleys * 80
total_trolley += trolleys
total_sales = 0
customers += 1
if trolleys > 55:
    discount = random.randint(41, 51)
elif trolleys > 40:
    discount = random.randint(31, 41)
elif trolleys > 25:
    discount = random.randint(21, 31)
elif trolleys > 10:
    discount = random.randint(11, 21)
else:
    discount = 5
discount_percentage = discount / 100
discount_amount = amount - (discount_percentage * amount)
print("Discount percentage applied:", discount, "%")
print("Amount: ", amount)
print("Discount: ", discount_amount)
print("Final amount: ", amount - discount_amount)
print("**************************")
total_sales = total_sales + amount
print("The total sales amoount of ", customers, "is", amount, ",buying ", total_trolley, "trolleys.")
