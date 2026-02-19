# Write your solution here
def who_won(game_board: list):
    player1_score = 0
    player2_score = 0

    for row in game_board:
        for sqaure in row:
            if sqaure == 1:
                player1_score += 1
            elif sqaure == 2:
                player2_score += 1
    if player1_score > player2_score:
        return 1
    if player1_score < player2_score:
        return 2
    if player1_score == player2_score:
        return 0
            
    