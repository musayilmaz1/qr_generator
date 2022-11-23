from PIL import ImageTk, Image

from main import olustur
import tkinter as tk
from PIL import Image

ekran = tk.Tk()
ekran.resizable(width=True, height=True)
ekran.geometry("800x800")

frame_ust = tk.Frame(master=ekran, bg="red")
frame_ust.place(relheight=1, relwidth=1)
baslik = tk.Label(text="QR CODE GENRATOR", master=frame_ust, font=50)
baslik.place(relx=0.36)

soru = tk.Label(
    master=frame_ust,
    text="qr koda cevirmek istediğiniz metin veya linki giriniz",
    width=50,
    bg="red",
    font=40
)
soru.pack(padx=10, pady=30)

giris = tk.Entry(
    master=frame_ust,
    width=50,
    font=50
)
giris.pack(padx=150, pady=10)




def goster():
    load = Image.open("qr.jpg")
    render = ImageTk.PhotoImage(load)
    img = tk.Label(frame_ust, image=render)
    img.place(x=100, y=250)
    frame_ust.mainloop()


def gonder():
    deger = giris.get()
    olustur(deger)
def indir():
    qr_image=Image.open("qr.jpg")
    qr_image.save("C:\qr\qrcode.jpg")
    qr_image.show()






dugme = tk.Button(frame_ust, text="QR KOD OLUSTUR", command=gonder)
dugme.pack(pady=20)

dugme = tk.Button(frame_ust, text="QR KODU GÖSTER", command=goster)
dugme.pack()
indir=tk.Button(frame_ust,text="QR KODU INDIR",command=indir)
indir.place(relx=1,rely=1,anchor="se")

ekran.update()
ekran.mainloop()
