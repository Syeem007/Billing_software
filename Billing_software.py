from tkinter import *
import math ,random
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg="black",fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        #.............variables.................
        #cosmetics
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.gel=IntVar()
        self.loshan=IntVar()
        self.shampoo=IntVar()
        #grocery
        self.rice=IntVar()
        self.oil=IntVar()
        self.food=IntVar()
        self.daal=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()
        #cold_drinks
        self.maza=IntVar()
        self.coke=IntVar()
        self.frooti=IntVar()
        self.thumbsup=IntVar()
        self.limca=IntVar()
        self.sprite=IntVar()

        #total product price and Tax variable

        self.cosmetic_price=StringVar()
        self.grocery_price = StringVar()
        self.cold_drink_price = StringVar()

        self.cosmetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drink_tax = StringVar()


        #....customer

        self.c_name=StringVar()
        self.c_phone = StringVar()
        self.c_bill_no = StringVar()
        x=random.randint(1000,9999)
        self.c_bill_no.set(str(x))
        self.search_bill = StringVar()

        #customer_details
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg="black")
        F1.place(x=0,y=80,relwidth=1)
        cname_lbl=Label(F1,text="Customer Name",bg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=5,pady=5)
        cname_text=Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)

        cphn_lbl = Label(F1, text="Phone Number", bg="white", font=("times new roman", 18, "bold")).grid(row=0,column=2,padx=5,pady=5)
        cname_text = Entry(F1, width=15, textvariable=self.c_phone,font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=5)

        c_bill_lbl = Label(F1, text="Bill Number", bg="white", font=("times new roman", 18, "bold")).grid(row=0,column=4,padx=5,pady=5)
        c_bill_text = Entry(F1, width=15,textvariable=self.search_bill ,font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=5, padx=10, pady=5)

        bill_btn=Button(F1,text="Search",width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=10,pady=10)

        #...............cosmetics..................................

        F2 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Cosmetics", font=("times new roman", 15, "bold"),fg="gold", bg="black")
        F2.place(x=5, y=180, width=325,height=380)

        bath_lbl=Label(F2,text="Bath soap",font=("times new roman",16,"bold"),bg="white",fg="Black").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F2,width=10,textvariable=self.soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        Face_cream_lbl = Label(F2, text="Face Cream", font=("times new roman", 16, "bold"), bg="white", fg="Black").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Face_cream_lbl = Entry(F2, width=10, textvariable=self.face_cream,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1,padx=10, pady=10)

        Face_wash_lbl = Label(F2, text="Face wash", font=("times new roman", 16, "bold"), bg="white", fg="Black").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Face_wash_txt = Entry(F2, width=10, textvariable=self.face_wash,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1,padx=10, pady=10)

        Hair_S_lbl = Label(F2, text="Hair Shampoo", font=("times new roman", 16, "bold"), bg="white", fg="Black").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Hair_S_txt = Entry(F2, width=10, textvariable=self.shampoo,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1,padx=10, pady=10)

        Hair_G_lbl = Label(F2, text="Hair Gel", font=("times new roman", 16, "bold"), bg="white", fg="Black").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Hair_G_txt = Entry(F2, width=10, textvariable=self.gel,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1,padx=10, pady=10)

        Body_lbl = Label(F2, text="Body lotion", font=("times new roman", 16, "bold"), bg="white", fg="Black").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        Body_txt = Entry(F2, width=10,textvariable=self.loshan ,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        # ...............grocery..................................

        F3 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Grocery", font=("times new roman", 15, "bold"),fg="gold", bg="black")
        F3.place(x=340, y=180, width=325, height=380)

        g1_lbl = Label(F3, text="Rice", font=("times new roman", 16, "bold"), bg="white", fg="Black").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        g1_txt = Entry(F3, width=10,textvariable=self.rice ,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1,padx=10, pady=10)

        g2_lbl = Label(F3, text="oil", font=("times new roman", 16, "bold"), bg="white",fg="Black").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        g2_txt = Entry(F3, width=10,textvariable=self.oil ,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        g3_lbl = Label(F3, text="Daal", font=("times new roman", 16, "bold"), bg="white", fg="Black").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        g3_txt = Entry(F3, width=10,textvariable=self.daal ,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        g4_lbl = Label(F3, text="Wheat", font=("times new roman", 16, "bold"), bg="white", fg="Black").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        g4_txt = Entry(F3, width=10,textvariable=self.food ,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        g5_lbl = Label(F3, text="Sugar", font=("times new roman", 16, "bold"), bg="white", fg="Black").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        g5_txt = Entry(F3, width=10,textvariable=self.sugar ,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        g6_lbl = Label(F3, text="tea", font=("times new roman", 16, "bold"), bg="white", fg="Black").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        g6_txt = Entry(F3, width=10,textvariable=self.tea ,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1,padx=10, pady=10)

        # ..............Drinks..................................

        F4 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Drinks", font=("times new roman", 15, "bold"),fg="gold", bg="black")
        F4.place(x=675, y=180, width=325, height=380)

        D1_lbl = Label(F4, text="Maza", font=("times new roman", 16, "bold"), bg="white", fg="Black").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        D1_txt = Entry(F4, width=10,textvariable=self.maza ,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1,padx=10, pady=10)
        D2_lbl = Label(F4, text="Coke", font=("times new roman", 16, "bold"), bg="white",fg="Black").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        D2_txt = Entry(F4, width=10,textvariable=self.coke ,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
        D3_lbl = Label(F4, text="Frooti", font=("times new roman", 16, "bold"), bg="white", fg="Black").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        D3_txt = Entry(F4, width=10,textvariable=self.frooti ,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        D4_lbl = Label(F4, text="Thumbs up", font=("times new roman", 16, "bold"), bg="white", fg="Black").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        D4_txt = Entry(F4, width=10,textvariable=self.thumbsup ,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        D5_lbl = Label(F4, text="Limca", font=("times new roman", 16, "bold"), bg="white", fg="Black").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        D5_txt = Entry(F4, width=10,textvariable=self.limca ,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
        D6_lbl = Label(F4, text="Sprite", font=("times new roman", 16, "bold"), bg="white", fg="Black").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        D6_txt = Entry(F4, width=10, textvariable=self.sprite,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1,padx=10, pady=10)


        #...........Bill_Area............

        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1010,y=180,width=340,height=380)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        #self.txtarea.pack(fill=BOTH,expand=1)
        self.txtarea.pack()


        #........Button Frame......

        F6 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Bill Frame", font=("times new roman", 15, "bold"), fg="gold", bg="black")
        F6.place(x=0, y=560, relwidth=1, height=140)

        m1=Label(F6,text="Total cosmetics price",bg="white", fg="Black",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1=Entry(F6,width=18,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2 = Label(F6, text="Total Grocery price", bg="white", fg="Black", font=("times new roman", 14, "bold")).grid(row=1, column=0, padx=20, pady=1, sticky="w")
        m2 = Entry(F6, width=18,textvariable=self.grocery_price ,font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=1)

        m3 = Label(F6, text="Total cold drinks price", bg="white", fg="Black", font=("times new roman", 14, "bold")).grid(row=2, column=0, padx=20, pady=1, sticky="w")
        m3 = Entry(F6, width=18,textvariable=self.cold_drink_price ,font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)

        #.................
        c_m1 = Label(F6, text="cosmetics Tax", bg="white", fg="Black", font=("times new roman", 14, "bold")).grid(row=0, column=2, padx=20, pady=1, sticky="w")
        c_m1 = Entry(F6, width=18,textvariable=self.cosmetic_tax ,font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=1)

        c_m2 = Label(F6, text="Grocery Tax", bg="white", fg="Black", font=("times new roman", 14, "bold")).grid(row=1, column=2, padx=20, pady=1, sticky="w")
        c_m2 = Entry(F6, width=18,textvariable=self.grocery_tax ,font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=3, padx=10, pady=1)

        c_m3= Label(F6, text="cold Tax", bg="white", fg="Black",font=("times new roman", 14, "bold")).grid(row=2, column=2, padx=20, pady=1, sticky="w")
        c_m3 = Entry(F6, width=18,textvariable=self.cold_drink_tax ,font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2, column=3, padx=10, pady=1)

        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=740,width=580,height=105)

        total_btn=Button(btn_F,command=self.total,text="Total",bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 12 bold").grid(row=0,column=0,padx=5,pady=5)
        G_B_btn = Button(btn_F, text="Generate Bill",command=self.bill_area,bg="cadetblue", fg="white",bd=2, pady=15, width=10,font="arial 12 bold").grid(row=0, column=1, padx=5, pady=5)
        clear_btn = Button(btn_F, text="Clear", bg="cadetblue", fg="white", bd=2,pady=15, width=10,font="arial 12 bold").grid(row=0, column=2, padx=5, pady=5)
        exit_btn=Button(btn_F,text="Exit",bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 12 bold").grid(row=0,column=3,padx=5,pady=5)
        self.wellcome_bill()
    def total(self):
        self.a=(self.soap.get()*120)
        self.b=(self.face_cream.get() * 140)
        self.c=(self.face_wash.get() * 40)
        self.d=(self.loshan.get() * 40)
        self.e=(self.gel.get() * 40)
        self.f=(self.shampoo.get() * 40)
        self.total_cosmetics_price=float(
            self.a+
            self.b+
            self.c+
            self.d+
            self.e+
            self.f
            )
        self.cosmetic_price.set("Tk."+str(self.total_cosmetics_price))
        self.cosmetic_tax.set("Tk." + str(self.total_cosmetics_price*0.05))
        self.g=(self.rice.get() * 20)
        self.h= (self.daal.get() * 10)
        self.i=(self.sugar.get() * 5)
        self.j=(self.food.get() * 4)
        self.k=(self.tea.get() * 40)
        self.l=(self.oil.get() * 80)
        self.total_grocery_price = float(
             self.g+
             self.h+
             self.i+
             self.j+
             self.k+
             self.l
            )
        self.grocery_price.set("Tk."+str(self.total_grocery_price))
        self.grocery_tax.set("Tk." + str(self.total_grocery_price*.3))
        self.m=(self.maza.get() * 2)
        self.n=(self.coke.get() * 10)
        self.o=(self.frooti.get() * 15)
        self.p=(self.thumbsup.get() * 14)
        self.q=(self.limca.get() * 4)
        self.r=(self.sprite.get() * 8)
        self.total_drinks_price = float(
             self.m+
             self.n+
             self.o+
             self.p+
             self.q+
             self.r
        )
        self.cold_drink_price.set("Tk."+str(self.total_drinks_price))
        self.cold_drink_tax.set("Tk." + str(self.total_drinks_price*.4))

    def wellcome_bill(self):
        self.txtarea.delete("1.0",END)
        self.txtarea.insert(END,"\t Welcome webcode Retail\n")
        self.txtarea.insert(END, f"\n Bill Number:{self.c_bill_no.get()} ")
        self.txtarea.insert(END, f"\n Customer Name: {self.c_name.get()}")
        self.txtarea.insert(END, f"\n Phone Number:{self.c_phone.get()}")
        self.txtarea.insert(END, f"\n===================================")
        self.txtarea.insert(END, f"\n Products\t\tQTY\tPrice")
        self.txtarea.insert(END, f"\n===================================")
    def bill_area(self):
            self.wellcome_bill()
            #cosmetics
            if self.soap.get() !=0:
                self.txtarea.insert(END,f"\n Bath Soap\t\t{self.soap.get()}\t\t{self.a}")
            if self.face_cream.get() !=0:
                self.txtarea.insert(END,f"\n Face cream\t\t{self.face_cream.get()}\t\t{self.b}")
            if self.face_wash.get() !=0:
                self.txtarea.insert(END,f"\n Face wash\t\t{self.face_wash.get()}\t\t{self.c}")
            if self.shampoo.get() !=0:
                self.txtarea.insert(END,f"\n Shampoo\t\t{self.shampoo.get()}\t\t{self.d}")
            if self.gel.get() !=0:
                self.txtarea.insert(END,f"\n Gel \t\t{self.gel.get()}\t\t{self.e}")
            if self.loshan.get() !=0:
                self.txtarea.insert(END,f"\n Lotion \t\t{self.loshan.get()}\t\t{self.f}")
            #grocery
            if self.rice.get() !=0:
                self.txtarea.insert(END,f"\n Bath Soap\t\t{self.rice.get()}\t\t{self.g}")
            if self.oil.get() !=0:
                self.txtarea.insert(END,f"\n Face cream\t\t{self.oil.get()}\t\t{self.h}")
            if self.daal.get() !=0:
                self.txtarea.insert(END,f"\n Face wash\t\t{self.daal.get()}\t\t{self.i}")
            if self.food.get() !=0:
                self.txtarea.insert(END,f"\n Shampoo\t\t{self.food.get()}\t\t{self.j}")
            if self.sugar.get() !=0:
                self.txtarea.insert(END,f"\n Gel \t\t{self.sugar.get()}\t\t{self.k}")
            if self.tea.get() !=0:
                self.txtarea.insert(END,f"\n Lotion \t\t{self.tea.get()}\t\t{self.l}")
            # drinks
            if self.maza.get() !=0:
                self.txtarea.insert(END,f"\n Bath Soap\t\t{self.maza.get()}\t\t{self.m}")
            if self.coke.get() !=0:
                self.txtarea.insert(END,f"\n Face cream\t\t{self.coke.get()}\t\t{self.n}")
            if self.frooti.get() !=0:
                self.txtarea.insert(END,f"\n Face wash\t\t{self.frooti.get()}\t\t{self.o}")
            if self.thumbsup.get() !=0:
                self.txtarea.insert(END,f"\n Shampoo\t\t{self.thumbsup.get()}\t\t{self.p}")
            if self.limca.get() !=0:
                self.txtarea.insert(END,f"\n Gel \t\t{self.limca.get()}\t\t{self.q}")
            if self.sprite.get() !=0:
                self.txtarea.insert(END,f"\n Lotion \t\t{self.sprite.get()}\t\t{self.r}")

            self.txtarea.insert(END, f"\n-----------------------------------")
            if self.cosmetic_tax.get()!="0.0":
                self.txtarea.insert(END, f"\n Cosmetic Tax \t\t{self.cosmetic_tax.get()}")
            self.txtarea.insert(END, f"\n----------------------------------- ")

            



root=Tk()
obj=Bill_App(root)
root.mainloop()


