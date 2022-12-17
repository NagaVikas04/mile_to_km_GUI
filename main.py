from tkinter import *

#window
window = Tk()
# window.minsize(width=300, height=200)
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

#labels
label_1 = Label(text="is equal to", font=("Arial", 14))
label_1.grid(row=1, column=0)

label_2 = Label(text="Miles", font=("Arial", 14))
label_2.grid(row=0, column=2)

label_3 = Label(text="Km", font=("Arial", 14))
label_3.grid(row=1, column=2)

label_4 = Label(text=0, font=("Arial", 14))
label_4.grid(row=1, column=1)

#input
input_1 = Entry()
input_1.config(width=20)
input_1.grid(row=0, column=1)

# output_1 = Entry()
# output_1.config(width=20)
# output_1.grid(row=1, column=1)


#converting miles to km and assigning the value to output_1
def conv_miles_to_km():
    output_1 = float(input_1.get()) * 1.609
    label_4.config(text=f"{output_1}")

#buttons
calc_button = Button()
calc_button.config(text="Calculate", font=("Times New Roman", 14), command=conv_miles_to_km)
calc_button.grid(row=2, column=1)





window.mainloop()