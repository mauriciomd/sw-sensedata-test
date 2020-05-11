## Flask App:

### Descrição:
- Aplicativo flask para visualizar dados do [SWAPI](https://swapi.dev/). Páginas da aplicação:
  - /: Apresenta a listagem com os personagens retornados pela rota ``/people`` da api. São exibidos os campos ``name, gender, weight e height`` dos personagens. Esta página apresenta:
    - Ordenação dos dados: ao clicar sobre o header do campo, os dados são apresentados de maneira ordenada.
    - Paginação: são exibidos 10 itens por página.
    - Filtros: é possível filtrar os personagens por ``planet, starship, vehicle ou film``.
  - /starships: apresenta uma tabela com todas as starships listadas pela rota ``/starships`` da api. São exibidos os campos de ``name, model, hyperdrive_rating, cost_in_credits e score``.
    - Os dados retornados são listados em ordem decrescente de ``score``, sendo este calculado pelo resultado de ``hyperdrive_rating / cost_in_credits``.

### Dependências:
- Todas as dependências estão contidas no arquivo requeriments.txt
  - ``pip3 install -r requeriments.txt``