# 🛡️ EndPwner – API Recon & Header Scanner

**EndPwner** é uma ferramenta de segurança ofensiva focada em escaneamento de endpoints REST e análise de headers HTTP.  
Foi criada para apoiar atividades de reconhecimento, mapeamento de superfície de ataque e identificação de falhas de configuração em APIs.

Desenvolvida com foco em simplicidade, performance e clareza na visualização dos dados, é uma ótima adição para qualquer profissional de **Pentest**, **AppSec**, **Red Team** ou entusiasta de **bug bounty**.

---

## 📌 Funcionalidades

- 🔍 Escaneia endpoints via requisições HTTP `GET`
- ⏱️ Mede tempo de resposta de cada rota
- 🔐 Verifica presença de **headers de segurança**
- 📄 Exporta resultados em **CSV**
- 💡 Visualização colorida com **Rich** no terminal
- 🧩 Leitura de wordlists customizadas
- 🛑 Tolerante a erros de rede e timeouts

---

## 🧠 Motivação

Durante testes de segurança, muitas APIs expõem rotas sensíveis ou desprotegidas.  
O EndPwner surgiu da necessidade de:

- Automatizar o reconhecimento de endpoints
- Coletar evidências rápidas de falhas em headers
- Avaliar comportamento da aplicação com base nos códigos de resposta

---

## 🔐 Headers Avaliados

A ferramenta checa os seguintes headers de segurança (padrão OWASP + boas práticas modernas):

| Header                     | Descrição |
|---------------------------|-----------|
| Content-Security-Policy   | Mitiga ataques XSS e injeções de conteúdo |
| Strict-Transport-Security | Força conexões HTTPS |
| X-Content-Type-Options    | Bloqueia MIME sniffing |
| X-Frame-Options           | Previne clickjacking |
| X-XSS-Protection          | Proteção básica contra XSS |
| Referrer-Policy           | Controla envio de referers entre sites |
| Permissions-Policy        | Gerencia acesso a funcionalidades como câmera, microfone etc |

---

## 🛠️ Instalação

```bash
git clone https://github.com/seuuser/endpwner.git
cd endpwner
pip install -r requirements.txt
