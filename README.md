# ✂️ CorteJá

> Plataforma SaaS de agendamento online para barbearias — conectando clientes e barbeiros de forma simples e direta.

---

## 💡 O Problema

Hoje a maioria dos barbeiros ainda agenda pelo WhatsApp. O cliente manda mensagem, espera resposta, negocia horário — uma experiência lenta e desorganizada para os dois lados.

## 🚀 A Solução

O **CorteJá** é uma plataforma web onde barbeiros cadastram sua barbearia e disponibilizam seus horários, e clientes encontram e agendam um horário em segundos — sem precisar falar com ninguém.

---

## 👥 Funcionalidades

### Cliente
- Cadastro com nome, telefone e senha
- Busca de barbearias por nome
- Visualização de horários disponíveis
- Agendamento de serviços com comprovante

### Barbeiro
- Cadastro completo da barbearia (nome, localização, foto, serviços)
- Configuração de dias e horários de atendimento
- Calendário semanal com agendamentos
- Bloqueio de horários e dias indisponíveis
- Cancelamento de agendamentos com notificação ao cliente

---

## 🛠️ Tecnologias

**Backend**
- Python 3.13
- Flask
- SQLAlchemy (ORM)
- SQLite
- bcrypt (criptografia de senhas)
- python-dotenv

**Frontend**
- HTML, CSS, JavaScript

---

## 🗂️ Estrutura do Projeto

```
CorteJá/
├── backend/
│   ├── models/          # Modelos do banco de dados
│   │   ├── cliente.py
│   │   ├── barbeiro.py
│   │   ├── servico.py
│   │   ├── agendamento.py
│   │   └── bloqueio.py
│   ├── routes/          # Rotas da API REST
│   │   ├── cliente.py
│   │   └── barbeiro.py
│   ├── extensions.py    # Instância do banco de dados
│   └── app.py           # Inicialização da aplicação
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
├── .env.example
├── .gitignore
└── requirements.txt
```

---

## ⚙️ Como rodar o projeto

**1. Clone o repositório**
```bash
git clone https://github.com/jorgemeert/corteja
cd corteja
```

**2. Crie e ative o ambiente virtual**
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
```

**3. Instale as dependências**
```bash
pip install -r requirements.txt
```

**4. Configure as variáveis de ambiente**

Crie um arquivo `.env` dentro da pasta `backend` com o seguinte conteúdo:
```
SECRET_KEY=sua_chave_secreta
DATABASE_URL=sqlite:///corteja.db
```

**5. Rode a aplicação**
```bash
python -m backend.app
```

Acesse em: `http://127.0.0.1:5000`

---

## 📡 Endpoints da API

| Método | Rota | Descrição |
|--------|------|-----------|
| POST | `/cadastro` | Cadastro de cliente |
| POST | `/login` | Login de cliente |
| POST | `/cadastroBarbeiro` | Cadastro de barbeiro |
| POST | `/loginBarbeiro` | Login de barbeiro |

---

## 🔒 Segurança

- Senhas criptografadas com **bcrypt** antes de salvar no banco
- Variáveis sensíveis isoladas no arquivo `.env` (não versionado)

---

## 📌 Status do Projeto

🚧 **Em desenvolvimento** — MVP em construção.

---

## 👨‍💻 Autor

**Jorge Meert**  
Estudante de Engenharia de Software — FIAP  
[github.com/jorgemeert](https://github.com/jorgemeert)
