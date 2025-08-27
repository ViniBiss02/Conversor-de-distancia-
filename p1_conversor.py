import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.60934
    print(f"{mile_input} milhas é igual a {km_output:.4f} km")
    output_string.set(f"{km_output:.4f} km")

#cria a janela principal
window = ttk.Window(themename="darkly")  # tema do ttkbootstrap

# configurações da janela
window.title("First Step GUI")
window.geometry("320x180") # largura x altura


# cria um rótulo("label")
label = ttk.Label(master=window, text="Hello, Tkinter!", font=("Calibri", 16, "bold"), style="My.TLabel")
label.pack(padx=10, pady=10) # adiciona o rótulo à janela

# criar campo de input
input_frame = ttk.Frame(master=window, style="My.TFrame")
entry_int = tk.IntVar()  # variável para armazenar o valor inteiro
entry = ttk.Entry(master=input_frame, width=20, textvariable=entry_int)
button = ttk.Button(master=input_frame, text="Submit", command = convert)

# adiciona o campo de input e o botão ao frame
entry.pack(side=tk.LEFT, padx=5, pady=5)
button.pack(side=tk.LEFT, padx=5, pady=5)
input_frame.pack(padx=10, pady=10)

#Campo de output
output_string = tk.StringVar(value="Resposta")  # define "Resposta" como valor inicial
output_label = ttk.Label(master=window,        # rótulo de saída
                         textvariable=output_string, # variável de texto com valor inicial
                         font=("Times New Roman", 16), # fonte
                         style="My.TLabel")           # estilo
output_label.pack(padx=10, pady=10)

#comando para iniciar o loop da interface(mantem a janela aberta) 
window.mainloop()