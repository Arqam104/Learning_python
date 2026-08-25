import random
MAX_LINES=3
MAX_BET=100
MIN_BET=1
ROWS=3
COLS=3
symbol_count={
    "A":2,
    "B":4,
    "C":6,
    "D":8
}
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}
def check_winning(columns,lines,bet,values):
    winnings=0
    winning_lines=[]
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            check_symbol=column[line]
            if symbol != check_symbol:
                break
        else:
            winnings+=values[symbol]*bet
            winning_lines.append(line+1)
    return winnings,winning_lines

def get_slot_machine_spin(rows,cols,symbols):
    all_symbol=[]
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbol.append(symbol)

    columns =[]
    for _ in range(cols):
        column=[]
        current_symbol=all_symbol[:]
        for _ in range(rows):
            value=random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)
        columns.append(column) 
    return columns       
            
def print_slot_machine(columns):
    for row in range (len(columns[0])):
        for i,column in enumerate(columns):
            if i!=len(columns)-1:
                print(column[row],end=" | ")
            else:
                print(column[row],end="" )
        print()        

    




def deposit():
    while True:
        amount=input("What would you like to deposit? $")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("please enter a number")
    return amount    
def get_no_of_lines():
    while True:
            lines=input("Enter the no of lines to bet on (1-"+str(MAX_LINES)+")?")
            if lines.isdigit():
                lines=int(lines)
                if 1<=lines<=MAX_LINES:
                    break
                else:
                    print("Enter a valid no of lines")
            else:
                print("please enter a number")
    return lines
def get_bet():
    while True:
        amount=input("What would you like to bet? $")
        if amount.isdigit():
            amount=int(amount)
            if MIN_BET<=amount<=MAX_BET:
               break
            else:
                print(f"Amount must be between ${MIN_BET}-${MAX_BET}")
        else:
                print("please enter a number")
    return amount    
def spin(balance):
    lines=get_no_of_lines()
    while True:
        bet=get_bet()
        total_bet=bet * lines
        if total_bet>balance:
            print(f"you do not have enough to bet that amount, your current balance is ${balance}")
        else:
            break
    print(f"you are betting ${bet} on {lines} lines. Total bet is equal to {total_bet}")
    slot=get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slot)
    winning,winning_line=check_winning(slot,lines,bet,symbol_value)
    print(f"You Won ${winning}")
    print(f"you won on lines:",*winning_line)
    return winning-total_bet
    
    
def main():
    balance=deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
    
    print(f"You left with ${balance}")

main()
