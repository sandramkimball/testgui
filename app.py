import tkinter as tk
from tkinter import filedialog, Text
import os

# attach stuff to this root
root = tk.Tk()
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r' ) as f:
        tempApps = f.read()
        tempApps = tempApps.split(',') # generate array, removes extra ,'s
        apps = [x for x in tempApps if x.strip()] # strip removes empty spaces

def addApp():
    # cleans frame for updates
    for widget in frame.winfo_children():
        widget.destroy

    filename = filedialog.asopenfilename(initialdir="/", title="Select File", filetypes=(("executables", "*.exe"), ("all files", "*.*")) )
    
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray") # attach to frame, location is app
        label.pack() # pack() to attach to screen


def runApps():
    for app in apps:
        os.startfile(app)

canvas = tk.Canvas(root, height=700, width=700, bg='#263D42')
canvas.pack()

# attach another little window in larger canvas window
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx = 0.1, rely=0.1)


# add some buttons
openFile = tk.Button(root, text='Open File', padx=10, pady=5, fg="white", bg="#263D42", command=openApp)
openFile.pack()

runApps = tk.Button(root, text='Run Apps', padx=10, pady=5, fg="white", bg="#263D42", command=runApps)
runApps.pack()

# when gui opens for first time, even if everything works, be sure text pops up because updates causes cleanup
for app in apps:
    label = tk.Label(frame, text=app)
    label

root.mainloop()

# when we close the app, it saves file (f) as txt using w(write)
with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')