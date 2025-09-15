#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils.prof_cadastro import JLogin

def main():
    jl = JLogin()  # Instância única do sistema

    while True:
        if not jl.logged_in_user:
            # Menu principal
            print("=== MENU ===")
            print("1 - Sign In (register)")
            print("2 - Login")
            print("3 - Exit")
            choice = input("Choose an option: ").strip()

            if choice == "1":
                jl.sign_in()
            elif choice == "2":
                success = jl.login()
                if success:
                    # Entrou no menu do usuário logado
                    logged_in_menu(jl)
            elif choice == "3":
                print("Exiting...")
                break
            else:
                print("Invalid option. Try again.")

def logged_in_menu(jl):
    """Menu do usuário logado, fica rodando até logout ou exit"""
    while True:
        print(f"\n=== User Menu ({jl.logged_in_user}) ===")
        print("1 - Logout")
        print("2 - Exit")
        choice = input("Choose an option: ").strip()

       
        if choice == "1":
            jl.logout()
            print("Logged out. Program finished.")
            break  
        elif choice == "2":
            print("Exiting...")
            exit(0)
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")
