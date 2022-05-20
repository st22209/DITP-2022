# 1
list1 = [100, 200, 300, 400, 500]
list1.reverse()
print("Reverse Method 1:",list1)

list2 = [100, 200, 300, 400, 500]
print("Reverse Method 2:",list2[::-1])

# 2
list3 = ["M", "na", "i", "Pra"]
list4 = ["y", "me", "s", "sad"]

print("\nZip:", " ".join([i+j for i, j in list(zip(list3, list4))]))

# 3
list5 = [1, 2, 3, 4, 5, 6, 7]
print("\nSquare List:", ", ".join([str(i**2) for i in list5]))


# 4
list6 = [10, 20, 30, 40]
list7 = [100, 200, 300, 400]

print("\nExpected Outcome:")
# for i, j in zip(list6, list7[::-1]):
#     print(f"{i} {j}")
print("\n".join([f"{i} {j}" for i, j in zip(list6, list7[::-1])]))





