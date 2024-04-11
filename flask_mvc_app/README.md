# MVC Architecture in Distributed Systems

Este exemplo em Flask utiliza a arquitetura Model-View-Controller (MVC). Essa arquitetura é amplamente usada para separar uma aplpicação em componentes inter-conectados: O Model, a View e o Controller.

Além da arquitetura MVC, nesta aplicação também é usado o **Object Relational Mapper** (ORM). ORM provê maneiras de mapear tabelas em classes, já que cada registro da tabela será um objeto da classe definida. Isso permite que os desenvolvedores usem uma maneira mais natural de interagir com o banco sem a necessidade de escrever SQL diretamente. O SQLAlchemy é uma biblioteca que provê uma interface para se trabalhar com ORM.

Uma outra tecnologia usada é a engine Jinja. Ela permite renderização dinâmica de páginas HTML, permitindo uma boa integração de estruturas de dados e lógica Python diretamente no HTML. Veja mais em:
- https://jinja.palletsprojects.com/en/3.1.x/templates/
- https://flask.palletsprojects.com/en/3.0.x/tutorial/templates/

## Overview

**Model**: Representa a estrutura de dados da aplicação, bem como a lógica de negócios relacionada ao gerenciamento desses dados. Os Models são responsáveis por acessar, modificar os dados no banco de dados, e aplicar regras de negócio específicas.

**View**: Gerencia a apresentação dos dados para o usuário. Elas geram uma interface, que apresenta o modelo dos dados para o usuário, capturam a interação do usuário e a delegam para o Controller. As ações do usuário na interface são capturadas por elementos da View (como botões ou formulários), mas é o Controller que define como essas ações serão tratadas.

**Controller**: Age como uma camada intermediária entre a View e o Model. Ele recebe as requisições do usuário, as processa (geralmente com a ajuda dos Models) e determina a saída que será renderizada pela View.

## Passos para Executar Local

- Certifique-se de que Python, Flask e Flask-SQLAlchemy estejam instalados. Preferencialmente, use um ambiente para desenvolver cada projeto.
- Navegue até o diretório da aplicação Flask.
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
- Execute a aplicação conforme o comando anterior para Execução Local.
- Atente-se ao endereço disponibilizado em "PORTAS", assim como, deixe a visibilidade do endereço web como "Público".

:warning: **Atenção!** Desligue a sua instância do Codespace, uma vez que você possui um [limite mensal gratuito de utilização](https://docs.github.com/en/codespaces/overview#billing-for-codespaces).

# Exercício para entrega

Você deve interagir com a applicação, assim como estudar o código fonte, com o intuito de entender a arquitetura MVC. Em seguida, você deverá responder:

1. Explique como a rota **/add** funciona. Dê detalhes sobre o método HTTP usado e como essa rota interage com o código html.

2. Explique como a função JavaScritpt **deleteNote** interage com a aplicação Flask. Descreva o processo a partir do momento que o usuário clica no botão *Delete* até a completa remoção da nota.

3. Discuta a importância de usar diferentes métodos HTTP em aplicações Web.

4. Nesta aplicação, explique quem representa o Model, quem representa o Controller e quem representa a View, uma vez que a aplicação usa a arquitetura MVC.

5. Quais as vantagens da arquitetura MVC em aplicações Web? 

6. Como a arquitetura MVC pode ser usada de forma distribuída, isto é, em sistemas distribuídos?