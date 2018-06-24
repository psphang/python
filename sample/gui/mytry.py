import tkinter as tk

insertnames = ["Title", "Location", "Tags", "Section", "Blah"]
obj = []

root = tk.Tk()

firstFrame = tk.Frame(root)
entryFrame = tk.Frame(root)

def mainmenu():
    firstFrame.pack()
    insertButton.pack(fill='x')

def insertcall():
    firstFrame.forget()
    entryFrame.pack()

    title = tk.Entry(entryFrame)
    title.bind('<Return>', lambda event: focus(title))
    title.grid(row=0, column=1)
    obj.append(title)
    tk.Label(entryFrame, text='Title').grid(row=0, column=0)

    location = tk.Entry(entryFrame)
    location.bind('<Return>', lambda event: focus(location))
    location.grid(row=1, column=1)
    obj.append(location)
    tk.Label(entryFrame, text='Location').grid(row=1, column=0)

    tags = tk.Entry(entryFrame)
    tags.bind('<Return>', lambda event: focus(tags))
    tags.grid(row=2, column=1)
    obj.append(tags)
    tk.Label(entryFrame, text='Tags').grid(row=2, column=0)

    section = tk.Entry(entryFrame)
    section.bind('<Return>', lambda event: focus(section))
    section.grid(row=3, column=1)
    obj.append(section)
    tk.Label(entryFrame, text='Section').grid(row=3, column=0)

    blah = tk.Entry(entryFrame)
    blah.bind('<Return>', lambda event: focus(blah))
    blah.grid(row=4, column=1)
    obj.append(blah)
    tk.Label(entryFrame, text='Blah').grid(row=4, column=0)

def focus(entryobj):
    i = 0
    for item in obj: #for each try and get next item unless it gives an error (then it must be the last entry so put it to 0)
        try:
            if item == entryobj:
                obj[i+1].focus_set()
                break
        except IndexError:
            obj[0].focus_set()
        i += 1

insertButton = tk.Button(firstFrame, text='Insert', command=insertcall)
insertButton.pack()

mainmenu()

root.mainloop()
