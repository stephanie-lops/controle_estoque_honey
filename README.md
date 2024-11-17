------- ENGLISH ---------

# [API] Honey Store: Parts Inventory
## Clothing Parts Inventory
**Author: Stephanie Lopes**

This project is my final MVP of Sprint 1 of the **Basic Full Stack Development** course at PUC RIO, 2024.

The goal here is to list the products of a clothing store, in order to record an inventory of items, input and output of parts.

Using 4 pieces of information: item name, image, size and quantity.

In this current collection there are 4 items registered in the "Honey" store:
```
Button-Detail Shirt
Flared Skirt
Cargo Jeans
Soft Bra
```
All items are available in sizes PP, P, M, G, and GG.

---
## How to run

You will need to have all the python libs listed in `requirements.txt` installed.
After cloning the repository, you need to go to the root directory, via the terminal, to be able to execute the commands described below.

> It is strongly recommended to use virtual environments of the [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) type.

Create virtual env environment:

```
python3 -m venv env
```

Activate virtual env environment (Windows):

```
.\env\Scripts\activate
```

Install the dependencies/libraries, described in the `requirements.txt` file.

```
(env)$ pip install -r requirements.txt
```

To run the API, simply run:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

In development mode, it is recommended to run using the reload parameter, which will automatically restart the server after a change in the source code.

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Open [http://localhost:5000/#/](http://localhost:5000/#/) in the browser to check the status of the API running.

---
## How to use routes in Swagger

To add an item through the POST route:
```
1 - Click on Try it out.
2 - Fill in the name, quantity and size fields.
3 - Click on Execute.
```

To edit an item using the PUT route:

```
1 - Click on Try it out.
2 - Click on the Request body field.
3 - Select all with ctrl A.
4 - Delete.
5 - Insert the following code, editing the "originalName" and "originalSize" fields according to the item you want to edit:

{
"originalName": "Button-Detail Shirt",
"originalSize": "M",
"nome": "Button-Detail Shirt",
"size": "GG",
"quantity": 5
}

6 - Click on Execute.
```

To delete an item using the DELETE route:
```
1 - Click on Try it out.
2 - Fill in the nome and size fields.
3 - Click on Execute.
```



------- PORTUGUESE ---------


# [API] Honey Store: Parts Inventory
## Inventário de Peças de Roupas
**Autor: Stephanie Lopes**

Este projeto é o meu MVP final da Sprint 1 do curso de **Desenvolvimento Full Stack Básico** da PUC RIO, 2024.

O objetivo aqui é listar os produtos de uma loja de roupas, com o intuito de registrar um inventário dos itens, entrada e saída de peças.

Utilizando 4 informações: nome do item, imagem, tamanho e quantidade.

Nessa coleção atual há 4 itens cadastrados na loja "Honey":
```
Button-Detail Shirt
Flared Skirt
Cargo Jeans
Soft Bra
```
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
