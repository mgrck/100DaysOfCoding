import tkinter

window = tkinter.Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=200, height=100)
window.config(padx=25, pady=25)

def clicked_button():
    result = float(input.get())*1.609
    km_result_label.config(text=round(result,2))

#Entry
input = tkinter.Entry(width=7)
input.grid(column=1, row=0)

#Labels
miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_to_label = tkinter.Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

km_result_label = tkinter.Label(text="0")
km_result_label.grid(column=1, row=1)

km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=1)

#Button
button = tkinter.Button(text="Convert", command=clicked_button)
button.grid(column=1, row=2)


window.mainloop()