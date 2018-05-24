from tkinter import *
#import vlc
#p=vlc.MediaPlayer("aplausos.mp3")
tk = Tk()
tk.title("Game")
canvas = Canvas(tk, width=1024, height=680)
canvas.pack()
imagen1=PhotoImage(file="fondo.gif")
canvas.create_image(0,0, ancho=NW, image=imagen1)
imagen2=PhotoImage(file="arco.gif")
canvas.create_image(20,300, ancho=NW, image=imagen2)
imagen3=PhotoImage(file="balon.gif")
canvas.create_image(800,360, ancho=NW, image=imagen3)
def movetriangle(event):
    if event.keysym=='Left':
        canvas.move(3,-10,0)
    elif event.keysym=='Right':
        canvas.move(3,10,0)
canvas.bind_all('<KeyPress-Left>',movetriangle)
canvas.bind_all('<KeyPress-Right>',movetriangle)
#p.play()

tk.mainloop()
