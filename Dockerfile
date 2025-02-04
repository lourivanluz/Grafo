# Usa uma imagem Python com bibliotecas essenciais
FROM python:3.10-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Instala dependências do sistema (necessárias para greenlet)
RUN apt-get update && apt-get install -y build-essential libpq-dev gcc && rm -rf /var/lib/apt/lists/*

# Copia os arquivos do projeto para o container
COPY . .

# Cria e ativa um ambiente virtual
RUN python -m venv venv
RUN . venv/bin/activate

# Instala as dependências do projeto
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expõe a porta padrão do Flask
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
