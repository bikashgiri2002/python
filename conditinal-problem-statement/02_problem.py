age = int(input("Enter Your Age : "))
day = input("Enter today's Day :").lower().strip()

ticket_price = 12 if age >= 18 else 8

if (day == 'wednesday'):
    ticket_price -= 2

print(f"final price of ticket is : ${ticket_price}")