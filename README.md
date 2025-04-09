# EndPwner 🔥

**Scanner de Endpoints para APIs REST — rápido, flexível e simples.**  
Ferramenta desenvolvida para ajudar profissionais de segurança na enumeração de endpoints expostos em aplicações web.  
Ideal para fase de *recon* ou durante pentests de APIs.

---

## 🚀 Demonstração no terminal

```bash
$ python endpwner.py -u https://api.alvo.com -w wordlist.txt

  ______           _ _____                          
 |  ____|         | |  __ \                         
 | |__   _ __   __| | |__) |__  _ __ __ _ _ __ _   _ 
 |  __| | '_ \ / _` |  ___/ _ \| '__/ _` | '__| | | |
 | |____| | | | (_| | |  | (_) | | | (_| | |  | |_| |
 |______|_| |_|\__,_|_|   \___/|_|  \__,_|_|   \__, |
                                               __/ |
                                              |___/   v1.0
                                                   EndPwner

┏━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━┓
┃ Endpoint   ┃ Status   ┃ Tempo (s) ┃
┡━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━┩
│ /admin     │ 200      │ 0.13      │
│ /login     │ 401      │ 0.11      │
│ /debug     │ 403      │ 0.10      │
│ /secret    │ 404      │ 0.09      │
└────────────┴──────────┴───────────┘
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
🔗 [LinkedIn](https://www.linkedin.com/in/caiohacker)  
🐙 GitHub: [@caiohacker](https://github.com/caiohacker)

---

## 🧠 Licença

MIT — Faça o que quiser, só não diga que foi você que fez 😎
