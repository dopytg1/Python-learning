items = ['Milk', 'Bread', 'Cheese', 'Chocolate', 'Water']
prices = [10, 5, 20.5, 7.15, 2.99]


print("%-30s %s" %("Name", "Price"))
for i in range(len(items)):
    print("%-30s %s" %(items[i], round(prices[i], 2)))