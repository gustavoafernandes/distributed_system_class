# Simple Flask Application for Distributed Systems Class

Esta página apresenta uma simples API em Flask. O objetivo é entender os conceitos básicos do Flask ao tratar as requisições HTTP GET e POST, principalmente.

Esta aplicação Flask é um exemplo básico para demonstrar os conceitos de API REST, rotas, programação em Python e métodos HTTP. Ela é projetada como uma ferramenta introdutória para ensinar estudantes sobre os fundamentos do desenvolvimento web e sistemas distribuídos.

## Tecnologias Utilizadas

**Flask**: Um microframework web escrito em Python, usado para construir aplicações web facilmente e com código mínimo.

**Python**: Uma linguagem de programação de alto nível, interpretada, conhecida por sua facilidade de uso e legibilidade.

**Métodos HTTP**: A aplicação demonstra o uso dos métodos GET e POST para recuperar e enviar dados.

## RESTful

As APIs estão em toda parte na Internet. Cada vez que você usa aplicações na Internet, as requisições da API são solicitadas. Algumas dessas APIs são serviços em execução, chamados serviços **RESTful**. Nesses serviços, tanto os dados quanto as funcionalidades são considerados **recursos** e ficam acessíveis aos clientes através da utilização de **URIs** (*Uniform Resource Identifiers*), que normalmente são endereços na web que identificam tanto o servidor no qual a aplicação está hospedada quanto a própria aplicação e qual dos recursos oferecidos está sendo solicitado.

Os recursos disponíveis em um serviço RESTful podem ser acessados ou manipulados a partir de um conjunto de operações predefinidas pelo padrão RESTful, utilizando o protocolo HTTP.

Quando um desenvolvedor cria uma API, ela precisa ser testada quanto à sua qualidade. Existem muitos elementos que compõem o teste de uma API, desde a verificação de requisitos funcionais até o desempenho, confiabilidade e segurança do serviço.

Também existem muitas ferramentas populares para permitir testes rápidos de API, como o **Postman**, uma ferramenta que pode ajudar no processo de teste de um desenvolvedor de APIs.

## Organização do projeto

* src/app.py: A aplicação Flask, isto é, nosso serviço. Leia mais em *https://flask.palletsprojects.com/en/3.0.x/*.

## Visão Geral

A aplicação consiste em um armazenamento simples de mensagens e duas rotas:

- Uma rota inicial (/) que exibe uma mensagem.
- Uma rota de envio (/send) que permite aos usuários postar uma nova mensagem.

## Passos para Executar Local

- Certifique-se de que Python e Flask estejam instalados. Para instalar o Flask, por exemplo, podemos usar o comando abaixo. Preferencialmente, use um ambiente para desenvolver cada projeto.
```
pip install flask
```
- Navegue até o diretório da aplicação Flask.
```
cd hello_world
```
- Execute o script usando o comando:
```
python src/app.py
```
- Abra um navegador web e vá para http://localhost:5000 ou http://0.0.0.0:5000.

## Passos para Executar usando o Github Codespace

O [Codespace](https://github.com/codespaces) é um ambiente de desenvolvimento em nuvem.

- No repositório do Github, clique em "Code".
- Em seguida, clique na aba "Codespaces".
- Clique em "Create Codespace" para criar uma nova instância.
- Execute a aplicação conforme o comando anterior para Execução Local. Lembre-se de instalar o Flask.
- Atente-se ao endereço disponibilizado em "PORTAS", assim como, deixe a visibilidade do endereço web como "Público".

:warning: :warning: **Atenção!** Desligue a sua instância do Codespace, uma vez que você possui um [limite mensal gratuito de utilização](https://docs.github.com/en/codespaces/overview#billing-for-codespaces).

## Postman

Postman ajuda a pessoa desenvolvedora da API a organizar requisições de API dentro de Coleções. Após criar a conta, você deverá criar uma coleção de requisições. Acesse https://www.postman.com/ e crie uma conta e/ou faça o download da aplicação. Você também pode, por exemplo, instalar uma extensão na sua IDE.

- Na IDE VSCode, clique sobre a extensão do Postman já instalada. Caso não tenha instalado, instale a extensão.
- Faça a autenticação.
- Crie uma nova coleção.
- Adicione uma nova "request".
- Configure da seguinte maneira:
   - Método: POST
   - URL: Endereço local ou endereço via Codespace. *Não se esqueça da rota correta e de alterar a visibilidade do endereço disponibilizado pelo github!*
   - Em "Body", formate uma mensagem 'raw' json com a seguinte estrutura: {"message": "Hello, World!"}
   - Clique em "Send". Analise a resposta da API.

Pratique e estude bastante. :rocket:

## 1. Exercício para entrega

Após se familiarizar com essa simples aplicação, você deverá responder as seguintes perguntas.

### Python e Flask

1. Como o objeto *request* do Flask funciona e como ele é usado na função *send_message*?
2. Que estrutura de dados define a variável *message_store*?
3. Discuta como a variável *message_store* é usada dentro da aplicação. Quais são as limitações de usar tal método de armazenamento em um sistema distribuído?
4. O que acontece na linha 17, caso a chave "message" não exista no dict "message"? Para responder, faça um teste prático com esta aplicação e adicione à sua resposta um *print* que corrobore a sua explicação.

### HTTP
1. Quais são os papéis dos métodos HTTP GET e POST em aplicações web, e como eles são demonstrados nesta aplicação Flask? Isto é, quais funções e rotas estão relacionadas aos métodos GET e POST?
2. Explique os conceitos de *stateless* e *stateful* no HTTP e como isso afeta o gerenciamento de dados em aplicações web.
3. Descreva o papel dos códigos de status HTTP.

### Routing e REST APIs
1. O que é uma rota em uma aplicação web, e como as rotas são definidas no Flask?

### Sistemas Distribuídos
1. Como o simples armazenamento de mensagens nesta aplicação poderia ser adaptado para um sistema distribuído escalável? Ou seja, um sistema que armazena as novas mensagens.
2. Quais desafios surgiriam ao tornar esta aplicação Flask altamente disponível e tolerante a falhas, após a adaptação anterior?

## 2. Exercício opcional

Você pode aprimorar essa aplicação para que a estrutura que armazena as mensagens no backend contenha uma lista de mensagens, porém ainda usando a chave "messages". Com isso ao solicitar a rota "/" a lista de mensagens deve ser retornada. E, ao realizar um POST na rota "/send" contendo uma nova mensagem, essa nova mensagem é inserida e a lista de mensagens é atualizada.