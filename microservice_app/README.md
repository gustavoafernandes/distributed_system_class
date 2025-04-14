# Microservice Flask app

Esta aplicação apresenta um exemplo em Flask, sobre a **arquitetura baseada em Microsserviços**. Ela permite ao usuário cadastrar livros por meio de um formulário web, assim como adicionar livros a um carrinho de compra. Essa última funcionalidade está implementada de maneira simplista. Todas as requisições são armazenadas no Redis. A aplicação roda em contêineres Docker para garantir desacoplamento e facilidade em manutenção e escalabilidade, em relação aos serviços e sua base de dados.

## Microsserviços
1) várias fontes do código, isto é, as suas funcionalidades são implementadas em projetos distintos. Veja que cada serviço tem seu próprio código-fonte e um Docker para sua configuração. Aqui usamos um único repositório, apenas por simplicidade. Porém, cada serviço poderia ter facilmente seu próprio repositório.
2) Os componentes são totalmente independentes, mesmo que algum faça requisição para outro, o que é comum, as lógicas-base de cada um e suas execuções estão completamente independentes. Alterar a lógica de um serviço não causa alteração em outro, o que permite escalar aplicação de forma mais agradável. Perceba, também, que cada serviço possui seu próprio banco de dados(*).
3) Entretanto o projeto se torna complexo à medida que o número de funcionalidades aumenta, pois haverão vários repositórios e várias tecnologias distintas que precisam ser integradas.

(*) **Nota**: Aqui, neste exemplo, o Redis é executado como uma única instância (contêiner), mas oferece suporte a vários bancos de dados lógicos na mesma instância. Ao criar um cliente Redis no nosso app Flask, ao especificar "db=0", significa que você está se conectando ao primeiro banco de dados lógico. Em um ambiente de produção, separar fisicamente os bancos de dados se alinha mais de perto com o paradigma de microsserviços, garantindo que cada serviço permaneça verdadeiramente autônomo.

* Após conectar no Redis, (veja o projeto [Intro Containerized App](https://github.com/gustavoafernandes/distributed_system_class/tree/main/intro_containerized_app)):
1. selecione a base lógica de interesse, por exemplo, selecionar a base do carrinho de compras:
```
SELECT 1
```
2. liste todas as chaves relacionadas ao carrinho:
```
KEYS cart:*
```

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

- Acesse a aplicação via browser: http://127.0.0.1:8080/books. Se estiver no Codespace, atente-se ao endereço fornecido.

- Em caso de alteração na aplicação Flask, você pode, via Compose:
```
docker-compose up --build
```

Esse último comando re-cria a imagem Docker em caso de alteração (na aplicação Flask) e reinicia o contêiner.

# Exercícios para entrega

Você deve interagir com a applicação, assim como estudar o código fonte para entender a importância do Docker, bem como entender como a aplicação foi desacoplada em relação a sua versão Monolítica do projeto [Intro Containerized App](https://github.com/gustavoafernandes/distributed_system_class/tree/main/intro_containerized_app). Foque, inicialmente, nas rotas de cada serviço, e como elas interagem entre si. Não se procupe com toda a lógica aqui implementada. Analise primeiro as rotas dos serviços book-service e cart-service. Após compreender, veja como o api-gateway gerencia o acesso aos recursos dos outros serviços.

1. Faça um desenho mostrando os três componentes da aplicação: api-gateway, book-service, cart-service. No seu desenho, mostre quem recebe as requisições, por qual porta e rota. Toda vez que algum componente receber uma requisição e/ou responder uma requisição, mostre esse fluxo por meio de setas no seu desenho. Pense em algo como: 
- nome do serviço e sua respectiva porta sobre um desenho que representa um bloco, 
- e dentro desse bloco apresente todas as rotas.
2. Qual é o papel do serviço api-gateway? Pesquise para responder.