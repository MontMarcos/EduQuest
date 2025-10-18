# 🚀 EduQuest Platform Core

![Status: Estável (Auth)](https://img.shields.io/badge/Status-Estável%20(Auth)-brightgreen)
![DB: PostgreSQL](https://img.shields.io/badge/DB-PostgreSQL-4169E1)
![Interface: Tkinter](https://img.shields.io/badge/Interface-Tkinter%2FTTK-blue)

O **EduQuest** é uma plataforma modular de apoio ao educador.  
Este repositório estabelece a **fundação segura** do sistema, fornecendo um módulo de autenticação robusto e uma arquitetura limpa, pronta para ser escalada.

---

## ✨ Módulo Principal: Autenticação (Auth API)

O sistema de autenticação migrou de arquivos JSON para uma API de segurança persistente em PostgreSQL.

---

### **1. Interface (Viewer) Profissional**

A interface foi desenvolvida em Tkinter (`ttk`) com foco na usabilidade e design *clean*, servindo como ponto de demonstração da API de autenticação.

| Tela de Login (Desconectado) | Tela Principal (Logado) |
| :---: | :---: |
| ![Tela de status inicial do EduQuest, com botão LOGIN em destaque e status de "Clique em Login para começar" em vermelho.](https://media.discordapp.net/attachments/1206426783570862134/1428922256737960169/image.png?ex=68f4430e&is=68f2f18e&hm=fe90d216a9b4968cfb4a66b2e896c3c77bc08eb44591d563127f7889b6fc0f38&=&format=webp&quality=lossless) | ![Tela de status logado, mostrando "Logado como: test" em verde. O botão LOGIN está desativado, e o LOGOUT está ativo.](https://media.discordapp.net/attachments/1206426783570862134/1428922152471629924/image.png?ex=68f442f5&is=68f2f175&hm=1dc27957aa83af2b4cdccef693052deace4da20e25a011672df370b95fd821f0&=&format=webp&quality=lossless) |
| *Status claro com feedback visual (vermelho/verde) e botões contextuais.* | *Usuário `test` logado com sucesso. Login/Cadastro desativados automaticamente.* |

---

### **2. Fluxo de Credenciais Simples**

Os modais de Login e Cadastro são minimalistas e focam apenas nos campos essenciais:

| Diálogo de Cadastro (Sign In) | Diálogo de Login |
| :---: | :---: |
| ![Diálogo "Cadastrar Nova Conta" com campos para nome de usuário, senha (oculta) e repetição de senha (oculta).](https://media.discordapp.net/attachments/1206426783570862134/1428922204220817530/image.png?ex=68f44301&is=68f2f181&hm=a2f52c9e12514bc8a16102ff5eba10f9c629719bcdc00d6dd8500f070a316975&=&format=webp&quality=lossless) | ![Diálogo "Fazer Login" com campos para nome de usuário e senha (oculta).](https://media.discordapp.net/attachments/1206426783570862134/1428922203860373514/image.png?ex=68f44301&is=68f2f181&hm=5524b6e64684c0f63467943aedb1b7b412b892823051a6044a360d75e38a7f1c&=&format=webp&quality=lossless) |
| *Permite o cadastro de um novo usuário, como `marcosmont`.* | *O usuário entra com as credenciais para verificação no PostgreSQL.* |

---

## 🏗️ Arquitetura e Tecnologia

O projeto é construído em camadas para garantir que a lógica de segurança possa ser usada por qualquer outro módulo, sem depender da interface gráfica.

| Categoria | Tecnologia | Detalhes |
| :--- | :--- | :--- |
| **Backend Core** | Python 3 | Linguagem de desenvolvimento principal. |
| **Banco de Dados** | PostgreSQL | Persistência de usuários e dados de segurança. |
| **Segurança** | `passlib` (SHA256-crypt) | Hashing robusto de senhas. |
| **UI** | Tkinter (`ttk`) | Interface Gráfica de demonstração e teste. |

---
---

## ⚙️ Guia de Configuração e Execução


### 🧩 Pré-requisitos (DB e Ambiente)

1. **PostgreSQL Server** rodando.  
2. Crie o banco de dados **`eduquest`** (ou o nome desejado).  
3. **Configure as variáveis de ambiente** com as credenciais do PostgreSQL:  

   - `DB_NAME` — nome do banco de dados  
   - `DB_USER` — nome do usuário  
   - `DB_PASS` — senha do banco  

   > 💡 *No Linux*, você pode adicioná-las ao `~/.bashrc` ou `~/.zshrc`:  
   > ```bash
   > export DB_NAME=eduquest
   > export DB_USER=seu_usuario
   > export DB_PASS=sua_senha
   > ```

---

### 🛠️ 1. Clonagem e Instalação

```bash
# Clone o repositório
git clone https://github.com/MontMarcos/EduQuest.git
cd EduQuest

# Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate   # Linux/macOS
# .\venv\Scripts\activate  # Windows (PowerShell)

# Instale as dependências necessárias
pip install psycopg2-binary python-dotenv passlib

## 🗂️ Estrutura do Projeto

```plaintext
EduQuest/
├── build/
│   └── EduQuest_Login/           # Arquivos de build gerados pelo PyInstaller
│
├── controls/                     # Camada de controle (acesso ao banco, lógica de conexão)
│   ├── postgres_manager.py       # Gerenciador de conexões e queries do PostgreSQL
│
├── models/                       # Camada de modelo (regras de negócio)
│   └── prof_cadastro.py          # Cadastro e manipulação de dados de professores
│
├── view/                         # Camada de apresentação (interface gráfica)
│   └── gui_viewer.py             # Interface principal em Tkinter
│
├── .env                          # Variáveis de ambiente (credenciais do banco, etc.)
├── Exe_EduQuest_Login            # Executável gerado com PyInstaller
├── LICENSE                       # Licença MIT
├── main.py                       # Ponto de entrada alternativo da aplicação
└── README.md                     # Documentação do projeto
```

## 🤝 Colabore

- Faça um **fork** do repositório.  
- Envie um **Pull Request** para novas funcionalidades ou correções.

---

## 📄 Licença

Distribuído sob a licença **MIT**.  
Veja o arquivo [`LICENSE`](./LICENSE) para mais informações.

---

## 👨‍💻 Autor

Feito com 💙 por **MontMarcos**.


