# Instruções para o Docker sobre como construir a imagem do aplicativo Flask, 
# incluindo a configuração do ambiente Python, a instalação de dependências 
# e a inicialização do aplicativo.

# A variante "slim" é uma imagem mínima que reduz o tamanho da imagem final.
FROM python:3.10-slim

# Define o diretório de trabalho dentro do contêiner para /app.
# Todos os comandos subsequentes serão executados neste diretório.
WORKDIR /app

# -- Instala as dependências
# Atualiza o pip para a versão mais recente.
RUN pip install --upgrade pip

# Copia o arquivo requirements.txt do host para o contêiner em /app.
COPY ./requirements.txt /app/requirements.txt

# Instala todas as dependências do Python especificadas em requirements.txt.
RUN pip install -r requirements.txt

# -- Copia os arquivos do projeto
# Copia o projeto inteiro do host para o diretório /app no ​​contêiner.
COPY . /app

# Especifiqua o comando a ser executado quando o contêiner iniciar.
# Aqui, ele executa o aplicativo Flask localizado em src/app.py usando python3.
CMD ["python3", "src/app.py"]
