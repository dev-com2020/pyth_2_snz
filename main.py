import tkinter as tk


def on_submit():
    name = name_var.get()
    try:
        number = num_var.get()
    except tk.TclError:
        number = 1000

    color = color_var.get()

    sweet = sweet_label_inp.get('1.0', tk.END)

    eater = eater_var.get()
    plain = plain_var.get()

    message = f'Dziękuje za wypełnienie ankiety, {name}\n'

    if not eater:
        message += 'Nie lubisz pączków :('
    else:
        message += f'Ciesz się z {number} {color} pączków!'

    if plain:
        message += f'Warzywa są zdrowe!\n'
    else:
        message += f'Powinineś jeść warzywa a nie pączki!!!\n'

    if sweet.strip():
        message += f'Twój wiersz:\n{sweet}'

    output_var.set(message)
    print(sweet)


root = tk.Tk()
root.geometry('640x480+300+300')
root.resizable(False, False)
# label = tk.Label(root, text='APLIKACJA')
title = tk.Label(
    root,
    text="Wypełnij ankietę:",
    font=('Arial 16 bold'),
    bg='brown',
    fg='#FF0'
)
name_var = tk.StringVar(root)
name_label = tk.Label(root, text='Podaj imię:')
name_inp = tk.Entry(root, textvariable=name_var)

eater_var = tk.BooleanVar()
eater_inp = tk.Checkbutton(root, text='Zaznacz jeśli jesz pączki', variable=eater_var)

num_var = tk.IntVar(value=3)
num_label = tk.Label(root, text='Ile pączków zjadasz?')
num_inp = tk.Spinbox(root, from_=0, to=1000, increment=1, textvariable=num_var)

color_var = tk.StringVar(value='Any')
color_label = tk.Label(
    root,
    text='Jaki kolor pączka lubisz?'
)

color_choices = (
    'Any', 'Brown', 'Pink', 'White', 'Green'
)
color_inp = tk.OptionMenu(
    root, color_var, *color_choices
)

plain_label = tk.Label(root, text='Czy jadłeś warzywa?')
plain_frame = tk.Frame(root)
plain_var = tk.BooleanVar()
plain_yes_inp = tk.Radiobutton(plain_frame, text='Yes', value=True, variable=plain_var)
plain_no_inp = tk.Radiobutton(plain_frame, text='No', value=False, variable=plain_var)

sweet_label = tk.Label(
    root,
    text='Napisz wiersz o pączku...'
)
sweet_label_inp = tk.Text(root, height=3)
submit_btn = tk.Button(root, text="Submit")
submit_btn.configure(command=on_submit)

output_var = tk.StringVar(value='')
tk.Label(root, textvariable=output_var, anchor='w', justify='left').grid(row=100, columnspan=2, sticky='NSEW')

title.grid(columnspan=2)
name_label.grid(row=1, column=0)
name_inp.grid(row=1, column=1)
num_label.grid(row=3, sticky='we')
num_inp.grid(row=3, column=1, sticky=(tk.W + tk.E))
eater_inp.grid(row=2, columnspan=2, sticky='we')
color_label.grid(row=4, columnspan=2, sticky=tk.W, pady=10)
color_inp.grid(row=5, columnspan=2, sticky=tk.W + tk.E, padx=25)

plain_yes_inp.pack(side='left', fill='x', ipadx=10, ipady=5)
plain_no_inp.pack(side='left', fill='x', ipadx=10, ipady=5)
plain_label.grid(row=6, columnspan=2, sticky=tk.W)
plain_frame.grid(row=7, columnspan=2, sticky=tk.W)

sweet_label.grid(row=8, sticky=tk.W)
sweet_label_inp.grid(row=9, columnspan=2, sticky='NSEW')
submit_btn.grid(row=99)

root.columnconfigure(1, weight=1)
root.rowconfigure(99, weight=2)
root.rowconfigure(100, weight=1)

root.mainloop()
