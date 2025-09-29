#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils.prof_cadastro import JLogin

def logged_in_menu(jl):
    """Menu do usuário logado, fica rodando até logout ou exit"""
    while True:
        print(f"\n=== User Menu ({jl.get_logged_in_user()}) ===")
        print("1 - Logout")
        print("2 - Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            jl.logout()
            print("Logged out. Returning to main menu.")
            break
        elif choice == "2":
            print("Exiting...")
            exit(0)
        else:
            print("Invalid option. Try again.")

def main():
    try:
        jl = JLogin()  
    except Exception as e:
        print(f"Error initializing JLogin. Check file paths and imports: {e}")
        return

    while True:
        if not jl.get_logged_in_user():
            print("\n=== MAIN MENU ===")
            print("1 - Sign In (register)")
            print("2 - Login")
            print("3 - Exit")
            choice = input("Choose an option: ").strip()

            if choice == "1":
                jl.sign_in()
            elif choice == "2":
                success = jl.login()
                if success:
                    logged_in_menu(jl)
            elif choice == "3":
                print("Exiting...")
                break
            else:
                print("Invalid option. Try again.")
        else:
            logged_in_menu(jl)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")
