from tkinter import *

grid = Grid()
#window
window = Tk()
window.title("Mile to Kilometer Converter")
window.config(padx=10, pady=20)



def miles_in_km():
    miles = float(input.get())
    conv_factor = 1.609344
    km = miles * conv_factor
    Kilometer_label.config(text=f"{km:.1f}")

#Entry
input = Entry(width=10 )
input.grid(column= 10, row=0)



# Label
miles_label = Label(text= "Miles", font=("Arial", 20, "bold"))
miles_label.grid(row=0, column= 12)

# 2 lable 
is_equal_to_label = Label(text= "is equal to", font=("Arial", 20, "bold"))
is_equal_to_label.grid()


#label 3
Kilometer_label = Label(text= "0", font=("Arial", 20, "bold"))
Kilometer_label.grid(column= 10, row= 1)

#Lable 4
Km_label = Label(text= "Km", font=("Arial", 20, "bold"))
Km_label.grid(column= 12, row= 1)


# button
button = Button(text="Calculate",command=miles_in_km)
button.grid(row=2, column=10)



window.mainloop()
