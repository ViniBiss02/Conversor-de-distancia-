import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    try:
        # Obter o valor de entrada; use float caso aceite casas decimais
        input_value = float(entry.get())

        # Obter as unidades selecionadas
        from_unit = first_combobox.get()
        to_unit = second_combobox.get()

        # Dicionário de conversão (os fatores representam quantos metros tem 1 unidade)
        conversion_factors = {
            "milhas": 1609.34,
            "quilômetros": 1000,
            "metros": 1,
            "jardas": 0.9144,
            "pés": 0.3048,
            "polegadas": 0.0254,
            "centímetros": 0.01,
            "milímetros": 0.001,
            "nanômetros": 1e-9,
            "micrômetros": 1e-6,
            "hectômetros": 100,
            "decâmetros": 10,
            "decímetros": 0.1
        }

        # Verifica se as unidades foram selecionadas
        if from_unit not in conversion_factors or to_unit not in conversion_factors:
            output_string.set("Selecione as unidades corretamente")
            return

        # Converte para metros e depois para a unidade de destino
        value_in_meters = input_value * conversion_factors[from_unit]
        converted_value = value_in_meters / conversion_factors[to_unit]

        # Exibe o resultado verificando se o valor é inteiro
        if converted_value.is_integer():
            output_string.set(f"{int(converted_value)} {to_unit}")
        else:
            output_string.set(f"{converted_value:.3f} {to_unit}")
    except ValueError:
        output_string.set("Digite um número válido!")

#cria a janela principal
window = ttk.Window(themename="darkly")  # tema do ttkbootstrap

# configurações da janela
window.title("First Step GUI")
window.geometry("520x380") # largura x altura


# cria um rótulo("label")
label = ttk.Label(master=window, text="Conversor de distancia", font=("Calibri", 26, "bold"), style="My.TLabel")

modelo_distancia = ["milhas", "quilômetros", "metros", "jardas", "pés", "polegadas", "centímetros", "milímetros", "nanômetros", "micrômetros", "hectômetros", "decâmetros", "decímetros"]
combo_frame = ttk.Frame(master=window)

first_combobox = ttk.Combobox(master=combo_frame, values=modelo_distancia, state="readonly")
arrow_label = ttk.Label(master=combo_frame, text="→", font=("Calibri", 16))
second_combobox = ttk.Combobox(master=combo_frame, values=modelo_distancia, state="readonly")

# criar campo de input
input_frame = ttk.Frame(master=window, style="My.TFrame")
entry_int = tk.IntVar()  # variável para armazenar o valor inteiro
entry = ttk.Entry(master=input_frame, width=20, textvariable=entry_int)
button = ttk.Button(master=input_frame, text="Submit", command = convert)


#Campo de output
output_string = tk.StringVar(value="Resposta")  # define "Resposta" como valor inicial
output_label = ttk.Label(master=window,        # rótulo de saída
                         textvariable=output_string, # variável de texto com valor inicial
                         font=("Times New Roman", 16), # fonte
                         style="My.TLabel") 

# adiciona o campo de input e o botão ao frame
label.pack(side=tk.TOP, padx=10, pady=25) # adiciona o rótulo à janela

combo_frame.pack(pady=15)
first_combobox.pack(side=tk.LEFT, padx=(0, 10))
arrow_label.pack(side=tk.LEFT, padx=(0, 10))
second_combobox.pack(side=tk.LEFT, padx=(0, 10))
entry.pack()
button.pack(padx=10, pady=10)
input_frame.pack()
output_label.pack()

#comando para iniciar o loop da interface(mantem a janela aberta) 
window.mainloop()