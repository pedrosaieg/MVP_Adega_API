from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  models import Base

class Categoria(Base):
    __tablename__ = 'categoria'

    id = Column("pk_categoria", Integer, primary_key=True)
    nome = Column(String(100), unique=True)
    ramo_atuacao = Column(String(100))
    sobre = Column(String(100))
    link = Column(String(120), unique = True)
    tamanho = Column(Integer)
    data_insercao = Column(DateTime, default=datetime.now())
    vinhos = relationship("Vinho", backref = "categoria")

    def __init__(self, nome:str, ramo_atuacao:str, sobre:str, link:str, tamanho:int,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria uma Categoria

        Argumentos:
            nome: nome da categoria 
            ramo_atuacao: linha de atuação de mercado da categoria
            sobre: informações gerais da categoria
            link: página web da categoria
            tamanho: número médio de funcionários
            data_insercao: data de quando o produto foi inserido à base
        """
        self.nome = nome
        self.ramo_atuacao = ramo_atuacao
        self.sobre = sobre
        self.link = link
        self.tamanho = tamanho

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao

 #   def adiciona_comentario(self, comentario:Comentario):
  #      """ Adiciona um novo comentário ao Produto
   #     """
    #    self.comentarios.append(comentario)

