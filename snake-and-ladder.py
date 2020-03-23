from random import randint

snake = {
    14:3,
    19:11,
    25:15,
    34:9,
    45:39,
    55:50,
    63:52,
}

ladder = {
    5:10,
    13:20,
    21:29,
    36:40,
    42:54,
    51:53,
}

player_post = 0
maxRole = 64

message = """
Welcome to text-based snake and ladder game
This game uses 64 square, so in order to win you need to reach the 64th square

Below are the rules
1) You hit snake, you go down to dessignated square
2) You hit ladder, you go up to dessignated square
3) No roll-6-special-rule
"""
print(message)

while(True):
    input("Press Enter to Role")
    player_role = randint(1,6)
    player_post += player_role
    print("You role ", player_role)
    if player_post < 64:
        if player_post in snake:
            player_post = snake.get(player_post)
            print("Aw, you hit a snake, moving down to post ", player_post)
        elif player_post in ladder:
            player_post = ladder.get(player_post)
            print("Yes, you found a ladder, moving up to post ", player_post)
        else:
            print("You are on post ", player_post)
    elif player_post > 64:
        player_post -= player_role
        print("You are stuck on this post ", player_post)
    else:
        print("Congrats you have won this game")
        break
