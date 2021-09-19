from tkinter import *
from tkinter import messagebox

count = 0
panels = ["panel"] * 10  # = ['panel', 'panel', 'panel', 'panel', 'panel', 'panel', 'panel', 'panel', 'panel', 'panel']


def winner(panels, mark):
    return ((panels[1] == panels[2] == panels[3] == mark)
            or (panels[1] == panels[4] == panels[7] == mark)
            or (panels[1] == panels[5] == panels[9] == mark)
            or (panels[2] == panels[5] == panels[8] == mark)
            or (panels[3] == panels[6] == panels[9] == mark)
            or (panels[3] == panels[5] == panels[7] == mark)
            or (panels[4] == panels[5] == panels[6] == mark)
            or (panels[7] == panels[8] == panels[9] == mark)
            )


def checker():
    if winner(panels, mark) and mark == 'X':
        messagebox.showinfo("Result", "Player1 wins")
        root.destroy()
    elif winner(panels, mark) and mark == 'O':
        messagebox.showinfo("Result", "Player2 wins")
        root.destroy()


def tap_the_choice(digit):
    global count, mark
    if digit == 1:
        if count % 2 == 0:
            mark = 'X'
        elif count % 2 != 0:
            mark = 'O'
        panels[digit] = mark
        button1.config(text=mark)
        count += 1
        checker()

    if digit == 2:
        if count % 2 == 0:
            mark = 'X'
        elif count % 2 != 0:
            mark = 'O'
        panels[digit] = mark
        button2.config(text=mark)
        count += 1
        checker()

    if digit == 3:
        if count % 2 == 0:
            mark = 'X'
        elif count % 2 != 0:
            mark = 'O'
        panels[digit] = mark
        button3.config(text=mark)
        count += 1
        checker()

    if digit == 4:
        if count % 2 == 0:
            mark = 'X'
        elif count % 2 != 0:
            mark = 'O'
        panels[digit] = mark
        button4.config(text=mark)
        count += 1
        checker()

    if digit == 5:
        if count % 2 == 0:
            mark = 'X'
        elif count % 2 != 0:
            mark = 'O'
        panels[digit] = mark
        button5.config(text=mark)
        count += 1
        checker()

    if digit == 6:
        if count % 2 == 0:
            mark = 'X'
        elif count % 2 != 0:
            mark = 'O'
        panels[digit] = mark
        button6.config(text=mark)
        count += 1
        checker()

    if digit == 7:
        if count % 2 == 0:
            mark = 'X'
        elif count % 2 != 0:
            mark = 'O'
        panels[digit] = mark
        button7.config(text=mark)
        count += 1
        checker()

    if digit == 8:
        if count % 2 == 0:
            mark = 'X'
        elif count % 2 != 0:
            mark = 'O'
        panels[digit] = mark
        button8.config(text=mark)
        count += 1
        checker()

    if digit == 9:
        if count % 2 == 0:
            mark = 'X'
        elif count % 2 != 0:
            mark = 'O'
        panels[digit] = mark
        button9.config(text=mark)
        count += 1
        checker()

    if count > 8 and winner(panels, 'X') == False and winner(panels, 'O') == False:
        messagebox.showinfo("Result", "Match Tied")
        root.destroy()


root = Tk()
root.title("GUI Tic Tac Toe Game")

Label(root, text="Player1 : X", font="times 15").grid(row=0, column=1)
Label(root, text="Player2 : O", font="times 15").grid(row=0, column=2)

button1 = Button(root, width=15, font=('Times 16 bold'), height=7, command=lambda: tap_the_choice(1))
button1.grid(row=1, column=1)
button2 = Button(root, width=15, height=7, font=('Times 16 bold'), command=lambda: tap_the_choice(2))
button2.grid(row=1, column=2)
button3 = Button(root, width=15, height=7, font=('Times 16 bold'), command=lambda: tap_the_choice(3))
button3.grid(row=1, column=3)
button4 = Button(root, width=15, height=7, font=('Times 16 bold'), command=lambda: tap_the_choice(4))
button4.grid(row=2, column=1)
button5 = Button(root, width=15, height=7, font=('Times 16 bold'), command=lambda: tap_the_choice(5))
button5.grid(row=2, column=2)
button6 = Button(root, width=15, height=7, font=('Times 16 bold'), command=lambda: tap_the_choice(6))
button6.grid(row=2, column=3)
button7 = Button(root, width=15, height=7, font=('Times 16 bold'), command=lambda: tap_the_choice(7))
button7.grid(row=3, column=1)
button8 = Button(root, width=15, height=7, font=('Times 16 bold'), command=lambda: tap_the_choice(8))
button8.grid(row=3, column=2)
button9 = Button(root, width=15, height=7, font=('Times 16 bold'), command=lambda: tap_the_choice(9))
button9.grid(row=3, column=3)

root.mainloop()
