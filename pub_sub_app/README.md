# Publish/Subscribe Pattern in Distributed Systems

## Overview

O Padrão de arquitetura Pub/Sub é um paradigma de troca de mensagens onde Publicadores de mensagens (publishers) não são programados para enviar suas mensages para assinantes específicos (subscribers). Em sistemas Pub/Sub, as mensagens são publicadas para tópicos sem o conhecimento de qualquer assinante. Os assinantes expressam interesse em um ou mais tópicos e, somente, recebem messagens de seu interesse, sem o conhecimento de quem publicou.

### Benefícios dessa Arquitetura

- Desacoplamento: Publicadores e Assinantes estão desacoplados, isto é, não se conhecem.
- Escalabilidade: O sistema é facilmente escalável, uma vez que novos assinantes e publicadores podem ser adicionados sem um afetar o outro.
- Flexibilidade: Assinantes podem processar mensagens de acordo com a maneira que cada um requerir.

# Example Flask Pub/Sub Application

É apresentado um exemplo de aplicação Flask no padrão Pub/Sub como um único serviço. O exemplo tem como objetivo provê um entendimento conceitual do padrão Pub/Sub.

## Features

- Tópicos pré-definidos: A aplicação inicia com um conjunto de tópicos válidos, simulando os "canais" de distribuição de mensagens.
- Subscription: Os clientes podem inscrever-se para esses tópicos, indicando seu interesse em receber mensagens relacionadas a esses tópicos.
- Publishing: Publicados enviam mensagens para um tópico específico.
- Recuperação da Informação: Um endpoint */info* permite listar o estado atual dos tópicos, assinantes e mensagens publicadas.

## Passos para Executar Local

- Certifique-se de que Python e Flask estejam instalados. Preferencialmente, use um ambiente para desenvolver cada projeto.
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

## Interagindo com a aplicação

Utilize o Postman com requisição:

- GET para a rota */info*
- POST para as rotas */subscribe* e */publish*. 

Para a primeira, envie um json no formato

```
{"topic": "sports", "callback_url": "soccer"}
```

já para a segunda rota, envie jsons no formato

```
{"topic": "sports", "message": "Breaking News!"}
```

# Exercício para entrega

1. Após se familiarizar com essa simples aplicação, você deverá apresentar um desenho mostrando como é o fluxo da informação, isto é, como é feita a troca de mensagens pelo sistema. Explique seu esquema.

2. Como o padrão Publish/Subscribe difere do padrão mais simples Request/Response presente em aplicações web?

3. Dado que a aplicação usa tópicos pré-definidos, o que acontece se um cliente tenta assinar um tópico que não está pré-definido?

4. A aplicação Flask simula o uso de **callbacks** com simples declarações "print". Entendendo o propósito de uma callback, qual é a importância da utilização delas em um sistema no padrão Pub/Sub?

5. O exemplo não possui uma maneira do assinante cancelar sua assinatura. Proponha uma solução que implemente essa nova configuração, considerando os princípios RESTful. Você não precisa implementar código, mas você deve descrever o que deverá ser alterado e adicionado para que essa nova feature possa ser implementada.