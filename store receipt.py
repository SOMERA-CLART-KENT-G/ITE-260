


name = input("Enter Costomer name: ")
cnumber = input("Enter contact number: ")
address = input("Enter address: ")

print("")

p1item = input("Enter product 1 name: ")
p1price = float(input("Enter the price: "))
p1qty = int(input("Enter the quantity: "))
amount1 = p1price * p1qty

print("")

p2item = input("Enter product 2 name: ")
p2price = float(input("Enter the price: "))
p2qty = int(input("Enter the quantity: " ))
amount2 = p2price * p2qty

print("")

p3item = input("Enter product 3 name: ")
p3price = float(input("Enter the price: "))
p3qty = int(input("Enter the quantit: "))
amount3 = p3price * p3qty

discount = float(input("Enter Discount (%): "))

print("     ")
print("===========================")
print("              STORE RECEIPT                     ")
print("===========================")
print("     ")
print("Customer Name:" , name )
print("Contact Number:" , cnumber)
print("Address:" , address)
print("-------------------------------------------------------")
print("Product      Price     Qty      Amount ")
print("-------------------------------------------------------")
print(p1item,   p1price,  p1qty,  amount1 )
print(p2item,   p2price,  p2qty,  amount2 )
print(p3item,   p3price,  p3qty,  amount3 )
print("-------------------------------------------------------")
print("Subtotal:", amount1 + amount2 + amount3)
Subtotal = amount1 + amount2 + amount3
print("Discount amount:", Subtotal * discount/100)
print("-------------------------------------------------------")
print("TOTAL:" ,       Subtotal - discount)
print("===========================")