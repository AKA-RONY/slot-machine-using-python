import random


MAX_LINE = 3  # GLOBAL CONSTANT
MAX_BET= 100
MIN_BET=1

ROW=3
COL=3# this are the reels that will have symbols within


symbol_count={
    "A":2,
    "B":4,
    "C":6,
    "D":8
}
symbol_value={
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

def deposit():
    while True:
        amount = input('enter amount to be deposit $$$')  # initially the amount will be string
        if amount.isdigit():  # we have checked whether the enter string is whole number or not
            amount = int(amount)  # if the string is number then parse it or convert it into integer
            if amount > 0:
                break
            else:
                print(' amount should be greater than 0')
        else:
            print('enter a valid number')
    return amount


def num_of_lines():
    while True:
        lines = input('enter of line you want to bet on (1-' + str(MAX_LINE) + ')?')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINE:
                break
            else:
                print('enter a valid line')
        else:
            print('please enter a  number')
    return lines

# amount to be bet on each line
def get_bet():
    while True:
        amount = input('enter amount to be bet on each line $$$')  # initially the amount will be string
        if amount.isdigit():  # we have checked whether the enter string is whole number or not
            amount = int(amount)  # if the string is number then parse it or convert it into integer
            if MIN_BET<=amount<= MAX_BET:
                break
            else:
                print(f'amount must be between ${MIN_BET} - ${MAX_BET}')# using f strings , only available in python 3.6 and above
        else:
            print('enter a valid number')
    return amount

def check_winnings(columns,lines,bet,value):
    winnings=0
    winnings_lines=[]
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbol_to_check=column[line]
            if symbol!=symbol_to_check:
                break
        else:# this else after for loop means that the code after the else block will be executed after the for loop is completed
            winnings+= value[symbol]* bet
            winnings_lines.append(line+1)
    return  winnings,winnings_lines



def get_slot_machine_spin(rows,cols,symbols):# this part is bit tricky, need to give more time on it.

    all_symbol=[]
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbol.append(symbol)

    columns=[]
    for _ in range(cols):
        column=[]# this interior list gives the values of the items i.e individual row values  in of our column
        current_symbols= all_symbol[:]# ':' operator copies the  contents from main list, and put in secondary list
        for _ in range(rows):
            value= random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)


        columns.append(column)
    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i!= len(columns) -1:
                print(column[row],end='|')
            else:
                print(column[row], end='')
        print()

def spin(balance):
    lines = num_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet < balance:
            break
        else:
            print(
                'you bet amount is greater then deposit amount!!! you cant bet , either increase your deposit amount or  bet a lesser amount ')

    print(
        f' you have  ${balance} in your gaming wallet and you  have bet ${bet} on {lines} lines  , so your total bet equals ${total_bet} ')  # means if two lines gets matched you get double of your bet, if three lines you get 3x of bet
    slots = get_slot_machine_spin(ROW, COL, symbol_count)
    print_slot_machine(slots)

    winnings, winnings_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f'you won ${winnings}')
    print(f'you won on lines :', *winnings_lines)  # * operator pass all the line from the winning lines

    return winnings-total_bet
def main():  # even if the program ends, we  can run the function
    balance = deposit()
    while True:
        print(f"current balance is ${balance}")
        answer= input('press enter to play(q to quit)')
        if answer=='q':
            break
        balance += spin(balance)
    print(f'you left with ${balance}')

main()
