from pydantic import BaseModel
from typing import Optional, List
from models.vinho import Vinho


class VinhoSchema(BaseModel):
    """ Define como uma nova vinho a ser inserida deve ser representada
    """
    nome:str = "Barca Velha"
    uva:str = "Touriga Nacional"
    descricao:str = "Vinho encorpado"
    categoria_id:int = 1

class VinhoViewSchema(BaseModel):
    """ Define como uma vinho será retornada.
    """
    id: int = 1
    nome: str = "Barca Velha"
    uva:str = "Touriga Nacional"
    descricao:str = "Vinho encorpado"
    categoria_id:int = 1

class VinhoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
    feita apenas com base no id da vinho.
    """
    id: int = 1

class ListagemVinhosSchema(BaseModel):
    """ Define como a lista de vinhos será retornada.
    """
    vinhos:list[VinhoSchema]

class VinhoDelSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
    feita apenas com base no id da vinho.
    """
    message: str = "Vinho removida com sucesso."
    id: int = 1

def apresenta_vinho(vinho: Vinho):
    """ Retorna uma representação da seguindo o schema definido em
        VinhoViewSchema.
    """
    return {
        "id": vinho.id,
        "nome": vinho.nome,
        "uva": vinho.uva,
        "descricao": vinho.descricao,
        "categoria_id": vinho.categoria_id
    }

def apresenta_vinhos(vinhos: List[Vinho]):
    """ Retorna uma representação da vinho seguindo o schema definido em
        VinhoViewSchema.
    """
    result = []
    for vinho in vinhos:
        result.append({
        "id": vinho.id,
        "nome": vinho.nome,
        "uva": vinho.uva,
        "descricao": vinho.descricao,
        "categoria_id": vinho.categoria_id
        })

    return {"vinhos": result}