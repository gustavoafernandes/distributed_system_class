# Using Padrões de Projeto (Design Patterns)

Os Padrões de Projeto são uma parte crucial da engenharia de software, fornecendo soluções generalizadas e reutilizáveis ​​para problemas comuns encontrados no projeto de software. Eles representam as melhores práticas, evoluídas através da experiência coletiva de engenheiros de software qualificados ao longo do tempo, e são categorizados em três tipos principais: **padrões de criação**, **estruturais** e **comportamentais**.

Ao criar aplicações distribuídas, basicamente usamos frameworks, que nos forçam à utilização de alguns padrões.

Ao aproveitar esses padrões, os desenvolvedores podem evitar armadilhas comuns, reduzir o tempo de desenvolvimento e construir sistemas mais robustos, escaláveis ​​e de fácil manutenção.

Vale a pena estudar mais em: https://refactoring.guru/design-patterns

## Tecnologias Utilizadas

**Flask**: Um microframework web escrito em Python, usado para construir aplicações web facilmente e com código mínimo.

**Python**: Uma linguagem de programação de alto nível, interpretada, conhecida por sua facilidade de uso e legibilidade.

**Métodos HTTP**: A aplicação demonstra o uso do método GET para recuperar e enviar dados.

## Organização do projeto

* examples/*.py: Contém exemplos de alguns padrões de projetos comuns em vários frameworks, inclusive no Flask.
* src/app.py: Uma aplicação Flask.

## Visão Geral

Vamos imaginar uma aplicação web básica que fornece informações sobre diversos tipos de veículos. O aplicativo terá as seguintes funcionalidades:

- **Factory**: cria objetos dinamicamente com base na solicitação. Usaremos isso para criar objetos de veículo.
- **Adapter**: certifica-se de que interfaces incompatíveis funcionem juntas. Adaptaremos objetos de veículo a uma interface comum para nossa aplicação web.
- **Decorator**: Adiciona novas funcionalidades aos objetos. Usaremos decoradores de rota Flask e também mostraremos como aplicar decoradores personalizados para recursos adicionais, como logs.

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

Pratique e estude bastante. :rocket:

### Exercício para entrega

## 1. TODO

Após se familiarizar com os exemplos, você deverá encontrar a marcação "TODO" em *example\_2.py* e você deverá implementar o Decorator vanilla (baunilha) simulando aumentar o sabor no café. Esse Decorator deve implementar o mesmo padrão dos anteriores, adicionando custo (cost) e descrição (description). Você deverá entregar todo o arquivo *example\_2.py* atualizado com um exemplo implementado do seu novo Decorator.

## 2. Python e Flask

Após executar e interagir com a aplicação Flask, responda:

- 2.1 Em geral, qual é a importancia de usar Design Patterns?

- 2.2 Como os padrões de projeto usados ​​no exemplo em Flask podem ser aplicados para aprimorar a escalabilidade e a confiabilidade de um sistema distribuído? A sua resposta deve contemplar os três padrões de projeto usados no exemplo em Flask.