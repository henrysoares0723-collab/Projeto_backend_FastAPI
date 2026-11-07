from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declaretive_base
from sqlalchemy_utils.types import ChoiceType

db = create_engine("sqllite:///banco.db")
base = declaretive_base()

class Usuario(base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String) 
    email = Column("email", String, nullable=False)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)
    admin = Column("admin", Boolean, default=False)

    def __init__(self, nome, email, senha, ativo=True, admin=False):
        self.nome = nome 
        self.emal = email
        self.senha = senha 
        self.ativo = ativo
        self.admin = admin 

#Pedidos
class pedido(base):
    _tablename_ = "Pedidos"

    STATUS_PEDIDOS = (
         ("PENDENTE", "PENDENTE"),
         ("CANCELADO", "CANCELADO")
         ("FINALIZADO", "FINALIZADO")

    )

    id = Column("id", Integer, primary_key=True, autoincrement=True) 
    status = Column("status", ChoiceType(choice=STATUS_PEDIDOS)) 
    usuario = Column("usario", ForeignKey("usuario.id")) 
    preco =  Column('preco', Float)
    #itens  

    def _init_(self,usuario,status="PENDENTE", preco=0):
        self.usuario = usuario
        self.preco = preco
        self.status = status


  #ItensPedido
class ItensPedido(base):
    __tablename__ = "itenspedido"

    id = Column("id", Integer, primary_key=True, autoincrement=True) 
    quantidade = Column("quantidade", Integer)
    sabor = Column("sabor", String) 
    tamanho = Column("tamanho", String)
    preco_unitario = Column("Preco_unitario", Float)
    pedido = Column("pedido", ForeignKey("pedido.id'"))

    def __init__(self,quantidade,sabor,tamanho,preco_unitario,pedido):
        self.quantidade = quantidade
        self.sabor = sabor 
        self.tamanho = tamanho
        self.preco_unitario = preco_unitario
        self.pedido = pedido 

      
        