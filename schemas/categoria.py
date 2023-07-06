from pydantic import BaseModel
from typing import Optional, List
from models.categoria import Categoria

from schemas import VinhoSchema


class CategoriaSchema(BaseModel):
    """ Define como uma nova categoria a ser inserida deve ser representada
    """

    nome:str = "XPTO"
    ramo_atuacao:str = "Óleo e gás"
    sobre:str = "Categoria que atua no ramo de upstream"
    link:str = "www.xpto.com.br"
    tamanho:int = 200


class CategoriaViewSchema(BaseModel):
    """ Define como uma categoria será retornada.
    """
    id: int = 1
    nome:str = "XPTO"
    ramo_atuacao:str = "Óleo e gás"
    sobre:str = "Categoria que atua no ramo de upstream"
    link:str = "www.xpto.com.br"
    tamanho:int = 200
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
    nome:str = "XPTO"
    ramo_atuacao:str = "Óleo e gás"
    sobre:str = "Categoria que atua no ramo de upstream"
    link:str = "www.xpto.com.br"
    tamanho:int = 200

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
        "ramo_atuacao": categoria.ramo_atuacao,
        "sobre": categoria.sobre,
        "link": categoria.link,
        "tamanho": categoria.tamanho,
        "vinhos": [{"id": c.id, 
                   "cargo": c.cargo, 
                   "conhecimentos": c.conhecimentos, 
                   "descricao": c.descricao, 
                   "responsabilidades": c.responsabilidades, 
                   "modalidade_contrato" : c.modalidade_contrato, 
                   "modalidade_trabalho" : c.modalidade_trabalho} for c in categoria.vinhos]
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
            "ramo_atuacao": categoria.ramo_atuacao,
            "sobre": categoria.sobre,
            "link": categoria.link,
            "tamanho": categoria.tamanho,
            "vinhos" : len(categoria.vinhos)
        })

    return {"categorias": result}