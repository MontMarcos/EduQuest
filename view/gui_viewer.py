import tkinter as tk
from tkinter import messagebox, ttk
import sys
import os

from models.prof_cadastro import PsqlLogin 

class AuthDialog(tk.Toplevel):
    def __init__(self, master, title, auth_system):
        super().__init__(master)
        self.auth_system = auth_system
        self.title(title)
        self.transient(master)
        self.result = None
        self.resizable(False, False)
        
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.password_verify = tk.StringVar()
        self.is_signin = (title == "Cadastrar Nova Conta")

        main_frame = ttk.Frame(self, padding="30 30 30 30")
        main_frame.pack(fill="both", expand=True)
        
        self.create_header(main_frame, title)
        self.create_widgets(main_frame)
        self.create_buttonbox(main_frame)
        
        self.update_idletasks()
        self.geometry(f'+{master.winfo_rootx() + master.winfo_width() // 2 - self.winfo_width() // 2}'
                      f'+{master.winfo_rooty() + master.winfo_height() // 2 - self.winfo_height() // 2}')

        self.grab_set()
        master.wait_window(self)

    def create_header(self, parent, title):
        ttk.Label(parent, text="EduQuest", font=("Arial", 24, "bold"), foreground="#4285F4").pack(pady=(0, 10))
        ttk.Label(parent, text=title, font=("Arial", 14)).pack(pady=(0, 20))
        
    def create_widgets(self, parent):
        fields_frame = ttk.Frame(parent)
        fields_frame.pack(fill='x', pady=10)

        self.user_entry = ttk.Entry(fields_frame, textvariable=self.username, width=40, font=('Arial', 10))
        self.user_entry.pack(pady=10, ipady=5) 
        self.user_entry.insert(0, "Email ou Nome de Usuário")
        self.user_entry.bind("<FocusIn>", lambda event: self.clear_placeholder(self.user_entry, "Email ou Nome de Usuário"))
        self.user_entry.bind("<FocusOut>", lambda event: self.set_placeholder(self.user_entry, "Email ou Nome de Usuário"))
        
        self.pass_entry = ttk.Entry(fields_frame, textvariable=self.password, show='*', width=40, font=('Arial', 10))
        self.pass_entry.pack(pady=10, ipady=5)
        self.pass_entry.insert(0, "Senha")
        self.pass_entry.bind("<FocusIn>", lambda event: self.clear_placeholder(self.pass_entry, "Senha", show='*'))
        self.pass_entry.bind("<FocusOut>", lambda event: self.set_placeholder(self.pass_entry, "Senha", show='*'))

        if self.is_signin:
            self.pass_verify_entry = ttk.Entry(fields_frame, textvariable=self.password_verify, show='*', width=40, font=('Arial', 10))
            self.pass_verify_entry.pack(pady=10, ipady=5)
            self.pass_verify_entry.insert(0, "Repetir Senha")
            self.pass_verify_entry.bind("<FocusIn>", lambda event: self.clear_placeholder(self.pass_verify_entry, "Repetir Senha", show='*'))
            self.pass_verify_entry.bind("<FocusOut>", lambda event: self.set_placeholder(self.pass_verify_entry, "Repetir Senha", show='*'))

    def clear_placeholder(self, entry, placeholder, show=''):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(show=show, foreground='black')

    def set_placeholder(self, entry, placeholder, show=''):
        if not entry.get():
            entry.insert(0, placeholder)
            entry.config(show='', foreground='gray')
            
    def create_buttonbox(self, parent):
        btn_frame = ttk.Frame(parent)
        btn_frame.pack(fill='x', pady=10)
        
        style = ttk.Style()
        style.configure('Primary.TButton', font=('Arial', 10, 'bold'), background='#4285F4', foreground='white')
        style.map('Primary.TButton', background=[('active', '#3c79e6')])
        
        ttk.Button(btn_frame, text="Confirmar", style='Primary.TButton', command=self.ok, width=15).pack(side=tk.RIGHT, padx=5)
        
        ttk.Button(btn_frame, text="Voltar", command=self.cancel, width=15).pack(side=tk.LEFT, padx=5)

        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)
        self.user_entry.focus_set()

    def ok(self, event=None):
        uname = self.username.get().strip() if self.username.get() != "Email ou Nome de Usuário" else ""
        pwd = self.password.get().strip() if self.password.get() != "Senha" else ""
        pwd_ver = self.password_verify.get().strip() if self.is_signin and self.password_verify.get() != "Repetir Senha" else pwd

        if not uname or not pwd:
            messagebox.showwarning("Atenção", "Preencha todos os campos.", parent=self)
            return

        if self.is_signin and pwd != pwd_ver:
            messagebox.showwarning("Atenção", "As senhas não coincidem.", parent=self)
            return

        if self.is_signin:
            success, message = self.auth_system.sign_in_user(uname, pwd)
            action = "Cadastro"
        else:
            success, message = self.auth_system.login_user(uname, pwd)
            action = "Login"

        if success:
            messagebox.showinfo("Sucesso", f"{action} realizado com sucesso!", parent=self.master)
        else:
            messagebox.showerror(f"Erro de {action}", message, parent=self.master)

        self.result = success 
        self.destroy()

    def cancel(self, event=None):
        self.result = False
        self.destroy()

class AuthViewerApp:
    
    def __init__(self, master):
        self.master = master
        master.title("EduQuest") 
        master.resizable(False, False)
        
        try:
            self.auth_system = PsqlLogin()
            print("Conexão com PostgreSQL estabelecida com sucesso.")
        except Exception as e:
            messagebox.showerror("Erro Crítico de Conexão", "Falha na conexão com o DB. Verifique o ambiente.")
            sys.exit(1)

        self.status_text = tk.StringVar()
        self.setup_ui()
        self.update_status()

    def setup_ui(self):
        main_frame = ttk.Frame(self.master, padding="30")
        main_frame.pack(fill="both", expand=True)

        ttk.Label(main_frame, text="EduQuest", font=("Arial", 28, "bold"), foreground="#4285F4").pack(pady=15)
        
        self.label_status = ttk.Label(main_frame, 
                                     textvariable=self.status_text, 
                                     font=("Arial", 10),
                                     anchor="center")
        self.label_status.pack(pady=10)

        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(pady=10)

        self.btn_login_call = ttk.Button(btn_frame, text="LOGIN", width=20, command=lambda: self.open_auth_dialog("Fazer Login"))
        self.btn_login_call.pack(pady=5)
        
        ttk.Label(btn_frame, text="Não tem conta?").pack(pady=(15, 0))
        self.btn_signin_call = ttk.Button(btn_frame, text="Cadastre-se", command=lambda: self.open_auth_dialog("Cadastrar Nova Conta"), style="Link.TButton")
        self.btn_signin_call.pack(pady=5)

        self.btn_logout = ttk.Button(btn_frame, text="Logout", width=20, command=self.logout_gui, state=tk.DISABLED)
        self.btn_logout.pack(pady=10)

    
    def open_auth_dialog(self, action):
        """Abre o diálogo de Login ou Cadastro."""
        AuthDialog(self.master, action, self.auth_system)
        self.update_status()

    def update_status(self):
        user = self.auth_system.get_logged_in_user()
        
        if user:
            self.status_text.set(f"Logado como: {user}")
            self.label_status.config(foreground="#28a745")
            self.btn_login_call.config(state=tk.DISABLED)
            self.btn_signin_call.config(state=tk.DISABLED)
            self.btn_logout.config(state=tk.NORMAL)
        else:
            self.status_text.set("Clique em Login para começar")
            self.label_status.config(foreground="#dc3545")
            self.btn_login_call.config(state=tk.NORMAL)
            self.btn_signin_call.config(state=tk.NORMAL)
            self.btn_logout.config(state=tk.DISABLED)

    def logout_gui(self):
        message = self.auth_system.logout()
        messagebox.showinfo("Logout", message)
        self.update_status()


if __name__ == '__main__':
    root = tk.Tk()
    app = AuthViewerApp(root)
    root.mainloop()