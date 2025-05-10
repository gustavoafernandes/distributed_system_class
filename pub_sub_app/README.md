# Publish/Subscribe Pattern in Distributed Systems

## Overview

O Padrão de arquitetura Pub/Sub é um paradigma de troca de mensagens onde Publicadores de mensagens (publishers) **não** são programados para enviar suas mensages diretas para assinantes específicos (subscribers). Em sistemas Pub/Sub, as mensagens são publicadas para tópicos sem o conhecimento de qualquer assinante. Os assinantes expressam interesse em um ou mais tópicos e, somente, recebem messagens de seu interesse, sem o conhecimento de quem publicou. Este padrão é baseado na arquitetura de Microsserviços.

### Benefícios dessa Arquitetura

- Desacoplamento: Publicadores e Assinantes estão desacoplados, isto é, não se conhecem.
- Escalabilidade: O sistema é facilmente escalável, uma vez que novos assinantes e publicadores podem ser adicionados sem um afetar o outro.
- Flexibilidade: Assinantes podem processar mensagens de acordo com a maneira que cada um requerir.

## Features

- Tópicos pré-definidos: A aplicação inicia com um conjunto de tópicos válidos, simulando os "canais" de distribuição de mensagens.
- Subscription: Os clientes podem inscrever-se para esses tópicos, indicando seu interesse em receber mensagens relacionadas a esses tópicos.
- Publishing: Publicadores enviam mensagens para um tópico específico.
- Recuperação da Informação: Um endpoint permite listar o estado atual das mensagens publicadas.
- O Redis faz o papel do barramento de mensagens (*message broker*). Uma única instância (serviço) é usada. Assim temos atualizações simples, de baixa latência e em tempo real, nas quais só se importa com os assinantes atuais.

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

- Inicie os contêineres Docker da aplicação. Com isso a aplicação Flask ficará conectada com o Redis, permitindo a comunicação entre os contêineres:
```
docker-compose up
```

- Acesse a aplicação via browser: http://127.0.0.1:5051/messages. Se estiver no Codespace, atente-se ao endereço fornecido.

- Em caso de alteração na aplicação Flask, você pode, via Compose:
```
docker-compose up --build
```

Esse último comando re-cria a imagem Docker em caso de alteração (na aplicação Flask) e reinicia o contêiner.

## Interagindo com a aplicação

1. Utilize o Postman com requisição POST para a rota */publish* com o json:

```
{"topic":"sports", "message":"Game tonight at 8PM"}
```

2. Faça outro teste usndo:

```
{"topic": "tech", "message":"Breaking News! New Gemini pro for free."}
```

# Exercício para entrega

1. Após se familiarizar com essa simples aplicação, você deverá apresentar um desenho mostrando como é o fluxo da informação, isto é, como é feita a troca de mensagens pelo sistema. Explique seu esquema.

2. Como o padrão Publish/Subscribe difere do padrão mais simples Request/Response presente em aplicações web?

3. Dado que a aplicação usa tópicos pré-definidos, o que acontece se um cliente publica um tópico que não está pré-definido? Faça esse teste usando o json abaixo e responda a pergunta. Seja completo em sua resposta.

```
{"topic":"cooking", "message":"New recipe for lasagna!"}
```

4. O exemplo não possui uma maneira do assinante cancelar sua assinatura. Proponha uma solução que implemente essa nova configuração, considerando os princípios RESTful. Você não precisa implementar código, mas você deve descrever o que deverá ser alterado e adicionado para que essa nova feature possa ser implementada. Descreva de forma clara onde deve haver alteração, como é a altereção e o que devemos criar.