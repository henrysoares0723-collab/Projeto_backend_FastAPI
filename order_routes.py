from fastapi import APIRouter 

order_router = APIRouter(prefix='/pedidos', tags=['Pedidos'])
@order_router.get('/')
async def pedidos():
    """
    Essa é a rota padrão de pedidos do sistema. Todas as rotas de pedidos precisam de autenticação
    """
    return{'Mensagem: Você acessou a rota de pedidos'}