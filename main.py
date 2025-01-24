import tkinter

window = tkinter.Tk()
window.minsize(width=400,height=300)
window.title("BMI Checker")
FONT = ("arial",10,"bold")

metin1 = tkinter.Label(text="lütfen boyunuz girin(m):",font=FONT)
metin1.place(x=150,y=20)

#enrty1
my_entry1 = tkinter.Entry(width=30)
my_entry1.place(x=120,y=40)


#my_entry1.update()
#print(my_entry1.winfo_width())
#print(my_entry1.winfo_height())



metin2 = tkinter.Label(text="lütfen kilonuzu girin(kg):",font=FONT)
metin2.place(x=150,y=75)


#enrty2
my_entry2 = tkinter.Entry(width=30)
my_entry2.place(x=120,y=105)

#my_entry1.update()
#print(my_entry1.winfo_width())
#print(my_entry1.winfo_height())

def hesapla_entry():
    try:
        sayi1 = float(my_entry1.get())
        sayi2 = float(my_entry2.get())
        sonuc = round(sayi2 / sayi1 **2,1)
        sayi_hesapla = tkinter.Label(text="vücüt kitle endeksiniz {}".format(sonuc),font=FONT)
        sayi_hesapla.place(x=110,y=160)
        print(sonuc)

        if sonuc < 18.5:
            my_indeks= tkinter.Label(text="vücut kitle endeksine göre zayıfsınız",font=FONT)
            my_indeks.place(x=80,y=185)
        elif 18.5 < sonuc < 24.9:
            my_indeks = tkinter.Label(text="vücut kitle endeksine göre normal kilodasınız",font=FONT)
            my_indeks.place(x=80, y=185)
        elif 25 < sonuc < 29.9:
            my_indeks = tkinter.Label(text="vücut kitle endeksine göre fazla kilolusunuz",font=FONT)
            my_indeks.place(x=80, y=185)

        elif 30 < sonuc < 34.9:
            my_indeks = tkinter.Label(text="vücut kitle endeksine göre 1.derece obezsiniz",font=FONT)
            my_indeks.place(x=80, y=185)
        elif 35 < sonuc < 39.9:
            my_indeks = tkinter.Label(text="vücut kitle endeksine göre 2.derece obezsiniz",font=FONT)
            my_indeks.place(x=80, y=185)
        elif 40 < sonuc :
            my_indeks = tkinter.Label(text="vücut kitle endeksine göre 3.derece obezsiniz",font=FONT)
            my_indeks.place(x=80, y=185)

    except:
        my_label = tkinter.Label(text="Bir yerde hata yaptınız lütfen hatayı düzeltin !!",font=FONT)
        my_label.place(x=80,y=0)

my_button = tkinter.Button(text="Hesapla",command = hesapla_entry)
my_button.place(x=180,y=140)



window.mainloop()
