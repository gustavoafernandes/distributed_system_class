# RESTful API

Esta página apresenta uma simples API em Flask, cujo objetivo é seguir os princípios RESTful, fornecendo uma interface CRUD **completa**. REST é um estilo de arquitetura de software que impõe condições sobre como uma API deve funcionar. Uma interface de programação de aplicação (API) define as regras para se comunicar com outros sistemas de software, sendo que para RESTful, a comunicação é entre clientes e recursos.

Um serviço RESTful completo adere a um conjunto de restrições e melhores práticas que, juntas, garantem escalabilidade, simplicidade e uma clara separação de preocupações (*Separation of Concerns*). A seguir, comenta-se o que normalmente é esperado.

## 1. **Arquitetura cliente-servidor**
Separação de preocupações: o cliente e o servidor são independentes. O cliente é responsável apenas pela interface do usuário e pelo estado do usuário, enquanto o servidor gerencia o armazenamento de dados e a lógica de negócios. Essa separação permite que ambos evoluam de forma independente.
## 2. **Ausência de estado (Statelessness)**
Solicitações autocontidas: cada solicitação do cliente deve conter todas as informações necessárias para processá-la. O servidor **não** armazena nenhum contexto do cliente entre as solicitações. Isso melhora a escalabilidade e a confiabilidade.
## 3. **Capacidade de cache**
Uso eficiente de recursos: as respostas devem definir claramente se podem ser armazenadas em cache ou não. Quando as respostas podem ser armazenadas em cache, os clientes ou intermediários (como *proxies*) podem reutilizá-las para reduzir a carga do servidor e melhorar o desempenho.
## 4. **Interface uniforme**
Esta é a base do REST e inclui vários princípios-chave:

**Identificação de Recursos**: Cada recurso é identificado exclusivamente por uma URL.

**Manipulação de Recursos por meio de Representações**: Os clientes interagem com os recursos trocando representações (normalmente JSON ou XML) que capturam o estado atual do recurso.

**Mensagens Autodescritivas**: Cada mensagem (solicitações e respostas) inclui informações suficientes (como métodos HTTP, cabeçalhos e códigos de status) para que o cliente ou servidor entenda como processá-la.

## 5. Sistema em Camadas
Modularidade e Escalabilidade: A API é projetada em camadas (por exemplo, balanceadores de carga, caches, camadas de segurança, serviços, etc). Cada camada só precisa saber sobre as camadas imediatamente adjacentes a ela, o que permite escalabilidade e gerenciabilidade.

## 6. Código sob demanda
Extensibilidade: Permite código sob demanda, onde o servidor pode estender ou personalizar temporariamente a funcionalidade do cliente enviando código executável (como JavaScript). Por exemplo, ao preencher um formulário de registro em qualquer site, o browser imediatamente destaca os erros cometidos, como números de telefone incorretos. Ele pode fazer isso devido ao código enviado pelo servidor.

## Práticas recomendadas
Uso correto de métodos HTTP e códigos de status:

- GET: recuperar um recurso.
- POST: criar um novo recurso.
- PUT/PATCH: atualizar um recurso existente.
- DELETE: remover um recurso.

Usar códigos de status adequados (por exemplo, 200 para sucesso, 404 para não encontrado, 201 para criação de recurso) ajuda o cliente a entender o resultado de cada operação.

**Segurança**: implementar autenticação, autorização e validação de entrada adequada para proteger recursos.

**Documentação**: documentação clara e acessível é essencial para que os clientes entendam como interagir com a API.

# Organização do projeto

* src/app.py: A aplicação Flask, isto é, nosso serviço. Para utilizar, lembre-se de instalar via pip as dependências.

# Exercício para entrega

1. Liste todos os *endpoints* definidos na aplicação e especifique quais métodos HTTP cada um suporta.
2. Em relação ao conceito de Interface Uniforme, como o agrupamento de operações para livros sobre /books está de acordo com esse conceito?
3. Na aplicação foi usado o Swagger (via [Flasgger](https://github.com/flasgger/flasgger)) para um propósito bem específico (acesse o *endpoint* /apidocs). Qual? Explique.
4. Você deverá criar uma rota para deletar um item da base. A rota deve ser no formato "/books/<int:book_id>". Atente-se à variável
'book_id'. A requisição é somente para DELETE. Implemente toda lógica necessária para a remoção do item. Use as implementações existentes como referência.