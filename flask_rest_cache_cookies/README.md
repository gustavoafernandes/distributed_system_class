# RESTful API: Cache & Cookies

Esta página apresenta uma simples API em Flask, cujo objetivo é seguir os princípios RESTful, fornecendo uma interface CRUD **completa**. Agora, o objetivo é entender como funciona um serviço web que utiliza cache em ambos os lados, cliente e servidor, assim como entender os famosos cookies.

# Organização do projeto

* src/app.py: A aplicação Flask, isto é, nosso serviço. Para utilizar, lembre-se de instalar via pip as dependências.

### Depedências

:warning: Lembre-se de instalar as dependências desse exemplo: flask, flask_caching, flasgger.

## Caching

Neste exemplo, usamos a extensão Flask-Caching com um cache simples em memória (SimpleCache). Decoramos nossos endpoints GET para armazenar respostas em cache por 60 segundos. Sempre que um recurso é criado, atualizado ou excluído, limpamos o cache relevante para que os clientes (browser) vejam os dados atualizados.

O cache pode ocorrer em várias camadas, e o exemplo que implementamos usa cache do lado do servidor e cache do lado do cliente (browser).

### Server‑Side vs. Client‑Side Caching

- Cache do lado do servidor (Flask-Caching):

Quando uma solicitação (requisição) é feita para um endpoint em cache (usando o decorador @cache.cached), o servidor verifica se já tem uma resposta armazenada na memória, por exemplo.

Se uma resposta em cache existir (*cache hit*), ela será retornada imediatamente sem re-executar a lógica do endpoint. Isso reduz o tempo de processamento e a carga no servidor. Esse cache é transparente para o cliente; o cliente simplesmente recebe uma resposta HTTP válida. Ele não sabe que os dados vieram de um cache no servidor.

Para endpoints que modificam dados (POST, PUT, DELETE), limpamos as respostas em cache usando *cache.delete_memoized()*. Isso garante que tanto o servidor quanto o cliente eventualmente recebam dados atualizados.

- Cache do lado do cliente (browser):

Os navegadores armazenam em cache as respostas com base em cabeçalhos HTTP, como Cache-Control, por exemplo.

Se esses cabeçalhos forem definidos pelo servidor, o navegador pode armazenar a resposta localmente e reutilizá-la para solicitações idênticas subsequentes, o que pode reduzir a latência da rede e melhorar o desempenho percebido.

Em nosso exemplo de aplicativo Flask, adicionamos uma função *after-request* que anexa um cabeçalho “Cache-Control” com uma idade máxima de 20 segundos a todas as respostas GET. Isso informa ao navegador para armazenar a resposta em cache por 20 segundos, isto é, durante os próximos 20 segundos a mesma resposta do serviço é reutilizada, para aquele mesmo endpoint GET.

### Interação entre o cache do cliente e do servidor

Enquanto o cache do lado do servidor acelera as respostas no backend, o cache do lado do cliente (por meio de cabeçalhos) reduz o tráfego de rede redundante e acelera as solicitações subsequentes do navegador.

O mecanismo de cache do cliente funciona de forma independente - se o cliente (ou navegador) armazena em cache uma resposta com base no cabeçalho, ele pode servir essa cópia em cache sem buscar novamente no servidor até que o cache expire (20 segundos neste caso).

## Cookies

Cookies são pequenas quantidades de dados que um servidor envia para um cliente (geralmente um navegador). Eles são armazenados no cliente e são incluídos em solicitações subsequentes ao servidor. Cookies são comumente usados ​​para gerenciamento de sessão, armazenamento de preferências do usuário ou rastreamento do comportamento do usuário.

Diferentemente do cache do lado do servidor, os cookies residem no navegador do cliente. Lembrem-se, RestFull é *stateless*, isto é, a API não armazena dados de sessão.

Como cookies são armazenados no disco, é possível recuperá-los, enquanto estiverem disponíveis. Cada navegador gerencia esses arquivos internamente. No Google Chrome, após abrir o **Developer Tools** (F12) do seu navegador, realize uma requisição que salva um cookie, vá para a aba "Application". Em "Storage" procure por "Cookies". Verifique se o cookie enviado da API para o cliente foi salvo. Espere o tempo de vida do cookie e procure novamente.

# Exercício para entrega

1. Qual a diferença entre *cache hit* e *cache miss*? **Pesquise para responder**. Além disso, explique pelo nosso exemplo, quando acontece *cache hit* e *cache miss*.
2. Qual é a função dos cabeçalhos **Cache-Control** e **Expires** no cache do lado do cliente? **Pesquise para responder**.
3. Que diferenças você observa ao executar uma atualização forçada (usando F5) em comparação a uma atualização normal? Use o **Developer Tools** (F12) do seu navegador. Explore a aba *Network* e analise as informações em cada requisição. Compare o comportamento do browser quando você habilita ou desabilita o cache.
4. Quais são os possíveis problemas do armazenamento em cache de respostas de API, especialmente em cenários onde os dados mudam com frequência?
5. Há o seguinte comentário na sessão sobre cookies: *"Cookies são comumente usados ​​para gerenciamento de sessão, armazenamento de preferências do usuário ou rastreamento do comportamento do usuário."*. Você poderia apresentar alguns exemplos específicos em que podemos usar Cookies? Apresente pelo menos dois casos de uso.