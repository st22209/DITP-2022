import threading

start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))
increment = int(input("Enter the amount to increment by: "))

for i in range(start, end+1, increment): 
    print(i)


end = input("Press the enter key to exit...")

if end == "":
    exit(0)

n = 0

def fuck_you():
    global n
    while True:
        n += 1
        print(n)

threads = []

for i in range(50):
    t = threading.Thread(target=fuck_you)
    t.daemon = True
    threads.append(t)

for i in range(50):
    threads[i].start()

for i in range(50):
    threads[i].join()