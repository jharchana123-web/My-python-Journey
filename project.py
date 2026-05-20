Name = input("Enter Your Name, Sir: ")
print(f"Oh! Hi {Name}")
 
item1 = (input(f"First Fruit item {Name}: "))
item2 = (input(f"Second Fruit item {Name}: "))
item3 = (input(f"Third Fruit item {Name}: "))
item4 = (input(f"Fourth Fruit item {Name}: "))
item5 = (input(f"Fifth Fruit item {Name}: "))

print(f"{Name}, Your items are: [{item1}, {item2}, {item3}, {item4}, {item5}]")

items = [item1, item2, item3, item4, item5]

print(f"\nTotal number of items: {len(items)}")
