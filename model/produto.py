from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy import Column, String, Integer, UniqueConstraint
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from model import Base

class Produto(Base):
    __tablename__ = 'produto'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    size = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)

    __table_args__ = (UniqueConstraint('nome', 'size', name='_nome_size_uc'),)


    def __init__(self, nome: str, size: str, quantity: int,
                 data_insercao: Union[DateTime, None] = None):
        """
        Creates a Product

        Arguments:
            name: name of the product.
            quantidade: quantity expected to purchase for that product
            valor: expected price for the product
            data_insercao: date when the product was added to the database
        """
        self.nome = nome
        self.size = size
        self.quantity = quantity

        # if not provided, it will be the exact date of insertion into the database
        if data_insercao:
            self.data_insercao = data_insercao
