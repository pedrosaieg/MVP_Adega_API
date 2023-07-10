from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  models import Base

class Categoria(Base):
    __tablename__ = 'categoria'

    id = Column("pk_categoria", Integer, primary_key=True)
    nome = Column(String(100), unique=True)
    pais = Column(String(100))
    descricao = Column(String(100))
    data_insercao = Column(DateTime, default=datetime.now())
    vinhos = relationship("Vinho", backref = "categoria")

    def __init__(self, nome:str, pais:str, descricao:str,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria uma Categoria

        Argumentos:
            nome: nome da categoria 
            pais: país da categoria
            descricao: informações gerais da categoria
            data_insercao: data de quando a categoria foi inserida à base
        """
        self.nome = nome
        self.pais = pais
        self.descricao = descricao

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao

