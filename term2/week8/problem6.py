winners = []

for i in range(1, 6): # for 5 games
    winners.append(input(f"Enter winner for game {i}: "))

for idx, i in enumerate(winners):
    print(f"Winner for game {idx}: {i}")