#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from getpass import getpass
from models.prof_cadastro import PsqlLogin

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    auth = PsqlLogin()

    while True:
        user = auth.get_logged_in_user()
        limpar_tela()

        print("\n===== MENU =====")
        print(f"Status: {'Logado como ' + user if user else 'Desconectado'}")
        print("1 - Cadastrar usuário")
        print("2 - Login")
        print("3 - Logout")
        print("4 - Listar usuários")

        op = input("Escolha: ").strip().lower()
        limpar_tela()

        if op == '1':
            uname = input("Username: ")
            pwd = getpass("Senha: ")
            pwd2 = getpass("Repita a senha: ")
            if pwd != pwd2:
                print("Senhas não coincidem.")
            else:
                ok, msg = auth.sign_in_user(uname, pwd)
                print(msg)

        elif op == '2':
            uname = input("Username: ")
            pwd = getpass("Senha: ")
            ok, msg = auth.login_user(uname, pwd)
            print(msg)

        elif op == '3':
            msg = auth.logout()
            print(msg)

        elif op == '4':
            user = auth.get_logged_in_user()
            if user:
                usuarios = auth.list_user()
                if usuarios:
                    for u in usuarios:
                        print(f" - {u['username']}")
                    print(f"\nTotal: {len(usuarios)} usuário(s)")
                else:
                    print("Nenhum usuário encontrado.")
            else:
                print("Acesso negado! Faça login primeiro.")
            input("\nPressione ENTER para voltar ao menu...")
if __name__ == "__main__":
    main()
