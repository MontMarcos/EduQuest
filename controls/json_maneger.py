from os.path import isfile
import json

class JsonManager:

    def create_json(self, file_path, username, password_hash):
        """Adiciona um usuário ao JSON sem apagar os antigos"""
        users = []

        if isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                try:
                    users = json.load(f)
                    # converte dict antigo em lista
                    if isinstance(users, dict):
                        users = [users]
                except Exception:
                    users = []

        users.append({"username": username, "password": password_hash})

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(users, f, indent=2, separators=(',', ': '))

    def read_json(self, file_path):
        if isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if isinstance(data, dict):
                    data = [data]
                return data
        return []

    def update_json(self, file_path, data):
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, separators=(',', ': '))
