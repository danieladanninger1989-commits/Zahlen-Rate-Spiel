import random  #modul importieren
import tkinter as tk


# zufällige zahlen generieren
random.seed()
a = random.randint(1, 50)
b = random.randint(1,50)
c = a + b

# Versuche zählen
versuch_counter = 0
max_versuche = 100

#Fenster erstellen
fenster = tk.Tk()
fenster.resizable(True, True)
fenster.minsize(400, 500)
fenster.title("Zahlenrate Spiel")
fenster.geometry("500x600")

#Begrüßungstext
label_title = tk.Label(fenster, text="Zahlenrate Spiel", fg="#7b2cbf", bg="#f5f0ff", font=("Segoe UI", 20, "bold"))
label_title.pack(pady=(25,15)) 

# Subtitle - Die aufgabe anzeigen
subtitle = tk.Label(fenster, text=f"viel Spass! Die Aufgabe ist: {a} + {b}", fg="#6a1b9a", bg="#f5f0ff", font=("Segoe UI", 11))
subtitle.pack(padx=(0,10))

#Label für Anweisungen
anweisung_label = tk.Label(fenster, text= "Gib deine Lösung ein und klicke auf Prüfen", fg="#333333", bg="#f5f0ff", font=("Segoe UI", 14))
anweisung_label.pack(pady=(20, 10))

#Eingabefeld für Zahlen

eingabe_feld = tk.Entry(fenster, font=("Segoe.UI", 14), width=20, justify="center")
eingabe_feld.pack(pady=20)

#Label für Feedback (Richtung/Falsch)

feedback_label = tk.Label(fenster, text="",fg="#423F3F", bg="#f5f0ff", font=("Segoe UI", 14, "bold"))
feedback_label.pack(pady=20)

#label für versuchsanzeige
versuch_label = tk.Label(fenster, text="Versuche: 0", fg="#555555", bg="#f5f0ff", font=("Segoe UI", 11))
versuch_label.pack(pady=10)

# Funktion die aufgerufen wird wenn der Button gedrückt wird
def pruefe_eingabe():
    global versuch_counter, a,b, c, subtitle, ergebnis_label

    #pfrüfen ob maximale verrsuche erreicht
    if versuch_counter >= max_versuche:
        feedback_label.config(text=f"Maximale Anzahl Vresuche erreicht", fg="red")
        return
    
    try:
        #eingabe holen und in Zahl umwandeln
        zahl = int(eingabe_feld.get())
        print(f"Eingabe: {zahl}, Ergebnis: {c}, Gleich? {zahl == c}")
        versuch_counter += 1

        #Prüfen ob richtig oder falsch
        if zahl == c:
           feedback_label.config(text=f"Ergebnis Richtig", fg="green")
           #optional: Butten deaktivieren nach richtigem Ergebnis

           #neue Aufgabe Generieren
           a = random.randint(1, 50)
           b = random.randint(1, 50)
           c = a + b
           print(f"Neue Zahlen: {a} + {b} = {c}")

           #Aufgabe im Fenster Aktualisieren
           subtitle.config(text=f"Neue Aufgabe: {a} + {b}")
           print(f"Subtitle sollte jetzt sein: Neue Aufgabe: {a} + {b}")
           ergebnis_label.config(text=f"Lösung zum Testen: {c}")

           versuch_counter = 0 #versuche zurücksetzten
           versuch_label.config(text=f"Versuche:0")

        else:    
         feedback_label.config(text=f"Ergebnis Falsch - Versuch es noch mal!", fg="red")
            #Versuch aktualisieren
         versuch_label.config(text=f"Versuche:{versuch_counter}")
            #Eingabefeld leeren für nächsten Versuch 
         eingabe_feld.delete(0,tk.END)

    except ValueError:
        #Falls keine gültigen Zahlen eingegeben wurde
       feedback_label.config(text=f"Bitte gib eine gültige Zahl ein", fg="orange")

    #Button zum Prüfen
pruefen_button = tk.Button(fenster, text="Prüfen", font=("Seoge UI", 12, "bold"),
                                 bg="#7b2cbf", fg="white", 
                                 width=15, height=2, command=pruefe_eingabe) #Diese Funktion wird beim Klicken ausgeführt
pruefen_button.pack(pady=20)

    #Ergebnis-Label (zum Debuggen- kann man später entfernen)
ergebnis_label = tk.Label(fenster, text=f"Lösung zum Testen:{c}", fg="#999999", bg="#f5f0ff", font=("Segoe UI", 9))
ergebnis_label.pack(pady=(30,10))

    #Enter Taste auch zum Prüfen nutzen
eingabe_feld.bind('<Return>',lambda event: pruefe_eingabe())                      


fenster.mainloop()