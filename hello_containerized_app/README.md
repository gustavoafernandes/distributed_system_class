# Containerized applications

Esta aplicação apresenta um exemplo em Flask que permite ao usuário submeter mensagens por meio de um formulário web. Essas mensagens são armazenadas no Redis, um banco NoSQL *in-memory*, demonstrando um básico uso de integração entre uma aplicação web com um banco de dados. A aplicação roda em contêineres Docker para garantir desacoplamento e facilidade em manutenção e escalabilidade.

## Docker

Docker é uma plataforma aberta para desenvolver, enviar e executar aplicações. Ela permite que o desenvolvedor separe a aplicação da infraestrutura permitindo uma entrega rápida. O Docker Compose é uma ferramenta para definir e executar aplicações Docker com vários contêineres. Com o Compose, você usa um arquivo YAML para configurar os serviços, redes e volumes da sua aplicação e, em seguida, cria e inicia todos os serviços da sua configuração com um único comando.

- Instale o docker em sua máquina local (ou ambiente virtual). Siga um dos passos abaixo:
   - *https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository*, ou
   - https://docs.docker.com/desktop/

- Os comandos Docker que mais usaremos são:
   - sudo docker image build -t image-name .
   - sudo docker image ls
   - sudo docker container ls -a
   - sudo docker container ps
   - sudo docker run [OPTIONS] image-name (ou image-id)
   - sudo docker stop (ou start) image-name (ou image-id)
   - sudo docker rm image-name (ou image-id)
   - sudo docker image rm image-name (ou image-id)

Você também pode instalar um plugin Docker na sua IDE para gerenciar suas imagens e contêineres.

## Passos para Executar Local

- Certifique-se de que Python, Docker, Flask e Redis estejam instalados. Preferencialmente, use um ambiente para desenvolver cada projeto.
   - Flask e Redis podem ser instalados via *pip*,
   - já o Python e Docker pelo gerenciador do SO.

- Caso deseje usar o Codespace, o Docker e Docker Compose já estão instalados no ambiente.

- Após configurar o repositório localmente, navegue até o diretório raíz do projeto.

- Crie as Imagens Docker:
```
docker-compose build
```

- Inicie os contêineres Docker da aplicação. Com isso a aplicação Flask ficará conectada com o Redis, permitindo a comunicação entre os dois contêineres:
```
docker-compose up
```

- Acesse a aplicação via browser.

- Para interagir com o Redis, via linha de comando:

```
docker exec -it <redis-container-name ou redis-container-id> redis-cli
```
- Use `lrange <key> 0 -1` para listar todos os elementos da lista armazenada sobre a chave *"key"*.
   - exemplo:
   ```
   lrange messages 0 -1
   ```

- Em caso de alteração na aplicação Flask, apague os contêineres via comandos Docker ou uando o plugin. Mas você também pode, via Compose:
```
docker-compose up --build
```

Esse último comando re-cria a imagem Docker em caso de alteração (na aplicação Flask) e reinicia o contêiner.

## Passos para Executar usando o Github Codespace

O [Codespace](https://github.com/codespaces) é um ambiente de desenvolvimento em nuvem.

- No repositório do Github, clique em "Code".
- Em seguida, clique na aba "Codespaces".
- Clique em "Create Codespace" para criar uma nova instância.
- Execute a aplicação conforme os comandos anteriores em Execução Local.
- Atente-se ao endereço disponibilizado em "PORTAS", assim como, deixe a visibilidade do endereço web como "Público".

:warning: **Atenção!** Desligue a sua instância do Codespace, uma vez que você possui um [limite mensal gratuito de utilização](https://docs.github.com/en/codespaces/overview#billing-for-codespaces).

# Exercício para entrega [WIP]

Você deve interagir com a applicação, assim como estudar o código fonte, com o intuito de entender a importância do Docker em desacoplar os componentes. Em seguida, você deverá responder:

