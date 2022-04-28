list1 = []
for i in range(1,10):
    item = input("Enter item for list: ")
    list1.append(item)

inlist = False
while inlist == False:
    finding = input("Enter item to find: ")
    if finding in list1:
        inlist = True
    else:
        continue

found = False
while found == False:
    for i in list1:
        if i == finding:
           found = True
        else:
            continue
print("Item found at position " + str(list1.index(finding)) + ".")
        

