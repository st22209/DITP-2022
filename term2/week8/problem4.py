player_a, player_b = 0, 0

for i in range(10):
    print("Round", (i + 1))
    winner = input("Who won? (A/B) ").lower()
    knockout = input(
        f"Did player {winner} knockout player {'B' if winner == 'a' else 'A'}? (Y/N): "
    ).lower()
    if knockout == "Y":
        if winner == "a":
            player_a += 10
        else:
            player_b += 10
    else:
        if winner == "a":
            player_a += 10
            player_b += 9
        else:
            player_b += 10
            player_a += 9

print(f"Player A score: {player_a} | Player B score: {player_b}")
if player_a < player_b:
    print("The winner is Player B")
elif player_b < player_a:
    print("The winner is Player B")
else:
    print("Draw!")
