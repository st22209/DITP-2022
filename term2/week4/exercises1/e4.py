def calculation(x: int, y: int):
    add_ans, sub_ans = (x + y, x - y)
    return (add_ans, sub_ans)


res = calculation(69, 42)
print(res)
