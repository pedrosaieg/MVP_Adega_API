from pydantic import BaseModel
from typing import Optional, List
from models.vinho import Vinho


class VinhoSchema(BaseModel):
    """ Define como uma nova vinho a ser inserida deve ser representada
    """
    cargo:str = "Analista"
    modalidade_contrato:str = "PJ"
    modalidade_trabalho:str = "Presencial"
    categoria_id:int = 1
    descricao:str = "Planejar"
    responsabilidades:str = "Propor"
    conhecimentos:str = "Bom"

class VinhoViewSchema(BaseModel):
    """ Define como uma vinho será retornada.
    """
    id: int = 1
    cargo: str = "Analista"
    modalidade_contrato:str = "CLT"
    modalidade_trabalho:str = "Presencial"
    categoria_id:int = 1
    descricao:str = "Planejar"
    responsabilidades:str = "Propor estratégias e alinhar/formalizar objetivos de performance junto aos clientes; Elaborar relatórios internos e externos de marketing digital"
    conhecimentos:str = "Bom raciocínio lógico; Perfil analítico e com foco em resultados; Habilidade de comunicação e relacionamento"

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
        "cargo": vinho.cargo,
        "modalidade_contrato": vinho.modalidade_contrato,
        "modalidade_trabalho": vinho.modalidade_trabalho,
        "categoria_id": vinho.categoria_id,
        "descricao": vinho.descricao,
        "responsabilidades": vinho.responsabilidades,
        "conhecimentos": vinho.conhecimentos
    }

def apresenta_vinhos(vinhos: List[Vinho]):
    """ Retorna uma representação da vinho seguindo o schema definido em
        VinhoViewSchema.
    """
    result = []
    for vinho in vinhos:
        result.append({
        "id": vinho.id,
        "cargo": vinho.cargo,
        "modalidade_contrato": vinho.modalidade_contrato,
        "modalidade_trabalho": vinho.modalidade_trabalho,
        "categoria_id": vinho.categoria_id,
        "descricao": vinho.descricao,
        "responsabilidades": vinho.responsabilidades,
        "conhecimentos": vinho.conhecimentos
        })

    return {"vinhos": result}