# ✂️ CorteJá

> Plataforma de agendamento online para barbearias — conectando clientes e barbeiros de forma simples e direta.

---

## 💡 O Problema

Hoje a maioria dos barbeiros ainda agenda pelo WhatsApp. O cliente manda mensagem, espera resposta, negocia horário — uma experiência lenta e desorganizada para os dois lados.

## 🚀 A Solução

O **CorteJá** é uma plataforma web onde barbeiros cadastram sua barbearia e disponibilizam seus horários, e clientes encontram e agendam um horário em segundos — sem precisar falar com ninguém.

---

## 👥 Funcionalidades

### Cliente

- Cadastro com nome, telefone e senha
- Login
- Busca de barbearias por nome
- Visualização de serviços e valores de cada barbearia
- Agendamento de dia, horário e serviço
- Visualização do agendamento ativo
- Cancelamento de agendamento

### Barbeiro

- Cadastro com dados da barbearia (nome, localização, foto, telefone)
- Login
- Configuração dos serviços oferecidos e seus valores
- Visualização dos agendamentos recebidos (calendário)
- Cancelamento de agendamentos
- Bloqueio de dias e horários indisponíveis

---

## 🛠️ Tecnologias

**Backend**

- Python 3.13
- Flask
- Flask-SQLAlchemy (ORM)
- Flask-CORS
- SQLite
- bcrypt (criptografia de senhas)
- python-dotenv

**Frontend**

- HTML, CSS, JavaScript (Fetch API)

**Ferramentas**

- Insomnia (testes de API)
- SQLite Viewer (inspeção do banco)

---

## 🗂️ Estrutura do Projeto

```
barber/
├── backend/
│   ├── models/                 # Modelos do banco de dados
│   │   ├── cliente.py
│   │   ├── barbeiro.py
│   │   ├── servico.py
│   │   ├── agendamento.py
│   │   └── bloqueio.py
│   ├── routes/                 # Rotas da API REST
│   │   ├── cliente.py
│   │   ├── barbeiro.py
│   │   ├── servico.py
│   │   ├── agendamento.py
│   │   └── bloqueio.py
│   ├── config/                 # Configurações da aplicação
│   ├── extensions.py           # Instância do banco de dados (SQLAlchemy)
│   └── app.py                  # Inicialização da aplicação Flask
├── frontend/
│   ├── index.html              # Escolha: cliente ou barbeiro
│   ├── script.js
│   ├── style.css
│   ├── cliente/
│   │   ├── login.html          # Login / registro de cliente
│   │   ├── barbearias.html     # Lista e busca de barbearias
│   │   ├── agendamentos.html   # Escolha de serviço, dia e horário
│   │   ├── agendamento-ativo.html
│   │   └── JavaScript/
│   │       ├── login.js
│   │       ├── barbearias.js
│   │       ├── agendamentos.js
│   │       └── agendamento-ativo.js
│   └── barbeiro/
│       ├── login.html          # Login / registro de barbeiro
│       ├── config.html         # Cadastro de serviços e valores
│       ├── horarios.html       # Calendário de agendamentos
│       ├── calendario.html     # Bloqueio de dias/horários
│       └── JavaScript/
│           ├── login.js
│           ├── config.js
│           ├── horarios.js
│           └── calendario.js
├── doc/                         # Histórias de usuário e backlog
├── .env                         # Variáveis de ambiente (não versionado)
├── .gitignore
└── requirements.txt
```

---

## ⚙️ Como rodar o projeto

**1. Clone o repositório**

```bash
git clone https://github.com/jorgemeert/corteja
cd barber
```

**2. Crie e ative o ambiente virtual**

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
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

A API estará disponível em `http://127.0.0.1:5000`

**6. Abra o frontend**

Use a extensão **Live Server** (ou similar) para abrir `frontend/index.html` em `http://127.0.0.1:5500`.

---

## 📡 Endpoints da API

### Cliente

| Método | Rota        | Descrição           |
| ------ | ----------- | ------------------- |
| POST   | `/cadastro` | Cadastro de cliente |
| POST   | `/login`    | Login de cliente    |

### Barbeiro

| Método | Rota                  | Descrição                 |
| ------ | --------------------- | ------------------------- |
| POST   | `/cadastroBarbeiro`   | Cadastro de barbeiro      |
| POST   | `/loginBarbeiro`      | Login de barbeiro         |
| GET    | `/barbearias`         | Lista todas as barbearias |
| POST   | `/pesquisarBarbearia` | Busca barbearia por nome  |

### Serviço

| Método | Rota                      | Descrição                     |
| ------ | ------------------------- | ----------------------------- |
| POST   | `/cadastroServico`        | Cadastro de serviço           |
| GET    | `/servicos/<id_barbeiro>` | Lista serviços de um barbeiro |

### Agendamento

| Método | Rota                                 | Descrição                             |
| ------ | ------------------------------------ | ------------------------------------- |
| POST   | `/agendarHorario`                    | Cria um novo agendamento              |
| GET    | `/mostrarAgendamentos/<id_barbeiro>` | Lista agendamentos de um barbeiro     |
| GET    | `/agendamentosAtivos/<id_cliente>`   | Mostra o agendamento ativo do cliente |
| DELETE | `/cancelarAgendamento/<id>`          | Cancela um agendamento                |

### Bloqueio

| Método | Rota          | Descrição                                |
| ------ | ------------- | ---------------------------------------- |
| POST   | `/bloquarDia` | Bloqueia um dia/horário para um barbeiro |

---

## 🔒 Segurança

- Senhas criptografadas com **bcrypt** antes de salvar no banco
- Variáveis sensíveis isoladas no arquivo `.env` (não versionado)
- CORS configurado para comunicação segura entre frontend e backend

---

## 📌 Status do Projeto

🚧 **Em desenvolvimento** — estrutura base do MVP concluída.

- [x] Modelagem do banco de dados
- [x] Backend completo (cliente, barbeiro, serviço, agendamento, bloqueio)
- [x] Fluxo completo do cliente: cadastro, login, busca de barbearias, agendamento, cancelamento
- [x] Fluxo completo do barbeiro: cadastro, login, configuração de serviços, calendário, bloqueio de horários
- [x] Cancelamento de agendamento pelo barbeiro
- [ ] Cancelamento de agendamento pelo cliente
- [ ] Estilização (CSS) de todas as páginas
- [ ] Notificação ao cliente em caso de cancelamento pelo barbeiro

---

## 👨‍💻 Autor

**Jorge Meert**
Estudante de Engenharia de Software — FIAP
[github.com/jorgemeert](https://github.com/jorgemeert)
