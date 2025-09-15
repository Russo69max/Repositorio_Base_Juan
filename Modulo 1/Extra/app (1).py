import customtkinter as ctk 
import sqlite3
from tkinter import  *
from tkinter import messagebox
class BackEnd():
    def conecta_db(self):
        self.conn = sqlite3.connect("Sistema_cadastros.db")
        self.cursor = self.conn.cursor()
        print("Banco de Dados Conectado")
    
    def desconecta_db(self):
        self.conn.close()
        print("Banco de Dados Desconectado")

    def cria_tabela(self):
        self.conecta_db()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Usuarios(
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                Username TEXT NOT NULL,
                Email TEXT NOT NULL,
                Senha TEXT NOT NULL,
                Comfirma_Senha TEXT NOT NUll
            );
        """)
        try:
            if (self.username_cadastro == "" or self.email_cadastro == "" or self.senha_cadastro == "" or self.confirma_senha_cadastro == ""):
                messagebox.showerror(title="Sistema de login ", message="ERRO!!!\nPor favor complete todos os campos!")
            elif (len(self.username_cadastro) < 4):
                messagebox.showwarning(title="Sistema de Login", message = "O nome de Usuario deve ser de pelo menos 4 caracteres.")

            elif (len(self.senha_cadastro) < 4):
                messagebox.showwarning(title="Sistema de Login", message = "A senha do Usuario deve ser de pelo menos 4 caracteres.")

            elif (self.senha_cadastro != self.confirma_senha_cadastro):
                messagebox.showwarning(title="Sistema de Login", message= "ERRO!!!\nPor favor coloque as Senhas iguais!")
            else:
                self.conn.commit()
                messagebox.showinfo(title= "Sistema de Login", message="Parabens {self.username_cadastro}\n Os seus dados foram cadastrados com sucesso!")
                self.desconecta_db()
            self.limpa_entry_cadastro()


        except:
            messagebox.showerror(title="Sistema de Login", message="Erro no processamento do seu cadastro\nPor favor tente novamente!")
            self.desconecta_db()

    def verifica_login(self):
        self.username_login = self.username_login_entry.get()
        self.senha_login = self.senha_login_entry.get()

        self.conecta_db()
        self.cursor.execute("""SELECT * FROM Usuarios WHERE (Username = ? AND Senha = ?)"""(self.username_login, self.senha_login))
        self.verifica_dados = self.cursor.fetchone() #Percorrendo na tabela Usuarios

        try:
            if(self.username_login =="" or self.senha_login==""):
                messagebox.showwarning(title="Sistema de Login", message="ERRO!!!\nPor favor preencha todos os campos!")
            elif(self.username_login in self.verifica_dados and self.senha_login in self.verifica_login):
                messagebox.showinfo(title="Sistema de Login", message=f"Parabens{self.username_login}\nLogin feito com Sucesso!")
                self.desconecta_db()
                self.limpa_entry_login()
        except:
            messagebox.showerror(title="Sistema de Login", message="ERRO!!!\nDados nao encontrados no Sistema.\nPor favor verifica os seus dados ou cadastre-se no nosso sistema!")
            self.desconecta_db()

    def cadastrar_usuario(self):
        self.username_cadastro =self.username_cadastro_entry.get()
        self.email_cadastro =self.email_cadastro_entry.get()
        self.senha_cadastro =self.senha_cadastro_entry.get()
        self.confirma_senha_cadastro =self.confirma_senha_entry.get()

        self.conecta_db()

        self.cursor.execute("""
            INSERT INTO Usuarios (Username, Email, Senha, Comfirma_senha)
            VALUES(?, ?, ?, ?)""",(self.username_cadastro, self.email_cadastro, self.senha_cadastro, self.confirma_senha_cadastro))

        self.conn.commit()
        print("Dados Cadastrados com Sucesso!")
        self.desconecta_db()

    
class App(ctk.CTk, BackEnd):
    def __init__(self):
        super().__init__()
        self.configuraçoes_da_janela_inicial()
        self.tela_de_login()
        self.cria_tabela()

    #Configurando a janela principal 
    def configuraçoes_da_janela_inicial(self):

        self.geometry("700x400")
        self.title("Sistema de Cadastro e Login")
        self.resizable(False, False)
    def tela_de_login(self):


        #trabalhando com imagens 
        self.img = PhotoImage(file="Loginfoto.png")
        self.lb_img=ctk.CTkLabel(self, text=None, image=self.img)
        self.lb_img.grid(row=1, column=0, padx=10)

        #Titulo da nossa plataforma 
        self.title = ctk.CTkLabel(self, text="Faça o seu Login ou Cadastre-se\nna nossa plataforma para acessar\nnossos serviços!", font=("Century Gothic", 16))
        self.title.grid(row=0, column=0, pady=10, padx=10)

        #Criar frame do formulario do login
        self.frame_login = ctk.CTkFrame(self, width=350, height=380)
        self.frame_login.place(x=350, y=10)

        #Colocando widgets dentro do frame - formulario de login 
        self.lb_title = ctk.CTkLabel(self.frame_login, text="Faça seu Login", font=("Century Gothic", 22))
        self.lb_title.grid(row=0, column=0, padx= 10, pady=10)

        self.username_login_entry = ctk.CTkEntry(self.frame_login, width=300, placeholder_text= "Seu nome de Usuario...", font=("Century Gothic", 16), corner_radius=15)
        self.username_login_entry.grid(row=1, column=0, padx=10, pady=10)

        self.senha_login_entry = ctk.CTkEntry(self.frame_login, width=300, placeholder_text= "Qual sua Senha...", font=("Century Gothic", 16), corner_radius=15, show=".", border_color="#1866a5")
        self.senha_login_entry.grid(row=2, column=0, padx=10, pady=10)


        self.ver_senha = ctk.CTkCheckBox(self.frame_login, text= "Clique para ver a sua Senha..", font=("Century Gothic", 14),corner_radius=20, border_color="#1866a5")
        self.ver_senha.grid(row=3, column=0, padx=10, pady=10)


        self.btn_login = ctk.CTkButton(self.frame_login, width=300,text= "Fazer Login".upper(), font=("Century Gothic", 14),    corner_radius=15, command = self.verifica_login)
        self.btn_login.grid(row=4, column=0, padx=10, pady=10)

        self.span = ctk.CTkLabel(self.frame_login, text="Se nao tem conta, clique no botao abaixo para poder se\ncadastrar no nosso sistema!", font=("Century Gothic", 10 ))
        self.span.grid(row=5, column=0, padx=10, pady=10)

        self.btn_cadastro = ctk.CTkButton(self.frame_login, width=300, fg_color = "green", hover_color="#050", text= "Fazer Cadastro".upper(), font=("Century Gothic", 14),corner_radius=15, command=self.tela_de_cadastro)
        self.btn_cadastro.grid(row=6, column=0, padx=10, pady=10)

    def tela_de_cadastro(self):
        #Remover o formulario de login 
        self.frame_login.place_forget()

        #Frame de formulario de Cadastro 
        self.frame_cadastro = ctk.CTkFrame(self, width=350, height=380)
        self.frame_cadastro.place(x=350, y=10)

        #Criando o nosso titulo
        self.lb_title = ctk.CTkLabel(self.frame_cadastro, text="Faça seu Login", font=("Century Gothic", 22))
        self.lb_title.grid(row=0, column=0, padx= 10, pady=10)

        #Criar os nossos widgets de cadastro
        self.username_cadastro_entry = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text= "Seu nome de Usuario...", font=("Century Gothic", 16), corner_radius=15)
        self.username_cadastro_entry.grid(row=1, column=0, padx=10, pady=5)

        self.email_cadastro_entry = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text= "Qual Seu Email de Usuario...", font=("Century Gothic", 16), corner_radius=15)
        self.email_cadastro_entry.grid(row=2, column=0, padx=10, pady=5)

        self.senha_cadastro_entry = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text= "Qual sua Senha de Usuario", font=("Century Gothic", 16), corner_radius=15, show=".", border_color="#1866a5")
        self.senha_cadastro_entry.grid(row=3, column=0, padx=10, pady=5)
        
        self.confirma_senha_entry = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text= "Confirma Senha de Usuario...", font=("Century Gothic", 16), corner_radius=15, show=".")
        self.confirma_senha_entry.grid(row=4, column=0, padx=10, pady=5)

        self.ver_senha = ctk.CTkCheckBox(self.frame_cadastro, text= "Clique para ver a sua Senha..", font=("Century Gothic", 14),corner_radius=20, border_color="#1866a5")
        self.ver_senha.grid(row=5, column=0, pady=10)

        self.btn_cadastrar_user = ctk.CTkButton(self.frame_cadastro, width=300, fg_color = "green", hover_color="#050", text= "Fazer Cadastro".upper(), font=("Century Gothic", 14),corner_radius=15, command=self.cadastrar_usuario)
        self.btn_cadastrar_user.grid(row=6, column=0, padx=10, pady=5)

        self.btn_login_back = ctk.CTkButton(self.frame_cadastro, width=300,text= "Voltar para o Login".upper(), font=("Century Gothic", 14),    corner_radius=15, fg_color="#444", hover_color= "#333", command= self.tela_de_login)
        self.btn_login_back.grid(row=7, column=0, padx=10, pady=10)

    def limpa_entry_cadastro(self):
        self.username_cadastro_entry.delete(0, END)
        self.email_cadastro_entry.delete(0, END)
        self.senha_cadastro_entry.delete(0, END)
        self.comfirma_senha_entry.delete(0, END)

    def limpa_entry_login(self):
        self.username_login_entry.delete(0, END)
        self.senha_login_entry.delete(0, END)


        


if __name__=="__main__":
    app = App()
    app.mainloop()

