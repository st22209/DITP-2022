import threading

start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))
increment = int(input("Enter the amount to increment by: "))

for i in range(start, end+1, increment): 
    print(i)

