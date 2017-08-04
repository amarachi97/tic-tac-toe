#Author: AMARACHI IWUH

def human_comp():
    C = [[0,1,2],[3,4,5],[6,7,8]]
    turn = 0
    from random import randint
    from win_or_lose import win_or_lose
    while True:
        user_play = input("chose player('X' OR 'O'): ")
        if user_play not in 'XxOo':
            continue
        elif user_play in 'Xx':
            comp_player = 'O'
            break
        else:
            comp_player = 'X'
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
        
        while True :
            computer = randint(0,8)
            if computer == user:
                continue
            else:
                print('computer has moved to', computer)
                for i in range (0,3):
                    for item in C:
                        if item[i] == computer:
                            item[i] = comp_player
                for char in C:
                    print(char)
                score = win_or_lose(C)
                if score == '*':
                    turn = turn + 1
                    break
                else:
                    return score



        
                    

            
