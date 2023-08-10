import random


def startgame():
    wins = 0
    losses = 0
    while losses < 3 or wins < 3:
        choice = input("Орёл или решка? (0 - орёл, 1 - решка, любое другое число - выход): ")
        if choice == '0':
            userchoice = 'орёл'
        elif choice == '1':
            userchoice = 'решка'
        else:
            break
        
        coin = random.choice(['орёл', 'решка'])
        print(f"Вы выбрали {userchoice}.")
        print(f"Монета выпала {coin}.")
        
        if userchoice == coin:
            print("Вы выиграли!")
            wins += 1
            if wins == 3:
                print("Игра окончена. Вы победили")
                break
        else:
            print("Вы проиграли.")
            losses += 1
            if losses == 3:
                print("Игра окончена. Вы проиграли")
                break
        print(f"Счет: {wins} побед, {losses} поражений.")
        print()


startgame()
