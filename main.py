from tkinter import * 


root = Tk()
root.title('Deck of cards')
root.iconbitmap('reverse.png')
root.geometry("900x500")
root.configure(background="green")

my_frame = Frame(root, bg="green")
my_frame.pack(pady=20)
#create frams for cards
dealer_frame = LabelFrame(my_frame, text="Dealer", bd=0)
dealer_frame.grid(row=0, coloumn=0, padx=20, ipadx=20)

player_frame = LabelFrame(my_frame, text="Dealer", bd=0)
player_frame.grid(row=0, coloumn=0, ipadx=20)

#put cards in frames
dealer_label = Label(dealer_frame, text='')
dealer_lbel.pack(pady=20)

player_label = Label(dealer_frame, text='')
player_label.pack(pady=20)

#button 
shuffle_button = Button(root, text="Shuffle Deck", font=("Helvetica", 14))
shuffle_button.pack(pady=20)

deal_button = Button(root, text="Get cards", font=("Helvetica", 14))
dead_button.pack(pady=20)

root.mainloop()