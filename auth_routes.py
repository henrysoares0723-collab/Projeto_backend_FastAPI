from fastapi import APIRouter

auth_router = APIRouter(prefix='/auth', tags=['auth'])
@auth_router.get('/')
async def autenticar():
    """
    Essa é a rota padrão de autenticaçâo do sistema
    """
    return {'Mensagem': 'Você acessou a rota de autenticaçâo', 'Autenticado': False}
