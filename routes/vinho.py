from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from models import Session, Vinho, Categoria
from logger import logger
from schemas import *
from flask_cors import CORS

from sqlalchemy.exc import IntegrityError

from schemas.vinho import apresenta_vinho, apresenta_vinhos

from app import app

vinho_tag = Tag(name="Vinho", description="Adição, visualização e remoção de vinhos à base")

@app.post('/vinho', tags=[vinho_tag],
          responses={"200": VinhoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_vinho(form: VinhoSchema):
    """Adiciona uma nova Vinho à base de dados

    Retorna uma representação das vinhos e categorias associadas.
    """
    categoria_id = form.categoria_id
    session = Session()
    categoria = session.query(Categoria).filter(Categoria.id == categoria_id).first()

    if not categoria:
        # se categoria não encontrada
        error_msg = "Categoria não encontrada na base :/"
        logger.warning(f"Erro ao criar vinho à categoria'{categoria_id}', {error_msg}")
        return {"mesage": error_msg}, 404
    print(form)
    vinho = Vinho(
       cargo = form.cargo,
       modalidade_contrato = form.modalidade_contrato,
       modalidade_trabalho = form.modalidade_trabalho,
       categoria_id = form.categoria_id,
       descricao = form.descricao,
       responsabilidades = form.responsabilidades,
       conhecimentos = form.conhecimentos)
    
    logger.debug(f"Adicionando vinho: '{vinho.cargo}'")
    try:
        # criando conexão com a base
        session = Session()
        # adicionando produto
        session.add(vinho)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionada vinho: '{vinho.cargo}'")
        return apresenta_vinho(vinho), 200

    except IntegrityError as e:
        error_msg = f"Ocorreu um erro de integridade ao tentar adicionar a vinho '{vinho.cargo}' à categoria '{categoria_id}' :/"
        logger.warning(f"Erro ao adicionar vinho '{vinho.cargo}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar vinho '{vinho.cargo}', {error_msg}")
        return {"mesage": error_msg}, 400
    
@app.get('/vinho', tags=[vinho_tag],
        responses={"200": VinhoViewSchema, "404": ErrorSchema})
def get_vinho(query: VinhoBuscaSchema):
    """Faz a busca por uma vinho com base no id
    
    Retorna uma representação da vinho.
    """
    vinho_id = query.id
    logger.debug(f"Coletando dados sobre a categoria #{vinho_id}")

    # criando conexão com a base
    session = Session()
    # fazendo a busca
    vinho = session.query(Vinho).filter(Vinho.id == vinho_id).first()

    if not vinho:
        error_msg = "Vinho não encontrada na base."
        return {"message": error_msg}, 404
    else:
        logger.debug(f'%Vinho {vinho_id} encontrada')
        return apresenta_vinho(vinho), 200
    
@app.get('/vinhos', tags=[vinho_tag],
        responses={"200": ListagemVinhosSchema, "404": ErrorSchema})
def get_vinhos():
    """Faz a busca por todas as vinhos cadastradas
    
    Retorna uma representação da listagem de vinhos.
    """
    logger.debug(f"Coletando vinhos.")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    vinhos = session.query(Vinho).all()

    if not vinhos:
        return {"vinhos": []}, 200
    else:
        logger.debug(f'%d vinhos encontradas' % len(vinhos))
        return apresenta_vinhos(vinhos), 200
   
@app.delete('/vinho', tags=[vinho_tag],
            responses={"200": VinhoDelSchema, "404": ErrorSchema})
def del_vinho(query: VinhoBuscaSchema):
    """Deleta uma vinho a partir do id informado

    Retorna uma mensagem de confirmação da remoção.
    """
    vinho_id = query.id
    logger.debug(f"Deletando dados sobre a vinho #{vinho_id}")

    # criando conexão com a base
    session = Session()
    # fazendo a busca
    vinho = session.query(Vinho).filter(Vinho.id == vinho_id).delete()
    session.commit()

    if not vinho:
        error_msg = "Vinho não encontrada na base."
        return {"message": error_msg}, 404
    else:
        logger.debug(f'%Vinho {vinho_id} removida.')
        return {"message": f"Vinho {vinho_id} removida."}, 200

