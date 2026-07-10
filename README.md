# ✂️ CorteJá

> Plataforma de agendamento online para barbearias — conectando clientes e barbeiros de forma simples e direta.

🔗 **Deploy:** [barber-phi-mocha.vercel.app](https://barber-phi-mocha.vercel.app/)

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
- Visualização do agendamento ativo em calendário mensal
- Cancelamento de agendamento

### Barbeiro
- Cadastro com dados da barbearia (nome, localização, foto, telefone)
- Login
- Configuração dos serviços oferecidos e seus valores
- Calendário mensal com agendamentos recebidos
- Cancelamento de agendamentos
- Bloqueio de dias e horários indisponíveis

> ⚠️ **MVP:** A tela de configurações está em desenvolvimento e pode apresentar instabilidades. As demais funcionalidades estão operacionais.

---

## 🛠️ Tecnologias

**Backend**
- Python 3.13
- Flask
- Flask-SQLAlchemy (ORM)
- Flask-CORS
- PostgreSQL (produção) / SQLite (desenvolvimento)
- bcrypt (criptografia de senhas)
- python-dotenv
- Gunicorn

**Frontend**
- HTML, CSS, JavaScript (Fetch API)

**Infraestrutura**
- Backend: [Render](https://render.com)
- Frontend: [Vercel](https://vercel.com)
- Banco de dados: PostgreSQL (Render)

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
│   ├── extensions.py           # Instância do banco de dados (SQLAlchemy)
│   └── app.py                  # Inicialização da aplicação Flask
├── frontend/
│   ├── index.html              # Escolha: cliente ou barbeiro
│   ├── cliente/
│   │   ├── login.html
│   │   ├── barbearias.html
│   │   ├── agendamentos.html
│   │   ├── agendamento-ativo.html
│   │   ├── css/
│   │   └── JavaScript/
│   └── barbeiro/
│       ├── login.html
│       ├── config.html
│       ├── horarios.html
│       ├── calendario.html
│       ├── css/
│       └── JavaScript/
├── doc/                        # Histórias de usuário e backlog
├── Procfile                    # Configuração do Gunicorn para deploy
├── .gitignore
└── requirements.txt
```

---

## ⚙️ Como rodar localmente

**1. Clone o repositório**
```bash
git clone https://github.com/jorgemeert/barber
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

Crie um arquivo `.env` dentro da pasta `backend`:
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

Use a extensão **Live Server** no VS Code para abrir `frontend/index.html`.

---

## 📡 Endpoints da API

### Cliente
| Método | Rota | Descrição |
|--------|------|-----------|
| POST | `/cadastro` | Cadastro de cliente |
| POST | `/login` | Login de cliente |

### Barbeiro
| Método | Rota | Descrição |
|--------|------|-----------|
| POST | `/cadastroBarbeiro` | Cadastro de barbeiro |
| POST | `/loginBarbeiro` | Login de barbeiro |
| GET | `/barbearias` | Lista todas as barbearias |
| POST | `/pesquisarBarbearia` | Busca barbearia por nome |

### Serviço
| Método | Rota | Descrição |
|--------|------|-----------|
| POST | `/cadastroServico` | Cadastro de serviço |
| GET | `/servicos/<id_barbeiro>` | Lista serviços de um barbeiro |

### Agendamento
| Método | Rota | Descrição |
|--------|------|-----------|
| POST | `/agendarHorario` | Cria um novo agendamento |
| GET | `/mostrarAgendamentos/<id_barbeiro>` | Lista agendamentos de um barbeiro |
| GET | `/agendamentosAtivos/<id_cliente>` | Mostra o agendamento ativo do cliente |
| DELETE | `/cancelarAgendamento/<id>` | Cancela um agendamento |

### Bloqueio
| Método | Rota | Descrição |
|--------|------|-----------|
| POST | `/bloquarDia` | Bloqueia um dia/horário para um barbeiro |

---

## 🔒 Segurança

- Senhas criptografadas com **bcrypt** antes de salvar no banco
- Variáveis sensíveis isoladas no arquivo `.env` (não versionado)
- CORS configurado para comunicação segura entre frontend e backend

---

## 📌 Status do Projeto

🚧 **MVP concluído** — projeto desenvolvido individualmente ao longo de aproximadamente 2 meses.

- [x] Modelagem do banco de dados (5 entidades)
- [x] Backend completo com 13 endpoints REST
- [x] Autenticação com bcrypt
- [x] Fluxo completo do cliente: cadastro, login, busca, agendamento, cancelamento
- [x] Fluxo completo do barbeiro: cadastro, login, serviços, calendário, bloqueio
- [x] Calendário mensal interativo (cliente e barbeiro)
- [x] Deploy em produção (Render + Vercel + PostgreSQL)
- [ ] Tela de configurações de horários do barbeiro (em desenvolvimento)
- [ ] Notificação ao cliente em caso de cancelamento pelo barbeiro

---

## 👨‍💻 Autor

**Jorge Meert**  
Estudante de Engenharia de Software — FIAP  
[github.com/jorgemeert](https://github.com/jorgemeert)
