from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from models import Base, Categoria

class Vinho(Base):
    __tablename__ = 'vinho'

    id = Column("pk_vinho", Integer, primary_key=True)
    nome = Column(String(140))
    uva = Column(String(30))
    descricao = Column(String(1000))

    data_insercao = Column(DateTime, default=datetime.now())

    categoria_id = Column(Integer, ForeignKey("categoria.pk_categoria"), nullable=False)

    def __init__(self, nome:str, uva:str, descricao:str, categoria_id:int,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um Vinho

        Argumentos:
            nome: nome do vinho
            uva: nome das uvas presentes no vinho
            descricao: descricao das qualidades do vinho
            data_insercao: data de quando o vinho foi inserido à base
        """
        self.nome = nome
        self.uva = uva
        self.descricao = descricao
        self.categoria_id = categoria_id

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao

