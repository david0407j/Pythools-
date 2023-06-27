from libpythonpro2.spam.modelos import Usuarios


def test_salvar_usuario(sessao):
    usuario = Usuarios(nome='Davidson', email='djunio239@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id , int)


def test_listar_usuario(sessao):
    usuarios = [
        Usuarios(nome='Davidson', email='djunio239@gmail.com'),
        Usuarios(nome= 'junior', email= 'junio239@gmail.com')
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
