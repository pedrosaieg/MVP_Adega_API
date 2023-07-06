from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, request
from urllib.parse import unquote

from models import Session, Categoria
from logger import logger
from schemas import *
from flask_cors import CORS

from sqlalchemy.exc import IntegrityError

from schemas.categoria import apresenta_categoria, apresenta_categorias

from app import app

categoria_tag = Tag(name="Categoria", description="Adição, visualização e remoção de categorias à base")

@app.post('/categoria', tags=[categoria_tag],
           responses={"200": CategoriaViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_categoria(form: CategoriaSchema):
    """Adiciona uma nova categoria à base de dados

    Retorna uma representação das categorias.
    """
    categoria = Categoria(
        nome = form.nome,
        ramo_atuacao= form.ramo_atuacao,
        sobre= form.sobre,
        link= form.link,
        tamanho= form.tamanho
    )

    logger.debug(f"Adicionando categoria: '{categoria.nome}'")
    try:
        # criando conexão com a base
        session = Session()
        # adicionando produto
        session.add(categoria)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionada categoria: '{categoria.nome}'")
        return apresenta_categoria(categoria), 200

    except IntegrityError as e:
        error_msg = f"Ocorreu um erro de integridade ao tentar adicionar a categoria '{categoria.nome}'"
        logger.warning(f"Erro ao adicionar categoria '{categoria.nome}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar categoria '{categoria.nome}', {error_msg}")
        return {"mesage": error_msg}, 400

@app.get('/categorias', tags=[categoria_tag],
         responses={"200": ListagemCategoriasSchema, "404": ErrorSchema})
def get_categorias():
    """Faz a busca por todas as categorias cadastradas
    
    Retorna uma representação da listagem de categorias.
    """
    logger.debug(f"Coletando categorias ")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    categorias = session.query(Categoria).all()

    if not categorias:
        return {"categorias": []}, 200
    else:
        logger.debug(f'%d categorias encontradas' % len(categorias))
        return apresenta_categorias(categorias), 200
    
@app.get('/categoria', tags=[categoria_tag],
         responses={"200": CategoriaViewSchema, "404": ErrorSchema})
def get_categoria(query: CategoriaBuscaSchema):
    """Faz a busca por uma categoria a partir do id da categoria
    
    Retorna uma representação categoria.
    """
    categoria_id = query.id
    logger.debug(f"Coletando dados sobre a categoria #{categoria_id}")

    # criando conexão com a base
    session = Session()
    # fazendo a busca
    categoria = session.query(Categoria).filter(Categoria.id == categoria_id).first()

    if not categoria:
        error_msg = "Categoria não encontrada na base."
        return {"message": error_msg}, 404
    else:
        logger.debug(f'%Categoria {categoria_id} encontrada')
        return apresenta_categoria(categoria), 200
    

@app.delete('/categoria', tags=[categoria_tag],
         responses={"200": CategoriaDelSchema, "404": ErrorSchema})
def delete_categoria(query: CategoriaBuscaSchema):
    """Deleta uma categoria a partir do id informado
    
    Retorna uma mensagem de confirmação da remoção.
    """
    categoria_id = query.id
    logger.debug(f"Deletando dados sobre a categoria #{categoria_id}")

    # criando conexão com a base
    session = Session()
    # fazendo a busca
    categoria = session.query(Categoria).filter(Categoria.id == categoria_id).delete()
    session.commit()

    if not categoria:
        error_msg = "Categoria não encontrada na base."
        return {"message": error_msg}, 404
    else:
        logger.debug(f'%Categoria {categoria_id} removida.')
        return {"message": f"Categoria {categoria_id} removida."}, 200
    

@app.put('/categoria/', tags=[categoria_tag],
         responses={"200": CategoriaViewSchema, "404": ErrorSchema})
def edit_categoria(form: CategoriaEditSchema):
    """Edita uma categoria a partir do id informado
    
    Retorna uma mensagem de confirmação da edição.
    """
    categoria_id = form.id
    print(form)

    logger.debug(f"Editando dados sobre a categoria #{categoria_id}")

    # criando conexão com a base
    session = Session()
    # fazendo a busca
    categoria = session.query(Categoria).filter(Categoria.id == categoria_id).update({"nome":form.nome, "ramo_atuacao": form.ramo_atuacao, "sobre": form.sobre, "link": form.link, "tamanho": form.tamanho})

    session.commit()

    if not categoria:
        error_msg = "Categoria não encontrada na base."
        return {"message": error_msg}, 404
    else:
        categoria_editada = session.query(Categoria).filter(Categoria.id == categoria_id).first()
        logger.debug(f'%Categoria {categoria_id} editada.')
        return apresenta_categoria(categoria_editada), 200