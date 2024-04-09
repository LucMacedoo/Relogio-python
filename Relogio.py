import tkinter as tk
import datetime
import locale

#Configurando o local
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

raiz = tk.Tk()

#Matemática que vai garantir que a tela esteja no centro
largura_raiz = 500
altura_raiz = 200
largura_pc = raiz.winfo_screenwidth()
altura_pc = raiz.winfo_screenheight()
x = (largura_pc - largura_raiz) // 2
y = (altura_pc - altura_raiz) // 2

#Configurações
raiz.title("Hora Atual")
raiz.geometry(f"{largura_raiz}x{altura_raiz}+{x}+{y}")
raiz.configure(bg="#303030")
raiz.resizable(False, False)

def get_date():
    dia_semana = datetime.datetime.now().strftime("%A").capitalize()
    dia_completo = datetime.datetime.now().strftime("%d / %m / %Y")
    dia.config(text=(dia_semana + " - " + dia_completo))
    hora.after(250, get_date)

def get_horas():
    hora_atual = datetime.datetime.now().strftime("%H : %M : %S")
    hora.config(text=hora_atual)
    hora.after(250, get_horas)

hora = tk.Label(raiz, font=("Tahoma", 40, "bold"), bg="#303030", fg="#00FF00")
hora.place(relx=0.5, rely=0.5, anchor="center")

dia = tk.Label(raiz, font=("Tahoma", 15), bg="#303030", fg="#00FF00", text="Teste")
dia.pack(pady=30)

get_horas()
get_date()

raiz.mainloop()
