from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from flask import request
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Produto
from logger import logger
from schemas import *
from flask_cors import CORS 


# ------------------------------------------------------------------------------------
# Swagger Title
# -------------------------------------------------------------------------------------
info = Info(title="Honey Parts Inventory", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# ------------------------------------------------------------------------------------
# Defining tags 
# -------------------------------------------------------------------------------------
home_tag = Tag(name="Documentation", description="Select documentation: Swagger, Redoc or Rapnomeoc")
produto_tag = Tag(name="Product", description="Adding, viewing and removing products from the database")

@app.get('/', tags=[home_tag])
def home():
    """Redirects to /openapi, a screen that allows the choice of documentation style.
    """
    return redirect('/openapi')

# ------------------------------------------------------------------------------------
# Defining POST route
# -------------------------------------------------------------------------------------
@app.post('/produto', tags=[produto_tag],
          responses={"200": ProdutoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_produto(form: ProdutoSchema):
    """Adds a new Product to the database"""
    
    produto = Produto(
        nome=form.nome,
        size=form.size,
        quantity=form.quantity
    )
    
    logger.debug(f"Adding product named: '{produto.nome}' and size: '{produto.size}'")
    try:
        # creating connection to the database
        session = Session()
        # adding product
        session.add(produto)
        # committing the command
        session.commit()
        logger.debug(f"Product '{produto.nome}' of size '{produto.size}' added")
        return apresenta_produto(produto), 200

    except IntegrityError as e:
        # Handling for duplicate name and size
        error_msg = "Product with the same name and size already exists in the database."
        logger.warning(f"Error adding product '{produto.nome}' of size '{produto.size}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # in case of an unexpected error
        error_msg = "Could not save the product."
        logger.warning(f"Error adding product '{produto.nome}', {error_msg}")
        return {"mesage": error_msg}, 400

# ------------------------------------------------------------------------------------
# Defining GET route - ALL ITEMS
# ------------------------------------------------------------------------------------
@app.get('/produtos', tags=[produto_tag],
         responses={"200": ListagemProdutosSchema, "404": ErrorSchema})
def get_produtos():
    """Searches for all registered Products

    Returns a representation of the product listing.
    """
    logger.debug(f"Collecting products ")
    # creating connection to the database
    session = Session()
    # performing the search
    produtos = session.query(Produto).all()

    if not produtos:
        # if there are no registered products
        return {"produtos": []}, 200
    else:
        logger.debug(f"%d Products found" % len(produtos))
        # returns the product representation
        print(produtos)
        return apresenta_produtos(produtos), 200

# ------------------------------------------------------------------------------------
# Defining GET route - ONE ITEM
# ------------------------------------------------------------------------------------

@app.get('/produto', tags=[produto_tag],
         responses={"200": ProdutoViewSchema, "404": ErrorSchema})
def get_produto(query: ProdutoBuscaSchema):
    """Searches for a Product by name and size"""
    
    produto_nome = query.nome
    produto_size = query.size
    logger.debug(f"Collecting data about product '{produto_nome}' of size '{produto_size}'")
    
    session = Session()
    produto = session.query(Produto).filter(Produto.nome == produto_nome, Produto.size == produto_size).first()

    if not produto:
        error_msg = "Product not found in the database."
        logger.warning(f"Error searching for product '{produto_nome}' of size '{produto_size}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Product found: '{produto.nome}', size: '{produto.size}'")
        return apresenta_produto(produto), 200

# ------------------------------------------------------------------------------------
# Defining DELETE route
# -------------------------------------------------------------------------------------

@app.delete('/produto', tags=[produto_tag],
            responses={"200": ProdutoDelSchema, "404": ErrorSchema, "400": ErrorSchema})
def del_produto(query: ProdutoBuscaSchema):
    """Deletes a Product based on the provided name and size"""
    
    produto_nome = unquote(query.nome)  # Decodes the product name
    produto_size = query.size  # Gets the product size
    logger.debug(f"Deleting product '{produto_nome}' of size '{produto_size}'")
    
    try:
        session = Session()
        count = session.query(Produto).filter(Produto.nome == produto_nome, Produto.size == produto_size).delete()
        session.commit()

        if count:
            logger.debug(f"Product '{produto_nome}' of size '{produto_size}' deleted")
            return {"mesage": "Product removed", "id": produto_nome}, 200
        else:
            error_msg = "Product not found in the database."
            logger.warning(f"Error deleting product '{produto_nome}' of size '{produto_size}', {error_msg}")
            return {"mesage": error_msg}, 404
    except Exception as e:
        error_msg = "Error deleting product. Please try again."
        logger.error(f"Error deleting product '{produto_nome}' of size '{produto_size}', {e}")
        return {"mesage": error_msg}, 400

# ------------------------------------------------------------------------------------
# Defining PUT route 
# -------------------------------------------------------------------------------------
@app.put('/produto', tags=[produto_tag],
         responses={"200": ProdutoViewSchema, "404": ErrorSchema, "400": ErrorSchema})
def update_produto(body: ProdutoUpdateSchema):
    """
    Edits the data of a selected product.

    This API call expects a JSON body with the following fields:
    - originalName: The current name of the product to edit
    - originalSize: The current size of the product to edit
    - nome: The new name for the product
    - size: The new size for the product
    - quantity: The new quantity for the product
    """
    data = body.dict()  # Converte o corpo em um dicionário
    try:
        # Instanciar sessão do banco de dados
        session = Session()

        # Buscando o produto original pelo nome e tamanho
        produto = session.query(Produto).filter(
            Produto.nome == data['originalName'],
            Produto.size == data['originalSize']
        ).first()

        if not produto:
            error_msg = "Product not found in the database :/"
            logger.warning(f"Error updating product '{data['originalName']}', {error_msg}")
            return {"mesage": error_msg}, 404

        # Verificando se já existe um produto com o novo nome e tamanho
        existing_produto = session.query(Produto).filter(
            Produto.nome == data['nome'],
            Produto.size == data['size']
        ).first()

        if existing_produto and existing_produto.id != produto.id:
            error_msg = "A product with this name and size already exists."
            logger.warning(f"Error updating product '{data['originalName']}', {error_msg}")
            return {"mesage": error_msg}, 400

        # Atualizando o produto com os novos valores
        produto.nome = data['nome']
        produto.size = data['size']
        produto.quantity = data['quantity']

        session.commit()
        logger.debug(f"Product updated: '{produto.nome}'")
        return apresenta_produto(produto), 200

    except IntegrityError as e:
        session.rollback()
        error_msg = "Error updating the product due to an integrity violation."
        logger.warning(f"Error updating product '{produto.nome}', {error_msg}")
        return {"mesage": error_msg}, 400

    except Exception as e:
        error_msg = "Error processing the request :/"
        logger.error(f"Error updating product: {e}")
        return {"mesage": error_msg}, 400