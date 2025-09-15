#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils.prof_cadastro import JLogin


def main():
    jl = JLogin()
    options = [
        ("1", "Sign In (register)"),
        ("2", "Login"),
        ("3", "Exit")
    ]

    while True:
        print("\n=== MENU ===")
        for key, desc in options:
            print(f"{key} - {desc}")
        choice = input("Choose an option: ")
        
        match choice:
            case "1":
                jl.sign_in()
            case "2":
                jl.login()
                break
            case "3":
                print("Exiting...")
                break
            case _:
                print("Invalid option. Try again.")


if __name__ == '__main__':
    main()
