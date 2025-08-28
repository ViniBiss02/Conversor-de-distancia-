 # instalação necessária:

py -m pip install tkinter 
py -m pip install ttkbootstrap

# cmd
Win + r

cmd , enter

# explicando código 

──────────────────────────────

Importações e configuração inicial

──────────────────────────────

• No início, importamos as bibliotecas necessárias:
 - A biblioteca padrão tkinter (importada como tk) serve para criar a interface gráfica.
 - Do módulo tkinter, é importado o ttk, que fornece widgets com um estilo moderno, e também importamos o ttkbootstrap, que permite usar temas pré-definidos (por exemplo, "darkly").
Essas importações garantem que possamos criar e configurar os diversos elementos da nossa interface.
──────────────────────────────

2. Função convert():

──────────────────────────────

Essa função é responsável por realizar a conversão de distâncias. Dentro dela, temos os seguintes passos:

 a) Conversão do valor de entrada
  - A linha:
   input_value = float(entry.get())
  Recebe o conteúdo digitado pelo usuário no campo de entrada (entry) e tenta convertê-lo para float. Esse float é armazenado na variável input_value. Se a conversão falhar (por exemplo, se o usuário digitar algo que não seja um número), o código entrará no bloco except e exibirá a mensagem "Digite um número válido!".

 b) Obtenção das unidades escolhidas
  - As variáveis from_unit e to_unit armazenam as opções escolhidas nos dois comboboxes (first_combobox e second_combobox). Isso define qual unidade o usuário selecionou para entrada e para saída.

 c) Dicionário conversion_factors
  - conversion_factors é um dicionário onde cada chave é uma unidade de medida (ex.: "milhas", "quilômetros", etc.) e o valor associado representa quantos metros correspondem a 1 unidade daquela medida.
   Por exemplo, "quilômetros": 1000 significa que 1 quilômetro equivale a 1000 metros.
  Esse dicionário serve de referência para converter qualquer valor dado para metros – uma base comum para todas as conversões.

 d) Verificação das unidades selecionadas
  - O código checa se os valores obtidos em from_unit e to_unit estão presentes no dicionário conversion_factors. Se algum deles não estiver, significa que o usuário não selecionou uma unidade válida, e a variável output_string é atualizada para informar "Selecione as unidades corretamente", após o que o programa retorna (não prossegue com a conversão).

 e) Realizando a conversão
  - Primeiro, o valor de entrada é convertido para metros:
   value_in_meters = input_value * conversion_factors[from_unit]
  Ou seja, multiplicamos o valor de entrada pelo fator correspondente à unidade de origem.
  - Em seguida, convertemos esse valor em metros para a unidade de destino, dividindo o valor em metros pelo fator da unidade de destino:
   converted_value = value_in_meters / conversion_factors[to_unit]

 f) Formatando e exibindo o resultado
  - Depois de calcular converted_value, o código verifica se esse valor é um inteiro (sem casas decimais) usando o método is_integer().
   Se for inteiro, converte para int e exibe sem casas decimais. Caso contrário, formata o valor com três casas decimais e exibe junto com a unidade de destino.
  - O resultado final é exibido através da variável output_string, que atualiza o texto exibido no rótulo de saída (output_label).

 g) Tratamento de erro
  - No caso de a conversão do valor de entrada falhar (por exemplo, se o usuário digitar texto em vez de número), o bloco except é executado e output_string recebe a mensagem "Digite um número válido!".

──────────────────────────────

3. Configuração da janela principal

──────────────────────────────
• A janela principal é criada com:
  window = ttk.Window(themename="darkly")
 Esse comando cria uma janela customizada usando o tema "darkly".
• Em seguida, o título da janela e seu tamanho são configurados com window.title() e window.geometry(), respectivamente, definindo, por exemplo, uma largura de 520 pixels e altura de 380 pixels.

──────────────────────────────

4. Criação dos widgets da interface

──────────────────────────────

• Label principal (título)
 - label = ttk.Label(..., text="Conversor de distancia", ...)
 Este widget exibe o título da aplicação no topo da janela com uma fonte maior ("Calibri", 26, negrito).

• Comboboxes e a seta de conversão
 - A lista modelo_distancia contém as opções de unidades de distâncias que o usuário pode escolher (ex.: "milhas", "quilômetros", etc.).
 - combo_frame é um Frame (um contêiner para outros widgets) que agrupa os comboboxes e a seta.
 - first_combobox e second_combobox são widgets do tipo Combobox, configurados com state="readonly" para que o usuário possa apenas selecionar entre as opções disponíveis.
 - arrow_label é um Label que exibe o símbolo "→", simbolizando a conversão do primeiro valor para o segundo.

• Campo de entrada e botão
 - input_frame é um Frame que contém a caixa de entrada e o botão.
 - entry_int é uma variável do tipo IntVar() associada ao widget entry (Entry) que permite ao usuário digitar o valor a ser convertido.
  Observação: apesar de usar IntVar, o valor é convertido para float na função convert, permitindo usar números decimais se for necessário.
 - button é o widget Button que, ao ser clicado, chama a função convert.

• Rótulo de saída
 - output_string é uma StringVar que armazena o texto a ser exibido no output_label. Inicialmente, ela está definida com "Resposta". Conforme a conversão é realizada, essa variável é atualizada com o valor convertido.
 - output_label é o Label que exibe a mensagem contida em output_string, comunicando ao usuário o resultado da operação.

──────────────────────────────

5. Organização dos widgets na janela

──────────────────────────────

• Cada widget é adicionado à janela utilizando o método pack(), que organiza os elementos em blocos:
 - Primeiro, o label principal (título) é packado no topo com espaçamentos (padx e pady).
 - Em seguida, o combo_frame é packado para exibir os comboboxes e a seta, organizados horizontalmente (usando side=tk.LEFT).
 - Depois, o input_frame (que contém o campo de entrada e o botão) é packado, seguido pelo output_label, que mostra o resultado.
Essa organização define a ordem visual dos elementos na aplicação.

──────────────────────────────

6. Loop principal da aplicação

──────────────────────────────

• A linha window.mainloop() inicia o laço de eventos da interface gráfica, mantendo a janela aberta e pronta para interagir com o usuário. Sem esse loop, a janela seria exibida e imediatamente fechada.

──────────────────────────────

Resumo Final

──────────────────────────────

O código cria uma interface completa para converter valores de uma unidade de distância para outra. Cada elemento do código tem um papel específico:
 - modelo_distancia define as opções de unidades para que o usuário escolha.
 - conversion_factors é um dicionário usado para converter qualquer valor para metros – uma base comum para todas as conversões.
 - output_string é a variável que armazena e atualiza o resultado da conversão exibido no rótulo de saída.
Assim, quando o usuário insere um valor, escolhe as unidades, e clica em "Submit", a função convert() lê os inputs, processa a conversão com base nos fatores definidos e exibe o resultado de forma adequada (sem casas decimais se o número for inteiro, ou com três casas decimais caso contrário).

Essa explicação detalhada deve ajudar a entender cada parte do código e como todas as peças se conectam para formar uma aplicação de conversão de distâncias.