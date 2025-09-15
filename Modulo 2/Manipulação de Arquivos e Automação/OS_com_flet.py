import os
import flet as ft

def main(page: ft.Page):
    page.title = "Gerenciador de arquivos"
    page.theme_mode = "light"
    
    def criar_pasta(e):
        global texto_pasta
        try:
            texto_pasta = texto_recebido.value
            os.mkdir(texto_pasta)
            informativo.value = f"Pasta criada: '{texto_pasta}'"
            informativo.color = "black"
        except FileExistsError:
            informativo.value = f"A pasta '{texto_pasta}' já existe."
            informativo.color = "red"
        except Exception as erro:
            informativo.value = f"Erro ao criar pasta: {erro}"
            informativo.color = "red"
        page.update()
    
    def remover_pasta(e):
        texto_pasta = texto_recebido.value
        try:
            os.rmdir(texto_pasta)
            informativo.value = f"Pasta '{texto_pasta}' removida!"
            informativo.color = "red"
        except FileNotFoundError:
            informativo.value = f"Pasta '{texto_pasta}' não encontrada."
            informativo.color = "red"
        except OSError as erro:
            informativo.value = f"Erro ao remover pasta (talvez não esteja vazia): {erro}"
            informativo.color = "red"
        page.update()  

    def remover_arquivo(e):
        try:
            texto_2 = texto_recebido_2.value
            caminho_arquivo = os.path.join(texto_pasta, texto_2)
            if os.path.exists(caminho_arquivo):
                os.remove(caminho_arquivo)
                informativo.value = f"Arquivo '{texto_2}' removido!"
                informativo.color = "green"
            else:
                informativo.value = f"Arquivo '{texto_2}' não existe."
                informativo.color = "gray"
        except Exception as erro:
            informativo.value = f"Erro ao remover arquivo: {erro}"
            informativo.color = "red"
    page.update()

    
    def criar_arquivo(e):
        try:
            texto_2 = texto_recebido_2.value
            open(f"{texto_pasta}/{texto_2}", "w").close()
            informativo.value = f"Arquivo criado: '{texto_2}'"
            informativo.color = "black"
        except Exception as erro:
            informativo.value = f"Erro ao criar arquivo: {erro}"
            informativo.color = "red"
        page.update()
    texto_recebido = ft.TextField(label="Escreva o nome da Pasta...", width=300)
    botao_pasta = ft.ElevatedButton("CRIAR PASTA", bgcolor="green", color="white", width=200, on_click=criar_pasta)
    botao_apagarpasta = ft.ElevatedButton("APAGAR PASTA", bgcolor="red", color="white", width=200, on_click=remover_pasta)
    botao_arquivo = ft.ElevatedButton("CRIAR ARQUIVO", bgcolor="Green", color="white", width=200, on_click=criar_arquivo)
    botao_apagararquivo = ft.ElevatedButton("APAGAR ARQUIVO", bgcolor="red", color="white", width=200, on_click=remover_arquivo)
    informativo = ft.Text("", size=20, color="black")
    texto_recebido_2 = ft.TextField(label="Escreva o nome da Pasta...", width=300)
    page.add(
        ft.Row([texto_recebido], alignment="center"),
        ft.Row([botao_pasta, botao_apagarpasta], alignment="center"),
        ft.Row([texto_recebido_2], alignment="center"),
        ft.Row([botao_arquivo, botao_apagararquivo], alignment="center"),
        ft.Row([informativo], alignment="center")
    )
ft.app(target=main)
