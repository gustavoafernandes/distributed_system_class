# Containerized applications

Esta aplicação apresenta um exemplo em Flask que permite ao usuário cadastrar livros por meio de um formulário web. Essas requisições são armazenadas no Redis, um banco NoSQL *in-memory*, demonstrando um básico uso de integração entre uma aplicação web com um banco de dados. A aplicação roda em contêineres Docker para garantir desacoplamento e facilidade em manutenção e escalabilidade, em relação ao serviço e sua base de dados. Esta aplicação possui uma **arquitura Monolítica**: 
- 1) única fonte do código base, isto é, todas as suas funcionalidades, incluindo a interface da web, lógica de negócios e acesso a dados reside em uma base de código. 
- 2) componentes são fortemente acoplados, isto é, para atualizar a maneira como os livros são manipulados ou alterar a lógica de armazenamento de dados, será necessário modificar o aplicativo central. Isso pode simplificar o desenvolvimento para aplicativos menores, mas torna o dimensionamento ou o isolamento de falhas mais desafiador em sistemas maiores.

## Redis
O Redis é um banco em memória e NoSQL, que também pode ser utilizado como cache ou *broker* de mensagens, conhecido por sua velocidade e flexibilidade. Ele usa uma estrutura de dados chave-valor, onde cada dado é associado a uma chave exclusiva. Essa chave é associada a um hash.

- Hash: Um hash é um valor gerado e deve identificar unicamente um elemento de um conjunto. É a chave usada pelo banco para qualquer manipulação daquele elemento. Na nossa aplicação, um hash é gerado, como no exemplo abaixo, pela chave "*book:1*":
````
"book:1" => {
    "id": "1",
    "title": "Flask Web Development: Developing Web Applications with Python",
    "author": "Miguel Grinberg",
    "published": "2018"
}
````

## Docker

Docker é uma plataforma aberta para executar aplicações. Ela permite que o desenvolvedor separe a aplicação da infraestrutura. O Docker Compose é uma ferramenta para definir aplicações Docker com vários contêineres. Com o Compose, você usa um arquivo YAML para configurar os serviços, redes e volumes da sua aplicação e, em seguida, cria e inicia todos os serviços da sua configuração com um único comando.

- Instale o docker em sua máquina local (ou ambiente virtual). Siga um dos passos abaixo:
   - *https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository*, ou
   - https://docs.docker.com/desktop/

- Os comandos Docker mais comuns são:
   - sudo docker image build -t image-name .
   - sudo docker image ls
   - sudo docker container ls -a
   - sudo docker container ps
   - sudo docker run [OPTIONS] image-name (ou image-id)
   - sudo docker stop (ou start) image-name (ou image-id)
   - sudo docker rm image-name (ou image-id)
   - sudo docker image rm image-name (ou image-id)

:warning: Você também pode instalar uma extensão Docker na sua IDE para gerenciar suas imagens e contêineres.

## Passos para Executar Local

- Certifique-se de que Python, Docker, Flask e Redis estejam instalados no seu ambiente.
   - Flask e Redis podem ser instalados via *pip*,
   - já o Python e Docker pelo gerenciador do SO.

- Se deseja usar o Codespace, o Docker e Docker Compose já estão instalados no ambiente.

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
- Use `smembers <set>` para listar todos os elementos do set armazenada sobre o nome *"key"*.
   - exemplo:
   ```
   smembers books
   ```

- Em caso de alteração na aplicação Flask, você pode, via Compose:
```
docker-compose up --build
```

Esse último comando re-cria a imagem Docker em caso de alteração (na aplicação Flask) e reinicia o contêiner.

# Exercícios para entrega

Você deve interagir com a applicação, assim como estudar o código fonte, com o intuito de entender a importância do Docker em desacoplar os componentes. Em seguida, você deverá responder:

1. Explique como o Flask interage com o Redis, isto é, quais são as rotas disponíveis e como elas interagem com o Redis? Não se preocupe em explicar os comandos do Redis, apenas atente-se ao que cada rota faz em sua interação com o Redis.

2. O que acontece se o Redis ficar temporariamente indisponível? Como isso afeta as funcionalidades da aplicação?

3. Explique como essa aplicação pode escalar para gerenciar aumento no tráfego de requisições. Quais componentes você escalaria? Pesquise sobre escalabilidade vertical VS horizontal para responder esta pergunta.

4. Pesquise sobre Balanceamento de Carga (*Load Balancing*). Em seguida, explique como você usaria o balanceamento de carga nesta aplicação. Use o contexto apresentado na sua resposta para a questão anterior.

5. Que tipo de problema pode aparecer em relação aos dados em aplicações distribuídas como esta? Mais especificamente, problemas relacionados a inconsitência dos dados na tentativa de escalar o banco.