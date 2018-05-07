import pytube
from tkinter import ttk
from tkinter import *

root = Tk()
root.geometry("330x150")
root.title("Vocetube")


def MAIN():
    link = str(ent.get())
    def show_progress(stream, chunk, file_handle, bytes_remaining):
        progress.step(int(file_handle.tell()*100/(file_handle.tell()+bytes_remaining)))
        progress.update()
    yt = pytube.YouTube(link)
    yt.register_on_progress_callback(show_progress)
    vids= yt.streams.filter(subtype='mp4',progressive=True).all()
    vids[1].download()
    progress["value"]=100
    progress.update()

def baixar():
    progress.after(2, MAIN)

lab = Label(root,text = "LINK: ")
lab.place(x=20,y=30)
ent = Entry(root,width=30)
ent.place(x=60,y=30)

but = Button(root, text = "Baixar",command = baixar)
but.place(x=20,y =60)

progress = ttk.Progressbar(root,length=300)
progress.place(x=20,y=100)

root.mainloop()
