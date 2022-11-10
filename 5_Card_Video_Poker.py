"""Jack or Better Video Poker
By Taylor Harrison"""
from tkinter import *
from random import shuffle
from PIL import Image, ImageTk
from tkinter import messagebox

root = Tk()
root.title("Jacks or Better Video Poker")
root.iconbitmap(r"C:\ico\Gaming-Cards.ico")
root.geometry("1100x620")
root.configure(background="green")


state1: bool = False
state2: bool = False
state3: bool = False
state4: bool = False
state5: bool = False

bet5_state: bool = False
bet10_state: bool = False
bet25_state: bool = False

money: int = int(100)


# Resize Cards
def resize_card(card):
    # Open the image
    global our_card_img
    our_card_img = Image.open(card)

    # Resize img
    re_card_img = our_card_img.resize((140, 208))
    our_card_img = ImageTk.PhotoImage(re_card_img)
    return our_card_img


# Shuffle the cards
def shuffle_deck():
    reset_card_state()
    draw_button.config(state="normal")
    # define deck
    suits = ["diamonds", "clubs", "hearts", "spades"]
    values = range(2, 15)

    global deck
    deck = []
    deck = [[v, s] for s in suits for v in values]
    shuffle(deck)

    # Create player
    global player
    player = []
    # player = [[5, "spades"],[3, "hearts"],[4, "diamonds"],[14, "diamonds"],[2, "diamonds"],]
    # player = [[10, "spades"],[11, "spades"],[12, "spades"],[14, "spades"],[13, "spades"],]
    # Grab 5 cards from the deck

    for i in range(5):
        player.append(deck[0])
        deck.remove(deck[0])

    global cardImg
    cardImg = []
    for i, v in enumerate(player):
        value = str(player[i][0])
        suite = str(player[i][1])
        cardImg.append(f"{value}_of_{suite}")

    fill_in_cards(cardImg)
    shuffle_button.config(state="disabled")


# Place card pictures on screen
def fill_in_cards(cardImg):
    # Player img/ cards
    global player_image1, player_image2, player_image3, player_image4, player_image5

    player_image1 = resize_card(f"C:\\ico\\PNG-cards-1.3\\{cardImg[0]}.png")
    player_label_1.config(image=player_image1, background="white")
    player_image2 = resize_card(f"C:\\ico\\PNG-cards-1.3\\{cardImg[1]}.png")
    player_label_2.config(image=player_image2, background="white")
    player_image3 = resize_card(f"C:\\ico\\PNG-cards-1.3\\{cardImg[2]}.png")
    player_label_3.config(image=player_image3, background="white")
    player_image4 = resize_card(f"C:\\ico\\PNG-cards-1.3\\{cardImg[3]}.png")
    player_label_4.config(image=player_image4, background="white")
    player_image5 = resize_card(f"C:\\ico\\PNG-cards-1.3\\{cardImg[4]}.png")
    player_label_5.config(image=player_image5, background="white")


def card_select_1(state):
    global state1
    if state == False:
        player_label_1.config(background="#EF130D")
        state = True
    elif state == True:
        player_label_1.config(background="white")
        state = False
    state1 = state


def card_select_2(state):
    global state2
    if state == False:
        player_label_2.config(background="#EF130D")
        state = True
    elif state == True:
        player_label_2.config(background="white")
        state = False
    state2 = state


def card_select_3(state):
    global state3
    if state == False:
        player_label_3.config(background="#EF130D")
        state = True
    elif state == True:
        player_label_3.config(background="white")
        state = False
    state3 = state


def card_select_4(state):
    global state4
    if state == False:
        player_label_4.config(background="#EF130D", borderwidth="6")
        state = True
    elif state == True:
        player_label_4.config(background="white", borderwidth="6")
        state = False
    state4 = state


def card_select_5(state):
    global state5
    if state == False:
        player_label_5.config(background="#EF130D")
        state = True
    elif state == True:
        player_label_5.config(background="white")
        state = False
    state5 = state


def reset_card_state():
    global state1, state2, state3, state4, state5
    state1 = False
    state2 = False
    state3 = False
    state4 = False
    state5 = False


def draw():
    global player, deck, money
    if state1 == False:
        player.remove(player[0])
        player.insert(0, deck[0])
        deck.remove(deck[0])
    if state2 == False:
        player.remove(player[1])
        player.insert(1, deck[0])
        deck.remove(deck[0])
    if state3 == False:
        player.remove(player[2])
        player.insert(2, deck[0])
        deck.remove(deck[0])
    if state4 == False:
        player.remove(player[3])
        player.insert(3, deck[0])
        deck.remove(deck[0])
    if state5 == False:
        player.remove(player[4])
        player.insert(4, deck[0])
        deck.remove(deck[0])

    cardImg = []
    for i, v in enumerate(player):
        value = str(player[i][0])
        suite = str(player[i][1])
        cardImg.append(f"{value}_of_{suite}")
    fill_in_cards(cardImg)
    reset_card_state()
    money = win_check()
    money_frame.config(text=f"Total bank: ${money:.2f}")
    shuffle_button.config(state="normal")


# Function to check if there's a flush
def flush_check(cards):
    flush: bool = False
    my_suits: list = []
    # for each of the cards, create a list of the suits
    for i in range(5):
        my_suits.append(cards[i][1])
    # Create a set of the suits
    s = len(set(my_suits))
    # if the length of the set is 1, then all the suits are the same and you have a Flush!
    if s < 2:
        flush = True
        return flush
    else:
        return False


# Function to check if 4 of a kind
def four_kind(cards):
    my_nums: list = []
    for i in range(len(cards)):
        my_nums.append(cards[i][0])
    for i in range(len(my_nums)):
        item_count = my_nums.count(my_nums[i])
        if item_count == 4:
            return True
    return False


# Function to check if 3 of a kind
def three_kind(cards):
    my_nums: list = []
    for i in range(len(cards)):
        my_nums.append(cards[i][0])
    for i in range(len(my_nums)):
        item_count = my_nums.count(my_nums[i])
        if item_count == 3:
            return True
    return False


# Function to check if 2 pair
def two_pair(cards):
    two_pair: bool = False
    my_values: list = []
    # for each of the cards, create a list of the values
    for i in range(5):
        my_values.append(cards[i][0])
    s = len(set(my_values))  # Create a set of the values
    # if the length of the set is 1, then all the suits are the same and you have a Flush!
    if s == 3:
        two_pair = True
        return two_pair
    else:
        return False


# Function to check if full house
def full_house(cards):
    full_house: bool = False
    my_values: list = []
    # for each of the cards, create a list of the values
    for i in range(5):
        my_values.append(cards[i][0])
    s = len(set(my_values))  # Create a set of the values
    # if the length of the set is 1, then all the suits are the same and you have a Flush!
    if s == 2:
        full_house = True
        return full_house
    else:
        return False


# check for pair, Jacks or better
def pair(cards):
    my_nums: list = []
    for i, v in enumerate(cards):
        if cards[i][0] > 10:
            my_nums.append(cards[i][0])
    for j, q in enumerate(my_nums):
        item_count = my_nums.count(my_nums[j])
        if item_count == 2:
            return True
    return False


# check for straight
def straight(cards):
    my_nums_int = []
    my_nums: list = []
    for count, ele in enumerate(cards):
        my_nums.append(cards[count][0])
        if cards[count][0] == 14:
            my_nums.append(1)

    for i, ele in enumerate(my_nums):
        my_nums_int.append(my_nums[i])
    my_nums_int.sort()
    if len(my_nums_int) == 5:
        if (
            my_nums_int[0] == (my_nums_int[1] - 1)
            and my_nums_int[0] == (my_nums_int[2] - 2)
            and my_nums_int[0] == (my_nums_int[3] - 3)
            and my_nums_int[0] == (my_nums_int[4] - 4)
        ):
            return True
    if len(my_nums_int) == 6:
        if (
            my_nums_int[1] == (my_nums_int[2] - 1)
            and my_nums_int[1] == (my_nums_int[3] - 2)
            and my_nums_int[1] == (my_nums_int[4] - 3)
            and my_nums_int[1] == (my_nums_int[5] - 4)
        ):
            return True
        elif (
            my_nums_int[0] == (my_nums_int[1] - 1)
            and my_nums_int[0] == (my_nums_int[2] - 2)
            and my_nums_int[0] == (my_nums_int[3] - 3)
            and my_nums_int[0] == (my_nums_int[4] - 4)
        ):
            return True
        else:
            return False


# check if we won
def win_check():
    global cash
    bet: float = float()
    if bet5_state == True:
        bet = float(5)
        if bet10_state == True:
            bet = float(15)
            if bet25_state == True:
                bet = float(40)
    elif bet10_state == True:
        bet = float(10)
        if bet25_state == True:
            bet = float(35)
    elif bet25_state == True:
        bet = float(25)
    else:
        bet = 5
    # print(f"States: {bet5_state}, {bet10_state}, {bet25_state}")
    if flush_check(player) and straight(player):
        cash = money + bet * 50
        messagebox.showinfo("Straight Flush!", f"You won ${bet*50:.2f}!")
        # print(f"\nYou have a straight flush! You won 💲{bet*50:.2f}!\n")
    elif flush_check(player):
        cash = money + bet * 5
        messagebox.showinfo("Flush!", f"You won ${bet * 5:.2f}!")
        # print(f"\nYou have a flush! You won 💲{bet*5:.2f}!\n")
    elif straight(player):
        cash = money + bet * 4
        messagebox.showinfo("Straight!", f"You won ${bet * 4:.2f}!")
        # print(f"\nYou have a straight! You won 💲{bet*4:.2f}!\n")
    elif four_kind(player):
        cash = money + bet * 30
        messagebox.showinfo("Four of a Kind!", f"You won ${bet * 30:.2f}!")
        # print(f"\nFour of a kind! You won 💲{bet*30:.2f}!\n")
    elif full_house(player):
        cash = money + bet * 7
        messagebox.showinfo("Full House!", f"You won ${bet * 7:.2f}!")
        # print(f"\nFull House! You won 💲{bet*7:.2f}!\n")
    elif three_kind(player):
        cash = money + bet * 3
        messagebox.showinfo("Three of a Kind!", f"You won ${bet * 3:.2f}!")
        # print(f"\nThree of a kind! You won 💲{bet*3:.2f}!\n")
    elif two_pair(player):
        cash = money + bet * 2
        messagebox.showinfo("Two Pair!", f"You won ${bet * 2:.2f}!")
        # print(f"\nTwo pair! You won 💲{bet*2:.2f}!\n")
    elif pair(player):
        cash = money + bet * 1.5
        messagebox.showinfo("Jacks or Better!", f"You won ${bet * 1.5:.2f}!")
        # print(f"\nYou have a pair! You won 💲{bet*1.5:.2f}!\n")
    else:
        cash = money - float(bet)
        messagebox.showwarning("You lost!", f"You lost ${bet:.2f}!")
        # print(f"\nYou lost, you have 💲{cash:.2f} remaining\n")

    # print(f"\nTotal funds: 💲{cash:.2f}\n")
    draw_button.config(state="disabled")
    return cash


# Bet $5 button state, turns red when true
def bet_five(state):
    global bet5_state
    if bet5_state == False:
        bet5.config(background="#FF615C")
        state = True
    elif state == True:
        bet5.config(background="white")
        state = False
    bet5_state = state
    # print(bet5_state)


# Bet $10 button state, turns red when true
def bet_ten(state):
    global bet10_state
    if bet10_state == False:
        bet10.config(background="#FF241D")
        state = True
    elif state == True:
        bet10.config(background="white")
        state = False
    bet10_state = state
    # print(bet10_state)


# Bet $25 button state, turns red when true
def bet_two5(state):
    global bet25_state
    if bet25_state == False:
        bet25.config(background="#F80902")
        state = True
    elif state == True:
        bet25.config(background="white")
        state = False
    bet25_state = state
    # print(bet25_state)


my_frame = Frame(root, bg="green")
my_frame.pack(pady=20)


# Create player frame
player_frame = LabelFrame(
    my_frame,
    text="Pick which cards to keep",
    font=("Bodoni MT Black", 12),
    bd=0,
    background="green",
)
player_frame.grid(row=1, column=1, ipadx=20)

# Create Button Frame
button_frame = Frame(root, bg="green")
button_frame.pack(pady=20)

# Create money frame
money_frame = Label(
    my_frame,
    text=f"Total Bank: ${money:.2f}",
    font=("Bodoni MT Black", 16),
    bd=0,
    background="#FFB90F",
)
money_frame.grid(row=5, column=1, ipadx=20)

bet_frame = Frame(root, bg="green")
bet_frame.pack(pady=30)

# Player Card Buttons
player_label_1 = Button(
    player_frame,
    text="",
    background="white",
    command=lambda: card_select_1(state1),
    borderwidth="6",
)
player_label_1.grid(row=2, column=0, pady=24, padx=24)
player_label_2 = Button(
    player_frame,
    text="",
    background="white",
    command=lambda: card_select_2(state2),
    borderwidth="6",
)
player_label_2.grid(row=2, column=1, pady=24, padx=24)
player_label_3 = Button(
    player_frame,
    text="",
    background="white",
    command=lambda: card_select_3(state3),
    borderwidth="6",
)
player_label_3.grid(row=2, column=2, pady=24, padx=24)
player_label_4 = Button(
    player_frame,
    text="",
    background="white",
    command=lambda: card_select_4(state4),
    borderwidth="6",
)
player_label_4.grid(row=2, column=3, pady=24, padx=24)
player_label_5 = Button(
    player_frame,
    text="",
    background="white",
    command=lambda: card_select_5(state5),
    borderwidth="6",
)
player_label_5.grid(row=2, column=4, pady=24, padx=24)

# Create buttons
shuffle_button = Button(
    button_frame,
    text="Deal",
    font=("Bodoni MT Black", 14),
    command=shuffle_deck,
    background="#63B8FF",
)
shuffle_button.grid(row=2, column=0)

draw_button = Button(
    button_frame,
    text="Draw",
    font=("Bodoni MT Black", 14),
    command=draw,
    background="#FF83FA",
)
draw_button.grid(row=2, column=1, padx=10)

bet5 = Button(
    bet_frame,
    text="Bet $5",
    font=("Bodoni MT Black", 14),
    command=lambda: bet_five(bet5_state),
    padx=8,
)
# bet5.grid(row=4, column=0)
bet5.pack()


bet10 = Button(
    bet_frame,
    text="Bet $10",
    font=("Bodoni MT Black", 14),
    command=lambda: bet_ten(bet10_state),
)
# bet10.grid(row=4, column=1)
bet10.pack()


bet25 = Button(
    bet_frame,
    text="Bet $25",
    font=("Bodoni MT Black", 14),
    command=lambda: bet_two5(bet25_state),
)
# bet25.grid(row=4, column=2)
bet25.pack()


shuffle_deck()

if money < 0:
    messagebox.showwarning("You are out of 💰, game over!", f"💸💸💸")
    draw_button.config(state="disabled")
    shuffle_button.config(state="disabled")

root.mainloop()
