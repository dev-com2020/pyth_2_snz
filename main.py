import tkinter as tk

def on_submit():
    name = name_inp.get()
    number = num_inp.get()
    selected_idx = color_inp.curselection()
    if selected_idx:
        color = color_inp.get(selected_idx)
    else:
        color = ''
    sweet = sweet_label_inp.get('1.0', tk.END)
    message = (
        f'Dziękuje za wypełnienie ankiety, {name}\n'
        f'Ciesz się z {number} {color} pączków!'
    )
    output_line.configure(text=message)
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
name_label = tk.Label(root, text='Podaj imię:')
name_inp = tk.Entry(root)

eater_inp = tk.Checkbutton(root, text='Zaznacz jeśli jesz pączki')

num_label = tk.Label(root, text='Ile bananów zjadasz?')
num_inp = tk.Spinbox(root, from_=0, to=1000, increment=1)

color_label = tk.Label(
    root,
    text='Jaki kolor pączka lubisz?'
)
color_inp = tk.Listbox(root, height=1)
color_choices = (
    'Any', 'Brown', 'Pink', 'White', 'Green'
)
for choice in color_choices:
    color_inp.insert(tk.END, choice)

plain_label = tk.Label(root, text='Czy jadłeś warzywa?')
plain_frame = tk.Frame(root)
plain_yes_inp = tk.Radiobutton(plain_frame, text='Yes')
plain_no_inp = tk.Radiobutton(plain_frame, text='No')

sweet_label = tk.Label(
    root,
    text='Napisz wiersz o pączku...'
)
sweet_label_inp = tk.Text(root, height=3)
submit_btn = tk.Button(root, text="Submit")
submit_btn.configure(command=on_submit)

output_line = tk.Label(root, text='', anchor='w', justify='left')

title.grid(columnspan=2)
name_label.grid(row=1, column=0)
name_inp.grid(row=1, column=1)
eater_inp.grid(row=2, columnspan=2, sticky=(tk.W + tk.E))
color_label.grid(row=4, columnspan=2, sticky=tk.W, pady=10)
color_inp.grid(row=5, columnspan=2, sticky=tk.W + tk.E, padx=25)

plain_yes_inp.pack(side='left', fill='x', ipadx=10, ipady=5)
plain_no_inp.pack(side='left', fill='x', ipadx=10, ipady=5)
plain_label.grid(row=6, columnspan=2, sticky=tk.W)
plain_frame.grid(row=7, columnspan=2, sticky=tk.W)

sweet_label.grid(row=8, sticky=tk.W)
sweet_label_inp.grid(row=9, columnspan=2, sticky='NSEW')
submit_btn.grid(row=99)
output_line.grid(row=100, columnspan=2, sticky='NSEW')

root.columnconfigure(1, weight=1)
root.rowconfigure(99, weight=2)
root.rowconfigure(100, weight=1)

root.mainloop()
