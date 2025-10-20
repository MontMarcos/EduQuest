#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os.path import dirname, realpath, join
from controls.postgres_maneger import PostgresManager
from getpass import getpass 
from passlib.hash import sha256_crypt

class PsqlLogin: 

    def __init__(self):
        self.db_manager = PostgresManager()
        self.__logged_in_user = None

    def sign_in_user(self, username, password):
        """Tenta cadastrar um usuário com username e password fornecidos."""
        if not username:
            return (False, "Username não pode ser vazio.")
        if len(username) > 20:
            return (False, "Username deve ter no máximo 20 caracteres.")
        if not password:
             return (False, "Password não pode ser vazio.")

        if self.db_manager.get_user_by_username(username):
            return (False, "Username já existe. Escolha outro.")

        hash_password = sha256_crypt.hash(password)
        
        if self.db_manager.create_user(username, hash_password):
            return (True, 'Registration done!')
        else:
            return (False, 'Falha ao salvar no banco de dados.')


    def login_user(self, username, password):
        """Tenta fazer login com username e password fornecidos."""

        user = self.db_manager.get_user_by_username(username) 
        
        if not user:
            return (False, "Username não existe!")

        if sha256_crypt.verify(password, user['password']):
            self.__logged_in_user = username
            return (True, f"Login successful! Welcome {username}")
        else:
            return (False, "Incorrect password!")

    def logout(self):
        if self.__logged_in_user:
            msg = f"{self.__logged_in_user} foi desconectado."
            self.__logged_in_user = None
            return msg
        else:
            return "Nenhum usuário está logado."

    def get_logged_in_user(self):
        return self.__logged_in_user
    
    def list_user(self):
        return self.db_manager.read_all_users()
