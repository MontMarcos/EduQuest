from os.path import isfile
from json import dump, load

class JsonManager:

    def create_json(self, filepatch, username, password_hash):
        """Adiciona um usuário ao JSON sem apagar os antigos"""
        users = []

        if isfile(filepatch):
            with open(filepatch, 'r') as f:
                try:
                    users = load(f)
                    if isinstance(users, dict):
                        users = [users]
                except Exception:
                    users = []

        users.append({"username": username, "password": password_hash})

        with open(filepatch, 'w') as f:
            dump(users, f, indent=2, separators=(',', ': '))

    def read_json(self, filepatch):
        if isfile(filepatch):
            with open(filepatch) as f:
                data = load(f)
                if isinstance(data, dict):
                    data = [data]
                return data
        return []

    def update_json(self, filepatch, data):
        with open(filepatch, 'w') as f:
            dump(data, f, indent=2, separators=(',', ': '))
