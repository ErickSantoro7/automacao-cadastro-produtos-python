import pyautogui
import time

pyautogui.PAUSE = 4.0 # Pausa de 0.5 segundo, para não "atropelar" uma ação em cima da outra
     


# Passo 1: Entrar no sistema da empresa

# Abrir o navegador
pyautogui.press("win")

pyautogui.write("opera") # Ou outro qualuqer navegador, apenas troque o nome.

pyautogui.press("Enter")

pyautogui.write("file:///C:/Users/marti/Desktop/NexStock/login.html")

pyautogui.press("Enter")

time.sleep(3)


# Passo 2: Fazer login
# selecionar o campo de email
pyautogui.click(x=1002, y=465)

# escrever o seu email
pyautogui.write("pythonestoque@gmail.com")

pyautogui.press("tab") # passando pro próximo campo

pyautogui.write("sua senha")

pyautogui.click(x=917, y=535) # clique no botao de login

time.sleep(3) 

pyautogui.click(x=970, y=591)

# Passo 3: Importar a base de produtos pra cadastrar
import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela)

# Passo 4: Cadastrar um produto
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=825, y=312)   
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
        # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim



link_sistema = "file:///C:/Users/marti/Desktop/NexStock/login.html"







