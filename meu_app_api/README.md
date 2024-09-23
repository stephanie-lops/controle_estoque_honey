# [API] Honey Store: Parts Inventory
## Inventário de Peças de Roupas
**Autor: Stephanie Lopes**

Este projeto é o meu MVP da Sprint 1 do curso de **Desenvolvimento Full Stack Básico** da PUC RIO, 2024.

O objetivo aqui é listar os produtos de uma loja de roupas, com o intuito de registrar um inventário dos itens, entrada e saída de peças.

Utilizando 4 informações: nome do item, imagem, tamanho e quantidade.

Nessa coleção atual há 4 itens cadastrados na loja "Honey":
Button-Detail Shirt
Flared Skirt
Cargo Jeans
Soft Bra

Todos os itens estão disponíveis nos tamanhos PP, P, M, G, e GG.

---
## Como executar 

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

Criar ambiente virtual env:

```
python3 -m venv env
```

Ativar ambiente virtual env (Windows):

```
.\env\Scripts\activate
```

Instalar as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

```
(env)$ pip install -r requirements.txt
```

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.


---
## Como utilizar as rotas no Swagger

Para adicionar um item através da rota POST:
```
1 - Clicar em Try it out.
2 - Preencher os campos nome, quantity e size.
3 - Clicar em Execute.
```

Para editar um item através da rota PUT:

```
1 - Clicar em Try it out.
2 - Clicar no campo Request body.
3 - Selecionar tudo com ctrl A.
4 - Apagar.
5 - Colocar o código a seguir, editando os campos "originalName" e "originalSize" de acordo com o item que deseja editar:

{
  "originalName": "Button-Detail Shirt",
  "originalSize": "M",
  "nome": "Button-Detail Shirt",
  "size": "GG",
  "quantity": 5
}

6 - Clicar em Execute.
```

Para excluir um item através da rota DELETE:
```
1 - Clicar em Try it out.
2 - Preencher os campos nome e size.
3 - Clicar em Execute.
```