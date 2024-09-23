from pydantic import BaseModel
from typing import Optional, List
from model.produto import Produto

from flask_openapi3 import APIView, Schema, request


class ProdutoSchema(BaseModel):
    """ Defines how a new product to be inserted should be represented
    """
    nome: str = "Button-Detail Shirt"
    size: str = "P"
    quantity: int = 5


class ProdutoBuscaSchema(BaseModel):
    """ Defines the structure for the search. It will be
        based on the name and size.
    """
    nome: str 
    size: str


class ListagemProdutosSchema(BaseModel):
    """ Defines how a listing of products will be returned.
    """
    produtos: List[ProdutoSchema]


def apresenta_produtos(produtos: List[Produto]):
    """ Returns a representation of the product following the schema defined in
        ProdutoViewSchema.
    """
    result = []
    for produto in produtos:
        result.append({
            "nome": produto.nome,
            "size": produto.size,
            "quantity": produto.quantity,
        })

    return {"produtos": result}


class ProdutoViewSchema(BaseModel):
    """ Defines how a product will be returned.
    """
    id: int = 1
    nome: str = "Button-Detail Shirt"
    size: str = "P"
    quantity: int = 5


class ProdutoDelSchema(BaseModel):
    """ Defines the structure of the data returned after a
        removal request.
    """
    mesage: str
    nome: str

def apresenta_produto(produto: Produto):
    """ Returns a representation of the product following the schema defined in
        ProdutoViewSchema.
    """
    return {
        "id": produto.id,
        "nome": produto.nome,
        "size": produto.size,
        "quantity": produto.quantity,
    }


class ProdutoUpdateSchema(Schema):
    originalName: str
    originalSize: str
    nome: str
    size: str
    quantity: int
