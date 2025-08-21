#Q1
con = ["India","Pakistan"]
con.append("China")
con.append("Sri Lanka")

print(con)

con.sort()
print(con)

if "India" in con:
    print("India is in the list")
else:
    print("India is not in the list")


#Q2
# Create a tuple with five elements, each representing the price of a product. Perform the following operations:
# a. Find the maximum and minimum price from the tuple.
# b. Calculate the total cost of all products.
# c. Convert the tuple to a list and add a new product with its price.
# d. Calculate the average price of the products.

prices = {100, 200, 300, 400, 500}
print(max(prices))
print(min(prices))
print(sum(prices))
prices_list = list(prices)
prices_list.append(600)
average_price = sum(prices_list) / len(prices_list)
print("Average price:", average_price)