#Author: AMARACHI IWUH

def human_human():
    C = [[0,1,2],[3,4,5],[6,7,8]]
    turn = 0
    from win_or_lose import win_or_lose
    while True:
        user_play = input("chose player('X' OR 'O'): ")
        if user_play not in 'XxOo':
            continue
        elif user_play in 'Xx':
            print("opponent is 'O'")
            player2 = 'O'
            break
        else:
            print("opponent is 'X'")
            player2 = 'X'
            break
        
    while turn < 9:
        user = int(input("where do you want to move? "))
        for i in range (0,3):
            for item in C:
                if item[i] == user:
                    item[i] = user_play
       
        score = win_or_lose(C)
        if score == '*':
            turn = turn + 1
        else:
            return score
        for char in C:
            print(char)
        

        while True:
             user2 = int(input("opponent, where do you want to move? "))
             if user2 == user:
                 continue
             else:
                 for i in range (0,3):
                     for item in C:
                         if item[i] == user2:
                             item[i] = player2
                 for char in C:
                     print(char)
       
                 score = win_or_lose(C)
                 if score == '*':
                     turn = turn + 1
                     break
                 else:
                     return score
        
               
