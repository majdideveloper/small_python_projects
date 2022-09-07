#!/usr/bin/env python3
# this funtion return index of number n 
def binarySearch(listNum,value):
    low = 0
    high = len(listNum) - 1
    while low <= high:
        middle = high - low
        if listNum[middle] == value:
            return middle
        elif listNum[middle] < value:
            low = middle + 1
        else:
            high = middle -1





print ("-------------Binary Search------------------")
lenList = int(input("give me the length of the list\n"))

listNumber = []
index = 0
while index != lenList:
    number = int(input(f"give me the item number {len(listNumber) + 1} in list\n"))
    if len(listNumber) > 0 and number < listNumber[index - 1]:
        print(f"your number need to be more than {listNumber[index - 1]}")
        
    else:
        listNumber.append(number)
        index+=1
print("your list")
print(listNumber)    
numberToFound = int(input("give me the number to finding .....\n"))
a = binarySearch(listNumber,numberToFound)
if a != None:
    print(f"{numberToFound} is the item number {a + 1} in list")
else:
    print(f"{numberToFound} is not found in list")












           

