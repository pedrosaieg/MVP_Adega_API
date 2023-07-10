from pydantic import BaseModel
from typing import Optional, List
from models.categoria import Categoria

from schemas import VinhoSchema


class CategoriaSchema(BaseModel):
    """ Define como uma nova categoria a ser inserida deve ser representada
    """

    nome:str = "Bordeaux"
    pais:str = "França"
    descricao:str = "Terroir de clima temperado"


class CategoriaViewSchema(BaseModel):
    """ Define como uma categoria será retornada.
    """
    id: int = 1
    nome:str = "Sul da França"
    pais:str = "França"
    descricao:str = "Terroir de clima temperado"
    vinhos:List[VinhoSchema]

class CategoriaBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
    feita apenas com base no id da categoria.
    """
    id: int = 1

class CategoriaDelSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
    feita apenas com base no id da categoria.
    """
    message: str = "Removida com sucesso."
    id: int = 1

class CategoriaEditSchema(BaseModel):
    """ Define como uma categoria será editada.
    """
    id:int = 1
    nome:str = "Sul da França"
    pais:str = "França"
    descricao:str = "Terroir de clima temperado"

class ListagemCategoriasSchema(BaseModel):
    """ Define como a lista de categorias será retornada.
    """
    categorias:list[CategoriaSchema]

def apresenta_categoria(categoria: Categoria):
    """ Retorna uma representação da categoria seguindo o schema definido em
        CategoriaViewSchema.
    """
    return {
        "id": categoria.id,
        "nome": categoria.nome,
        "pais": categoria.pais,
        "descricao": categoria.descricao,
        "vinhos": [{"id": c.id, 
                   "nome": c.nome, 
                   "uva": c.uva, 
                   "descricao": c.descricao} for c in categoria.vinhos]
    }

def apresenta_categorias(categorias: List[Categoria]):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    result = []
    for categoria in categorias:
        result.append({
            "id": categoria.id,
            "nome": categoria.nome,
            "pais": categoria.pais,
            "descricao": categoria.descricao,
            "vinhos" : len(categoria.vinhos)
        })

    return {"categorias": result}