
OriginalPrice = int(input("Enter the original Price: "))
DiscountPercent = int(input("Enter the discount percent: "))

FinalPrice = OriginalPrice * (1 - (DiscountPercent / 100))

print("The Original Price of {} becomes {} after {}% discount".format(OriginalPrice, FinalPrice, DiscountPercent))
