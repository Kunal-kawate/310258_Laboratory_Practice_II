import tkinter as tk


def main():
    user = e.get().lower()

    if ((user=='how are you') or (user=='how r u')):
        txt.insert(tk.END,'\nI am pretty good, whats about you?')
    elif((user=='i am fine') or (user=='i am good') or (user=='i am pretty good')):
        txt.insert(tk.END,'\ngreat.....')
    elif((user=='hi') or (user=='hii') or (user=='hiii') or (user=='hello') or (user=='hey')):
        txt.insert(tk.END,'\nHello')
    else:
        txt.insert(tk.END,'\nI dont undersatnad what you mean.....')



if __name__=='__main__':
    app = tk.Tk()
    app.title("Chat Bot Ver. 0.9")

    txt = tk.Text(app)
    txt.grid(row=0,column=0,columnspan=2)

    e = tk.Entry(app,width=100)
    e.grid(row=1,column=0)

    send= tk.Button(app,text='Send', command=main).grid(row=1,column=1)

    app.mainloop()