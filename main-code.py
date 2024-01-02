import customtkinter as ctk
import pyperclip

#region Dictionary
o2 ={           0:29.274,
                100:29.538,
                200:29.931,                                                   
                300:30.400,
                400:30.878,
                500:31.334,
                600:31.761,
                700:32.150,
                800:32.502,
                900:32.825,
                1000:33.118,
                1100:33.386,
                1200:33.633,
                1300:33.863,
                1400:34.076,
                1500:34.282,
                1600:34.474,
                1700:34.658,
                1800:34.834,
                1900:35.006,
                2000:35.169,
                2100:35.328,
                2200:35.483,
                2300:35.634,
                2400:35.785,
                2500:35.927,
                2600:36.069,
                2700:36.207,
                2800:36.341,
                2900:36.509,
                3000:36.676}
n2 = {0:29.115,
                100:29.144,
                200:29.228,
                300:29.383,
                400:29.601,
                500:29.864,
                600:30.149,
                700:30.451,
                800:30.748,
                900:31.037,
                1000:31.313,
                1100:31.577,
                1200:31.828,
                1300:32.067,
                1400:32.293,
                1500:32.502,
                1600:32.699,
                1700:32.883,
                1800:33.055,
                1900:33.218,
                2000:33.373,
                2100:33.520,
                2200:33.658,
                2300:33.787,
                2400:33.909,
                2500:34.002,
                2600:34.206,
                2700:34.290,
                2800:34.415,
                2900:34.499,
                3000:34.583}
h2 = {0:28.617,
                100:28.935,
                200:29.073,
                300:29.123,
                400:29.186,
                500:29.249,
                600:29.316,
                700:29.408,
                800:29.517,
                900:29.647,
                1000:29.789,
                1100:29.944,
                1200:30.107,
                1300:30.287,
                1400:30.467,
                1500:30.647,
                1600:30.832,
                1700:31.012,
                1800:31.192,
                1900:31.372,
                2000:31.548,
                2100:31.723,
                2200:31.891,
                2300:32.058,
                2400:32.222,
                2500:32.385,
                2600:32.540,
                2700:32.691,
                2800:32.866,
                2900:33.034,
                3000:33.159}
h2o = {0:33.499,
                100:33.741,
                200:34.118,
                300:34.575,
                400:35.090,
                500:35.630,
                600:36.195,
                700:36.789,
                800:37.392,
                900:38.008,
                1000:38.619,
                1100:39.26,
                1200:39.825,
                1300:40.407,
                1400:40.976,
                1500:41.525,
                1600:42.056,
                1700:42.576,
                1800:43.070,
                1900:43.539,
                2000:43.995,
                2100:44.435,
                2200:44.853,
                2300:45.255,
                2400:45.644,
                2500:46.017,
                2600:46.381,
                2700:46.729,
                2800:47.060,
                2900:47.378,
                3000:""}
co2 = {0:35.860,
                100:38.112,
                200:40.059,
                300:41.755,
                400:43.250,
                500:44.573,
                600:45.753,
                700:46.813,
                800:47.763,
                900:48.617,
                1000:49.392,
                1100:50.099,
                1200:50.740,
                1300:51.322,
                1400:51.858,
                1500:52.348,
                1600:52.800,
                1700:53.218,
                1800:53.604,
                1900:53.959,
                2000:54.290,
                2100:54.596,
                2200:54.881,
                2300:55.144,
                2400:55.391,
                2500:55.617,
                2600:55.852,
                2700:56.061,
                2800:56.229,
                2900:56.438,
                3000:56.606}
co = {0:29.123,
                100:29.178,
                200:29.303,
                300:29.517,
                400:29.789,
                500:30.099,
                600:30.425,
                700:30.752,
                800:31.070,
                900:31.376,
                1000:31.665,
                1100:31.937,
                1200:32.192,
                1300:32.427,
                1400:32.653,
                1500:32.858,
                1600:33.051,
                1700:33.231,
                1800:33.402,
                1900:33.561,
                2000:33.708,
                2100:33.850,
                2200:33.980,
                2300:34.106,
                2400:34.223,
                2500:34.336,
                2600:34.499,
                2700:34.583,
                2800:34.667,
                2900:34.750,
                3000:34.834}
so2 = {0:38.854,
                100:40.654,
                200:42.329,
                300:43.878,
                400:45.217,
                500:46.390,
                600:47.353,
                700:48.232,
                800:48.944,
                900:49.614,
                1000:50.158,
                1100:50.660,
                1200:51.079,
                1300:51.623,
                1400:51.958,
                1500:52.251,
                1600:52.544,
                1700:52.796,
                1800:53.047,
                1900:53.214,
                2000:53.465,
                2100:53.633,
                2200:53.800,
                2300:53.968,
                2400:54.135,
                2500:54.261,
                2600:54.387,
                2700:54.512,
                2800:54.596,
                2900:54.721,
                3000:54.847}
ch1 = {0:34.738,
                100:36.806,
                200:39.427,
                300:42.274,
                400:45.180,
                500:47.977,
                600:50.673,
                700:53.277,
                800:55.902,
                900:58.330,
                1000:60.503,
                1100:62.454,
                1200:64.175}
c2h6 = {0:49.530,
                100:55.919,
                200:62.195,
                300:68.232,
                400:74.161,
                500:79.629,
                600:84.674,
                700:89.355,
                800:93.713,
                900:97.766,
                1000:101.526,
                1100:104.984,
                1200:108.162}
c2h8 = {0:68.329,
                100:78.670,
                200:88.886,
                300:97.929,
                400:106.680,
                500:114.174,
                600:121.752,
                700:128.284,
                800:134.229,
                900:141.765,
                1000:144.821,
                1100:149.678,
                1200:154.242}
c2h4 = {0:40.947,
                100:46.222,
                200:51.163,
                300:55.936,
                400:60.206,
                500:64.184,
                600:67.826,
                700:71.050,
                800:74.148,
                900:76.912,
                1000:79.507,
                1100:81.936,
                1200:84.113}
c2h2 = {0:41.910,
                100:45.871,
                200:48.517,
                300:50.677,
                400:52.536,
                500:54.160,
                600:55.638,
                700:56.999,
                800:58.268,
                900:59.444,
                1000:60.537,
                1100:61.571,
                1200:62.542}
c6h6 = {0:73.688,
                100:89.472,
                200:103.540,
                300:116.561,
                400:127.907,
                500:137.871,
                600:146.831,
                700:154.744,
                800:161.862,
                900:168.309,
                1000:174.171,
                1100:179.488,
                1200:184.261}
h2s = {0:33.787,
                100:34.332,
                200:35.002,
                300:35.755,
                400:36.593,
                500:37.430,
                600:38.309,
                700:39.147,
                800:39.984,
                900:40.738,
                1000:41.491,
                1100:42.203,
                1200:42.831}
c2h5oh = {0:70.087,
                100:77.288,
                200:83.903,
                300:90.477,
                400:96.464,
                500:101.990,
                600:107.140,
                700:111.788,
                800:116.100,
                900:120.077,
                1000:123.678,
                1100:127.111,
                1200:130.209}

mapiranje_rijecnika_plinova = {
    "o2": o2,
    "n2": n2,
    "ch1": ch1,
    "h2": h2,
    "h2o": h2o,
    "c2h2": c2h2,
    "c2h4": c2h4,
    "c2h5oh": c2h5oh,
    "c2h6": c2h6,
    "co": co,
    "c2h8": c2h8,
    "c6h6": c6h6,
    "co2": co2,
    "h2s": h2s,
    "so2": so2,
}


#endregion

#region List
lista_rijecnika_plinova = [o2,n2,ch1,h2,h2o,c2h2,c2h4,c2h5oh,c2h6,co,c2h8,c6h6,co2,h2s,so2]
#endregion

def izracunaj():
    next_lower = None
    next_higher = None
    
    global textbox_racunica_1
    global textbox_racunica_2
    global textbox_racunica_3
    global textbox_racunica_4
    global textbox_racunica_5
    global textbox_racunica_6
    
    textbox_racunica_1.delete("0.0","end")
    textbox_racunica_2.delete("0.0","end")
    textbox_racunica_3.delete("0.0","end")
    textbox_racunica_4.delete("0.0","end")
    textbox_racunica_5.delete("0.0","end")
    textbox_racunica_6.delete("0.0","end")
    
    unesena_temperatura = int(entry_temperatura.get())   #za temperaturu 
    
    unos_plina_1 = plin_entry_1.get().lower()  #rijeseno
    unos_plina_2 = plin_entry_2.get().lower()  #rijeseno
    unos_plina_3 = plin_entry_3.get().lower()  #rijeseno
    unos_plina_4 = plin_entry_4.get().lower()  #rijeseno
    unos_plina_5 = plin_entry_5.get().lower()  #rijeseno
    unos_plina_6 = plin_entry_6.get().lower()  #rijeseno
     
    if unos_plina_1 == "":
        pass
    
    elif unos_plina_1 in mapiranje_rijecnika_plinova:
        gas_dict = mapiranje_rijecnika_plinova[unos_plina_1]
        
        if unesena_temperatura in gas_dict:
            textbox_racunica_1.insert(1.0,text=f"{gas_dict[unesena_temperatura]}")    
        else:
            for key in sorted(gas_dict.keys()):
                if key <= unesena_temperatura:
                    next_lower = key
                    value_lower = gas_dict[next_lower]
                else:
                    next_higher = key
                    value_higher = gas_dict[next_higher]
                    break
            a = float(value_lower) + (float(value_higher)-float(value_lower))/(float(next_higher)-float(next_lower)) * (unesena_temperatura-float(next_lower))
            textbox_racunica_1.insert(1.0,text=a)         
    else:
        pass    
    
    if unos_plina_2 == "":
        pass
    elif unos_plina_2 in mapiranje_rijecnika_plinova:
        gas_dict = mapiranje_rijecnika_plinova[unos_plina_2]
        if unesena_temperatura in gas_dict:
            textbox_racunica_2.insert(1.0,text=f"{gas_dict[unesena_temperatura]}")
        else:
            for key in sorted(gas_dict.keys()):
                if key <= unesena_temperatura:
                    next_lower = key
                    value_lower = gas_dict[next_lower]
                else:
                    next_higher = key
                    value_higher = gas_dict[next_higher]
                    break
            b = float(value_lower) + (float(value_higher)-float(value_lower))/(float(next_higher)-float(next_lower)) * (unesena_temperatura-float(next_lower))
            textbox_racunica_2.insert(1.0,text=b)
    else:
        pass    
    
    if unos_plina_3 == "":
        pass
    elif unos_plina_3 in mapiranje_rijecnika_plinova:
        gas_dict = mapiranje_rijecnika_plinova[unos_plina_3]
        if unesena_temperatura in gas_dict:
            textbox_racunica_3.insert(1.0,text=f"{gas_dict[unesena_temperatura]}")
        else:
            for key in sorted(gas_dict.keys()):
                if key <= unesena_temperatura:
                    next_lower = key
                    value_lower = gas_dict[next_lower]
                else:
                    next_higher = key
                    value_higher = gas_dict[next_higher]
                    break
            c = float(value_lower) + (float(value_higher)-float(value_lower))/(float(next_higher)-float(next_lower)) * (unesena_temperatura-float(next_lower))
            textbox_racunica_3.insert(1.0,text=c)
    else:
        pass
    
    if unos_plina_4 == "":
        pass
    elif unos_plina_4 in mapiranje_rijecnika_plinova:
        gas_dict = mapiranje_rijecnika_plinova[unos_plina_4]
        if unesena_temperatura in gas_dict:
            textbox_racunica_4.insert(1.0,text=f"{gas_dict[unesena_temperatura]}")
        else:
            for key in sorted(gas_dict.keys()):
                if key <= unesena_temperatura:
                    next_lower = key
                    value_lower = gas_dict[next_lower]
                else:
                    next_higher = key
                    value_higher = gas_dict[next_higher]
                    break
            d = float(value_lower) + (float(value_higher)-float(value_lower))/(float(next_higher)-float(next_lower)) * (unesena_temperatura-float(next_lower))
            textbox_racunica_4.insert(1.0,text=d)
    else:
        pass
    
    if unos_plina_5 == "":
        pass
    elif unos_plina_5 in mapiranje_rijecnika_plinova:
        gas_dict = mapiranje_rijecnika_plinova[unos_plina_5]
        if unesena_temperatura in gas_dict:
            textbox_racunica_5.insert(1.0,text=f"{gas_dict[unesena_temperatura]}")
        else:
            for key in sorted(gas_dict.keys()):
                if key <= unesena_temperatura:
                    next_lower = key
                    value_lower = gas_dict[next_lower]
                else:
                    next_higher = key
                    value_higher = gas_dict[next_higher]
                    break
            e = float(value_lower) + (float(value_higher)-float(value_lower))/(float(next_higher)-float(next_lower)) * (unesena_temperatura-float(next_lower))
            textbox_racunica_5.insert(1.0,text=e)
    else:
        pass
    
    if unos_plina_6 == "":
        pass
    elif unos_plina_6 in mapiranje_rijecnika_plinova:
        gas_dict = mapiranje_rijecnika_plinova[unos_plina_6]
        if unesena_temperatura in gas_dict:
            textbox_racunica_6.insert(1.0,text=f"{gas_dict[unesena_temperatura]}")
        else:
            for key in sorted(gas_dict.keys()):
                if key <= unesena_temperatura:
                    next_lower = key
                    value_lower = gas_dict[next_lower]
                else:
                    next_higher = key
                    value_higher = gas_dict[next_higher]
                    break
            f = float(value_lower) + (float(value_higher)-float(value_lower))/(float(next_higher)-float(next_lower)) * (unesena_temperatura-float(next_lower))
            textbox_racunica_6.insert(1.0,text=f)
    else:
        pass
        
        
        
def izbrisi_sve_unesene_plinove():

    plin_entry_1.delete(0,"end")
    plin_entry_2.delete(0,"end")
    plin_entry_3.delete(0,"end")
    plin_entry_4.delete(0,"end")
    plin_entry_5.delete(0,"end")
    plin_entry_6.delete(0,"end")
    
    button_izracunaj.configure(state="normal")

def izbrisi_unos_plina_1():
    plin_entry_1.delete(0,"end")
 
def izbrisi_unos_plina_2():
    plin_entry_2.delete(0,"end")
    
def izbrisi_unos_plina_3():
    plin_entry_3.delete(0,"end")
    
def izbrisi_unos_plina_4():
    plin_entry_4.delete(0,"end")

def izbrisi_unos_plina_5():
    plin_entry_5.delete(0,"end")

def izbrisi_unos_plina_6():
    plin_entry_6.delete(0,"end")

def kopiraj_sve_izracune():
    first_copy = textbox_racunica_1.get("0.0","end")
    second_copy = textbox_racunica_2.get("0.0","end")
    third_copy = textbox_racunica_3.get("0.0","end")
    fourth_copy = textbox_racunica_4.get("0.0","end")
    fifth_copy = textbox_racunica_5.get("0.0","end")
    sixth_copy = textbox_racunica_6.get("0.0","end")
    
    long_string_of_copy = f"{first_copy}{second_copy}{third_copy}{fourth_copy}{fifth_copy}{sixth_copy}"
    pyperclip.copy(long_string_of_copy)

def kopiraj_izracune_plin_1():
    pyperclip.copy(textbox_racunica_1.get("0.0","end"))

def kopiraj_izracune_plin_2():
    pyperclip.copy(textbox_racunica_2.get("0.0","end"))

def kopiraj_izracune_plin_3():
    pyperclip.copy(textbox_racunica_3.get("0.0","end"))
    
def kopiraj_izracune_plin_4():
    pyperclip.copy(textbox_racunica_4.get("0.0","end"))

def kopiraj_izracune_plin_5():
    pyperclip.copy(textbox_racunica_5.get("0.0","end"))
    
def kopiraj_izracune_plin_6():
    pyperclip.copy(textbox_racunica_6.get("0.0","end"))



aplikacija = ctk.CTk()
aplikacija.geometry("1000x800+350+100")
aplikacija.resizable(False,False)


#region ENTRY

#these are the entries for entering wanted gas

plin_entry_1 = ctk.CTkEntry(aplikacija,placeholder_text="Unesite plin",width=200,height=40,corner_radius=0,font=("Times New Roman",18))

plin_entry_1.place(x=20,y=200)

plin_entry_2 = ctk.CTkEntry(aplikacija,placeholder_text="Unesite plin",width=200,height=40,corner_radius=0,font=("Times New Roman",18))

plin_entry_2.place(x=20,y=250)

plin_entry_3 = ctk.CTkEntry(aplikacija,placeholder_text="Unesite plin",width=200,height=40,corner_radius=0,font=("Times New Roman",18))

plin_entry_3.place(x=20,y=300)

plin_entry_4 = ctk.CTkEntry(aplikacija,placeholder_text="Unesite plin",width=200,height=40,corner_radius=0,font=("Times New Roman",18))

plin_entry_4.place(x=20,y=350)

plin_entry_5 = ctk.CTkEntry(aplikacija,placeholder_text="Unesite plin",width=200,height=40,corner_radius=0,font=("Times New Roman",18))

plin_entry_5.place(x=20,y=400)

plin_entry_6 = ctk.CTkEntry(aplikacija,placeholder_text="Unesite plin",width=200,height=40,corner_radius=0,font=("Times New Roman",18))

plin_entry_6.place(x=20,y=450)

#in this entry the user inputs the wanted temperature

entry_temperatura = ctk.CTkEntry(aplikacija,width=300,height=30,placeholder_text="Unesite temperaturu bez mjerne jedinice",font=("Times New Roman",18))

entry_temperatura.place(x=320,y=590)
#endregion
 

#region TEXTBOX
#these are the textbox widgets that receive wanted data and display them

textbox_racunica_1 = ctk.CTkTextbox(aplikacija,width=200,height=40,corner_radius=0,font=("Times New Roman",18))

textbox_racunica_1.place(x=670,y=200)

textbox_racunica_2 = ctk.CTkTextbox(aplikacija,width=200,height=40,corner_radius=0,font=("Times New Roman",18))

textbox_racunica_2.place(x=670,y=250)

textbox_racunica_3 = ctk.CTkTextbox(aplikacija,width=200,height=40,corner_radius=0,font=("Times New Roman",18))

textbox_racunica_3.place(x=670,y=300)

textbox_racunica_4 = ctk.CTkTextbox(aplikacija,width=200,height=40,corner_radius=0,font=("Times New Roman",18))

textbox_racunica_4.place(x=670,y=350)

textbox_racunica_5 = ctk.CTkTextbox(aplikacija,width=200,height=40,corner_radius=0,font=("Times New Roman",18))

textbox_racunica_5.place(x=670,y=400)

textbox_racunica_6 = ctk.CTkTextbox(aplikacija,width=200,height=40,corner_radius=0,font=("Times New Roman",18))

textbox_racunica_6.place(x=670,y=450)
#endregion
 

#region LABEL

#this is the label that tells the user where to input the wanted gas
label_plin = ctk.CTkLabel(aplikacija,text="UNOS PLINA:",font=("Times New Roman",24),corner_radius=0)
label_plin.place(x=20,y=160)

 

#this is the label that displays the apps headline (wanted by user)
label_naslov_aplikacije = ctk.CTkLabel(aplikacija,text="Srednji molarni toplinski kapacitet idealnih \nplinova između temperatura 0°C i ϑ°C",font=("Times New Roman",36))
label_naslov_aplikacije.place(x=200,y=0)

 

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

 
button_del_all = ctk.CTkButton(aplikacija,width=50,height=40,text="DEL ALL",font=("Times New Roman",20),corner_radius=0,fg_color="#EB4242",hover_color="#A76A6A",command=izbrisi_sve_unesene_plinove)
button_del_all.place(x=20,y=100)


button_delete_plin_1 = ctk.CTkButton(aplikacija,width=30,height=40,text="DEL",font=("Times New Roman",14),corner_radius=0,fg_color="#EB4242",hover_color="#A76A6A",command=izbrisi_unos_plina_1)
button_delete_plin_1.place(x=220,y=200)

 
button_delete_plin_2 = ctk.CTkButton(aplikacija,width=30,height=40,text="DEL",font=("Times New Roman",14),corner_radius=0,fg_color="#EB4242",hover_color="#A76A6A",command=izbrisi_unos_plina_2)
button_delete_plin_2.place(x=220,y=250)

 
button_delete_plin_3 = ctk.CTkButton(aplikacija,width=30,height=40,text="DEL",font=("Times New Roman",14),corner_radius=0,fg_color="#EB4242",hover_color="#A76A6A",command=izbrisi_unos_plina_3)
button_delete_plin_3.place(x=220,y=300)

 
button_delete_plin_4 = ctk.CTkButton(aplikacija,width=30,height=40,text="DEL",font=("Times New Roman",14),corner_radius=0,fg_color="#EB4242",hover_color="#A76A6A",command=izbrisi_unos_plina_4)
button_delete_plin_4.place(x=220,y=350)

 
button_delete_plin_5 = ctk.CTkButton(aplikacija,width=30,height=40,text="DEL",font=("Times New Roman",14),corner_radius=0,fg_color="#EB4242",hover_color="#A76A6A",command=izbrisi_unos_plina_5)
button_delete_plin_5.place(x=220,y=400)

 
button_delete_plin_6 = ctk.CTkButton(aplikacija,width=30,height=40,text="DEL",font=("Times New Roman",14),corner_radius=0,fg_color="#EB4242",hover_color="#A76A6A",command=izbrisi_unos_plina_6)
button_delete_plin_6.place(x=220,y=450)

 
button_copy_data = ctk.CTkButton(aplikacija,width=30,height=40,text="Copy All",font=("Times New Roman",24),corner_radius=0,fg_color="#218ED1",hover_color="#196DA0",command=kopiraj_sve_izracune)
button_copy_data.place(x=880,y=100)


button_copy_izracun_1 = ctk.CTkButton(aplikacija,width=30,height=40,text="COPY",font=("Times New Roman",14),corner_radius=0,fg_color="#218ED1",hover_color="#196DA0",command=kopiraj_izracune_plin_1)
button_copy_izracun_1.place(x=630,y=200)

 
button_copy_izracun_2 = ctk.CTkButton(aplikacija,width=30,height=40,text="COPY",font=("Times New Roman",14),corner_radius=0,fg_color="#218ED1",hover_color="#196DA0",command=kopiraj_izracune_plin_2)
button_copy_izracun_2.place(x=630,y=250)

 
button_copy_izracun_3 = ctk.CTkButton(aplikacija,width=30,height=40,text="COPY",font=("Times New Roman",14),corner_radius=0,fg_color="#218ED1",hover_color="#196DA0",command=kopiraj_izracune_plin_3)
button_copy_izracun_3.place(x=630,y=300)

 
button_copy_izracun_4 = ctk.CTkButton(aplikacija,width=30,height=40,text="COPY",font=("Times New Roman",14),corner_radius=0,fg_color="#218ED1",hover_color="#196DA0",command=kopiraj_izracune_plin_4)
button_copy_izracun_4.place(x=630,y=350)


button_copy_izracun_5 = ctk.CTkButton(aplikacija,width=30,height=40,text="COPY",font=("Times New Roman",14),corner_radius=0,fg_color="#218ED1",hover_color="#196DA0",command=kopiraj_izracune_plin_5)
button_copy_izracun_5.place(x=630,y=400)

 
button_copy_izracun_6 = ctk.CTkButton(aplikacija,width=30,height=40,text="COPY",font=("Times New Roman",14),corner_radius=0,fg_color="#218ED1",hover_color="#196DA0",command=kopiraj_izracune_plin_6)
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
