# EndPwner 🔥

**Scanner de Endpoints para APIs REST — rápido, flexível e simples.**  
Ferramenta desenvolvida para ajudar profissionais de segurança na enumeração de endpoints expostos em aplicações web.  
Ideal para fase de *recon* ou durante pentests de APIs.

---


## 🚀 Features

- 🔥 Brute-force de endpoints com wordlist
- 🛡️ Avaliação de headers de segurança (7 principais)
- 📊 Exporta resultado em CSV (compatível com Excel)
- 🧠 Ranking de segurança estilo CVSS (A+ até F)
- ⚡ Interface colorida com Rich

---

## 🧠 Avaliação de Segurança (Ranking)

O ranking é baseado na presença dos **headers de segurança** abaixo:

- `Content-Security-Policy`
- `Strict-Transport-Security`
- `X-Content-Type-Options`
- `X-Frame-Options`
- `X-XSS-Protection`
- `Referrer-Policy`
- `Permissions-Policy`

### 🎯 Classificação dos endpoints:

| Headers Presentes | Nota            |
|-------------------|-----------------|
| 7                 | `A+ - Excelente`|
| 5-6               | `A - Alto`      |
| 3-4               | `B - Médio`     |
| 1-2               | `C - Baixo`     |
| 0                 | `F - Nenhum`    |

---


## 🚀 Demonstração no terminal

```bash
$ python endpwner.py -u https://api.alvo.com -w wordlist.txt


 _____           _                               
| ____|_ __   __| |_ ____      ___ __   ___ _ __ 
|  _| | '_ \ / _` | '_ \ \ /\ / / '_ \ / _ \ '__|
| |___| | | | (_| | |_) \ V  V /| | | |  __/ |   
|_____|_| |_|\__,_| .__/ \_/\_/ |_| |_|\___|_|   
                  |_|                            
    Endpoint Wordlist Bruteforcer - By Caio Luchetti
EndPwner rodando em: https://example.com/
Escaneando endpoints... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:06
     EndPwner - Resultados do Scanner de API      
┏━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━┓
┃ Endpoint     ┃ Status ┃ Tempo (s) ┃ Segurança  ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━┩
│ /            │ 200    │ 0.27      │ F - Nenhum │
│ /login       │ 404    │ 0.32      │ D - Fraco  │
│ /api/users   │ 404    │ 0.26      │ D - Fraco  │
│ /admin/panel │ 404    │ 0.34      │ D - Fraco  │
│ /status      │ 404    │ 5.35      │ D - Fraco  │
└──────────────┴────────┴───────────┴────────────┘

Scan finalizado. Resultados salvos em: resultados.csv

```

---

## 📦 Instalação

```bash
git clone https://github.com/seuusuario/endpwner.git
cd endpwner
pip install -r requirements.txt
```

---

## 🛠️ Como usar

```bash
python endpwner.py -u <URL da API> -w <wordlist.txt> [-t TIMEOUT] [-o output.csv]
```

- `-u`, `--url`: URL base da API alvo  
- `-w`, `--wordlist`: arquivo com lista de endpoints para testar  
- `-t`, `--timeout`: (opcional) timeout de cada request (default: 5s)  
- `-o`, `--output`: (opcional) nome do arquivo CSV de saída (default: resultados.csv)

---

## 📁 Exemplo de uso

```bash
python endpwner.py -u https://api.exemplo.com -w wordlist.txt -t 3 -o resultado.csv
```

---

## 📄 Output

Um arquivo `.csv` contendo:

```
Endpoint,Status,Tempo (s)
/admin,200,0.13
/login,401,0.11
/secret,404,0.09
```

---

## 🤖 Requisitos

- Python 3.7+
- rich
- requests

Instalável via:

```bash
pip install -r requirements.txt
```

---

## 👨‍💻 Autor

**Caio Luchetti**  
🔗 [LinkedIn](https://www.linkedin.com/in/caio-luchetti/)  
🐙 GitHub: [@cxiolz](https://github.com/cxiolz)

---

## 🧠 Licença

MIT — Faça o que quiser, só não diga que foi você que fez 😎
