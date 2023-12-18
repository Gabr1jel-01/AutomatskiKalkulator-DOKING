import customtkinter as ctk

import tkinter as tk

import os

 

o2_STMK_lista ={ 0,"35,860",

                100,"38,112",

                200,"40,059",

                300,"41,755",

                400,"43,250",

                500,"44,573",

                600,"45,753",

                700,"46,813",

                800,"47.763",

                900,"48,617",

                1000,"49,392",

                1100,"50,099",

                1200,"50,740",

                1300,"51,322",

                1400,"51,858",

                1500,"52,348",

                1600,"52,800",

                1700,"53,218",

                1800,"53,604",

                1900,"53,959",

                2000,"54,290",

                2100,"54,596",

                2200,"54,881",

                2300,"55,144",

                2400,"55,391",

                2500,"55,617",

                2600,"55,852",

                2700,"56,061",

                2800,"56,229",

                2900,"56,438",

                3000,"56,606",

                }

#dvije temp i koji plin i onda formula i izracun

 

def izracunaj():

    pass

 

def delete_all():

    entry_racunica.delete("0.0", "end")

    button_izracunaj.configure(state="normal")

 

aplikacija = ctk.CTk()

aplikacija.geometry("1000x800")

aplikacija.resizable(False,False)




"""

padajuci_izbornik_plin = ctk.CTkOptionMenu(aplikacija,font=("Times New Roman",24),corner_radius=0

                                           ,fg_color="#979797",button_color="#979797",button_hover_color="#5D5959",

                                           width=300,height=50,values=["O2","N2","H2","H2O","CO2","CO","SO2","CH1metan","C2H8propan","C2H4etilen","C2H2acetilen","C6H6benzen","H₂Ssumporovodik","C₂H5OHetilnialkohol"])

padajuci_izbornik_plin.place(x=50,y=40)

 

padajuci_izbornik_temperatura_1 = ctk.CTkOptionMenu(aplikacija,font=("Times New Roman",24),button_hover_color="#5D5959",button_color="#979797",corner_radius=0,width=200,height=50,values=["0°C","100°C","200°C","300°C","400°C","500°C","600°C","700°C","800°C","900°C","1000°C","1100°C","1200°C",

                                                                                         "1300°C","1400°C","1500°C","1600°C","1700°C","1800°C","1900°C","2000°C","2100°C","2200°C","2300°C","2400°C",

                                                                                         "2500°C","2600°C","2700°C","2800°C","2900°C","3000°C"],fg_color="#979797")

padajuci_izbornik_temperatura_1.place(x=50,y=160)

 

padajuci_izbornik_temperatura_2 = ctk.CTkOptionMenu(aplikacija,font=("Times New Roman",24),button_hover_color="#5D5959",button_color="#979797",corner_radius=0,width=200,height=50,values=["0°C","100°C","200°C","300°C","400°C","500°C","600°C","700°C","800°C","900°C","1000°C","1100°C","1200°C",

                                                                                         "1300°C","1400°C","1500°C","1600°C","1700°C","1800°C","1900°C","2000°C","2100°C","2200°C","2300°C","2400°C",

                                                                                         "2500°C","2600°C","2700°C","2800°C","2900°C","3000°C"],fg_color="#979797")

padajuci_izbornik_temperatura_2.place(x=50,y=260)

"""

 

#region ENRTY

 

#these are the entries for entering wanted gas

plin_entry_1 = ctk.CTkEntry(aplikacija,placeholder_text="Unesite plin",width=200,height=40,corner_radius=0)

plin_entry_1.place(x=20,y=200)

plin_entry_2 = ctk.CTkEntry(aplikacija,placeholder_text="Unesite plin",width=200,height=40,corner_radius=0)

plin_entry_2.place(x=20,y=250)

plin_entry_3 = ctk.CTkEntry(aplikacija,placeholder_text="Unesite plin",width=200,height=40,corner_radius=0)

plin_entry_3.place(x=20,y=300)

plin_entry_4 = ctk.CTkEntry(aplikacija,placeholder_text="Unesite plin",width=200,height=40,corner_radius=0)

plin_entry_4.place(x=20,y=350)

plin_entry_5 = ctk.CTkEntry(aplikacija,placeholder_text="Unesite plin",width=200,height=40,corner_radius=0)

plin_entry_5.place(x=20,y=400)

plin_entry_6 = ctk.CTkEntry(aplikacija,placeholder_text="Unesite plin",width=200,height=40,corner_radius=0)

plin_entry_6.place(x=20,y=450)

 

#these are the entries that receive wanted data and display them

entry_racunica_1 = ctk.CTkTextbox(aplikacija,width=200,height=40,corner_radius=0)

entry_racunica_1.place(x=670,y=200)

entry_racunica_2 = ctk.CTkTextbox(aplikacija,width=200,height=40,corner_radius=0)

entry_racunica_2.place(x=670,y=250)

entry_racunica_3 = ctk.CTkTextbox(aplikacija,width=200,height=40,corner_radius=0)

entry_racunica_3.place(x=670,y=300)

entry_racunica_4 = ctk.CTkTextbox(aplikacija,width=200,height=40,corner_radius=0)

entry_racunica_4.place(x=670,y=350)

entry_racunica_5 = ctk.CTkTextbox(aplikacija,width=200,height=40,corner_radius=0)

entry_racunica_5.place(x=670,y=400)

entry_racunica_6 = ctk.CTkTextbox(aplikacija,width=200,height=40,corner_radius=0)

entry_racunica_6.place(x=670,y=450)

 

#in this entry the user inputs the wanted temperature

entry_temperatura = ctk.CTkEntry(aplikacija,width=300,height=30,placeholder_text="Unesite temperaturu bez mjerne jedinice")

entry_temperatura.place(x=320,y=590)

 

#endregion

 

#region LABEL

 

#this is the label that tells the user where to input the wanted gas

label_plin = ctk.CTkLabel(aplikacija,text="UNOS PLINA:",font=("Times New Roman",24),corner_radius=0)

label_plin.place(x=20,y=160)

 

#this is the label that displays the apps headline (wanted by user)

label_naslov_aplikacije = ctk.CTkLabel(aplikacija,text="Srednji molarni toplinski kapacitet idealnih \nplinova između temperatura 0°C i ϑ°C",font=("Bookman Old Style",36))

label_naslov_aplikacije.place(x=120,y=0)

 

#this is the label that tells the user where to input the wanted temperature

label_temperatura = ctk.CTkLabel(aplikacija,text="TEMPERATURA:",font=("Times New Roman",24),corner_radius=0)

label_temperatura.place(x=390,y=550)

 

#this label is used to display celsius sign

label_celzijus_za_entry = ctk.CTkLabel(aplikacija,text="°C",font=("Times New Roman",26))

label_celzijus_za_entry.place(x=630,y=590)

 

#this label is used to display gases measure unit

label_mjerna_jedinica_1 = ctk.CTkLabel(aplikacija,text="KJ/KmolK",font=("Times New Roman",24))

label_mjerna_jedinica_1.place(x=890,y=200)

 

#this label is used to display gases measure unit

label_mjerna_jedinica_2 = ctk.CTkLabel(aplikacija,text="KJ/KmolK",font=("Times New Roman",24))

label_mjerna_jedinica_2.place(x=890,y=250)

 

#this label is used to display gases measure unit

label_mjerna_jedinica_3 = ctk.CTkLabel(aplikacija,text="KJ/KmolK",font=("Times New Roman",24))

label_mjerna_jedinica_3.place(x=890,y=300)

 

#this label is used to display gases measure unit

label_mjerna_jedinica_4 = ctk.CTkLabel(aplikacija,text="KJ/KmolK",font=("Times New Roman",24))

label_mjerna_jedinica_4.place(x=890,y=350)

 

#this label is used to display gases measure unit

label_mjerna_jedinica_5 = ctk.CTkLabel(aplikacija,text="KJ/KmolK",font=("Times New Roman",24))

label_mjerna_jedinica_5.place(x=890,y=400)

 

#this label is used to display gases measure unit

label_mjerna_jedinica_6 = ctk.CTkLabel(aplikacija,text="KJ/KmolK",font=("Times New Roman",24))

label_mjerna_jedinica_6.place(x=890,y=450)

 

#endregion

 

#region BUTTON

button_izracunaj = ctk.CTkButton(aplikacija,width=100,height=50,text="Izračunaj",command=izracunaj,corner_radius=0,fg_color="#979797",hover_color = "#5D5959")

button_izracunaj.place(x=420,y=680)

 

button_del_all = ctk.CTkButton(aplikacija,width=50,height=40,text="DEL ALL",font=("Times New Roman",20),corner_radius=0,fg_color="#EB4242",hover_color="#A76A6A")

button_del_all.place(x=20,y=100)

 

button_delete_plin_1 = ctk.CTkButton(aplikacija,width=30,height=40,text="DEL",font=("Times New Roman",14),corner_radius=0,fg_color="#EB4242",hover_color="#A76A6A")

button_delete_plin_1.place(x=220,y=200)

 

button_delete_plin_2 = ctk.CTkButton(aplikacija,width=30,height=40,text="DEL",font=("Times New Roman",14),corner_radius=0,fg_color="#EB4242",hover_color="#A76A6A")

button_delete_plin_2.place(x=220,y=250)

 

button_delete_plin_3 = ctk.CTkButton(aplikacija,width=30,height=40,text="DEL",font=("Times New Roman",14),corner_radius=0,fg_color="#EB4242",hover_color="#A76A6A")

button_delete_plin_3.place(x=220,y=300)

 

button_delete_plin_4 = ctk.CTkButton(aplikacija,width=30,height=40,text="DEL",font=("Times New Roman",14),corner_radius=0,fg_color="#EB4242",hover_color="#A76A6A")

button_delete_plin_4.place(x=220,y=350)

 

button_delete_plin_5 = ctk.CTkButton(aplikacija,width=30,height=40,text="DEL",font=("Times New Roman",14),corner_radius=0,fg_color="#EB4242",hover_color="#A76A6A")

button_delete_plin_5.place(x=220,y=400)

 

button_delete_plin_6 = ctk.CTkButton(aplikacija,width=30,height=40,text="DEL",font=("Times New Roman",14),corner_radius=0,fg_color="#EB4242",hover_color="#A76A6A")

button_delete_plin_6.place(x=220,y=450)

 

button_copy_data = ctk.CTkButton(aplikacija,width=30,height=40,text="Copy All",font=("Times New Roman",24),corner_radius=0,fg_color="#218ED1",hover_color="#196DA0")

button_copy_data.place(x=880,y=100)




button_copy_izracun_1 = ctk.CTkButton(aplikacija,width=30,height=40,text="COPY",font=("Times New Roman",14),corner_radius=0,fg_color="#218ED1",hover_color="#196DA0")

button_copy_izracun_1.place(x=630,y=200)

 

button_copy_izracun_2 = ctk.CTkButton(aplikacija,width=30,height=40,text="COPY",font=("Times New Roman",14),corner_radius=0,fg_color="#218ED1",hover_color="#196DA0")

button_copy_izracun_2.place(x=630,y=250)

 

button_copy_izracun_3 = ctk.CTkButton(aplikacija,width=30,height=40,text="COPY",font=("Times New Roman",14),corner_radius=0,fg_color="#218ED1",hover_color="#196DA0")

button_copy_izracun_3.place(x=630,y=300)

 

button_copy_izracun_4 = ctk.CTkButton(aplikacija,width=30,height=40,text="COPY",font=("Times New Roman",14),corner_radius=0,fg_color="#218ED1",hover_color="#196DA0")

button_copy_izracun_4.place(x=630,y=350)

 

button_copy_izracun_5 = ctk.CTkButton(aplikacija,width=30,height=40,text="COPY",font=("Times New Roman",14),corner_radius=0,fg_color="#218ED1",hover_color="#196DA0")

button_copy_izracun_5.place(x=630,y=400)

 

button_copy_izracun_6 = ctk.CTkButton(aplikacija,width=30,height=40,text="COPY",font=("Times New Roman",14),corner_radius=0,fg_color="#218ED1",hover_color="#196DA0")

button_copy_izracun_6.place(x=630,y=450)

 

#endregion

 

#region FRAME

frame_line_1 = ctk.CTkFrame(aplikacija,width=360,height=3,fg_color="black")

frame_line_1.place(x=260,y=215)

 

frame_line_2 = ctk.CTkFrame(aplikacija,width=360,height=3,fg_color="black")

frame_line_2.place(x=260,y=265)

 

frame_line_3 = ctk.CTkFrame(aplikacija,width=360,height=3,fg_color="black")

frame_line_3.place(x=260,y=315)

 

frame_line_4 = ctk.CTkFrame(aplikacija,width=360,height=3,fg_color="black")

frame_line_4.place(x=260,y=365)

 

frame_line_5 = ctk.CTkFrame(aplikacija,width=360,height=3,fg_color="black")

frame_line_5.place(x=260,y=415)

 

frame_line_6 = ctk.CTkFrame(aplikacija,width=360,height=3,fg_color="black")

frame_line_6.place(x=260,y=465)

 

frame_line_7 = ctk.CTkFrame(aplikacija,width=200,height=3,fg_color="black")

frame_line_7.place(x=115,y=605)

 

frame_line_8 = ctk.CTkFrame(aplikacija,width=3,height=105,fg_color="black")

frame_line_8.place(x=116,y=503)

#endregion



aplikacija.mainloop()