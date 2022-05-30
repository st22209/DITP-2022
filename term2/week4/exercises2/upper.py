def case_count(text: str) -> list[int]:
    upper, lower = (0,0)
    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1

    return [upper, lower]

print(case_count("HelOowkow jnTHerioteuqht MAtequtipq3153wqtg3biu2jw"))