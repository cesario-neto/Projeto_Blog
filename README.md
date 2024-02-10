# Projeto_Blog

Blog criado utilizando Django. (Incompleto)

## Como usar:
1. Clone o repositório
```
git clone https://github.com/cesario-neto/Projeto_Blog.git
```
2. Acesse o repositório
```
cd Pojeto_Blog
```
3. Crie um ambiente virtual python
```
python -m venv venv
```
4. Ative seu ambiente
- Windows
```
venv/scripts/activate
```
- linux, macOS
```
. venv/bin/activate
```

### Usando com docker
1. No repositório, use o comando:
```
docker-compose up
```

### Usando sem o docker
1. Instale as dependências
```
pip install -r app/requirements.txt
```
2. Prepare as migrações
```
python app/manage.py makemigrations
```
3. Faça as migrações
```
python app/manage.py migrate
```
4. Inicie o servidor
```
python app/manage.py runserver
```
