numSlots = int(input())

dictItems = {}

for i in range(numSlots):
    item = input("").split()
    name = item[0]
    count = int(item[1])

    if name in dictItems:
        dictItems[name] += int(count)
    else:
        dictItems[name] = int(count)



for key,value in dictItems.items():
    print (key, ((value + 63) //64))

