import random
def deposit_balance():
    while True:
        amount=input("Enter Deposit Amount:")
        try:
            amount=float(amount)
            if amount>0:
                return amount
            else:
                print("amount must be greater than 0")
        except ValueError:
            print("please enter a valid amount")
def bet(balance):
    while True:
        bet=input("how much do you want to bet:")
        try:
            bet=float(bet)
            if 0<bet<=balance:
                return bet 
            elif bet>balance:
                print("you dont have balance for this bet")
            else:
                print("you cant bet negative")
        except ValueError:
            print("please enter a valid bet")
def dice_roll():
    dice=[]
    for _ in range(3):
        dice.append(random.randint(1,6))
    
    return dice
def main():
    balance=deposit_balance()
    while balance>0:
         play_game=input("press enter to play game or q to quit")
         if play_game=="q":
             break
         else:
          your_bet=bet(balance)
          balance-=your_bet
          dice_list=dice_roll()
          print(dice_list)
          unique_dice=len(set(dice_list))
          if unique_dice==1:
              print(f"all 3 dice matched you won 5x your bet ")
              win=your_bet*5
              balance+=win
              print(f"you won ${win}, your new balance is:{balance} ")
          elif unique_dice==2:
              print(f"2 dice matched you won 3x your bet")
              win=your_bet*3
              balance+=win
              print(f"you won ${win}, your new balance is:{balance}")
          else:
              print(f"no dice matched , you lost${your_bet} ,your new balance is {balance}")
    print(f"your final balance is {balance}")
    if balance==0:
        print("you ran out of money,byee!")

    
main()
              




 



    
