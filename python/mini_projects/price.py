# take the product and their price in a string and then store the product and the price in two diffrent lists

data=input().split()

product=[]
price=[]

for item in data:
    if item.isalpha():
        product.append(item)
    elif item.isnumeric():
        price.append(item)

print(product)
print(price)