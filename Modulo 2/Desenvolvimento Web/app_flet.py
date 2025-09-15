import flet as ft 

def main(page: ft.Page):
    page.theme_mode = "Dark"
    texto_login = ft.Text("Login:",size= 30, color="Purple") 
    entrada_texto_login = ft.TextField(width = 600)
    texto_senha  = ft.Text("Senha:",size=30, color= "Purple") 
    entrada_texto_senha = ft.TextField(width = 600, password=True, can_reveal_password=True )
    def click(e):
        Valor_do_texto_login = texto_login.value
        print("xD!",Valor_do_texto_login)
    btn = ft.ElevatedButton("Clique em mim", on_click=click )
    page.add(ft.Row([texto_login ,entrada_texto_login]), ft.Row([texto_senha,entrada_texto_senha]),
             ft.Row([btn]))
ft.app(target=main)