shopping_list = []

print("What should we pick up at the store? ")
print("Enter 'DONE' to stop adding items.")

while True:
    new_item = input("> ")

    if new_item == 'DONE':
        break
    else:
        shopping_list.append(new_item)
        print("Added {}! List has {} items".format(new_item, len(shopping_list)))

print("Here's your list: ")
for item in shopping_list:
    print(item)