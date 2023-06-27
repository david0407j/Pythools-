import pytest

from libpythonpro2.spam.enviador_de_email import Enviador
from libpythonpro2.spam.main import EnviadorDeSpam
from libpythonpro2.spam.modelos import Usuarios
from unittest.mock import Mock
@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuarios(nome='Davidson', email='djunio239@gmail.com'),
            Usuarios(nome='junior', email='djunio239@gmail.com')],
        [
            Usuarios(nome='Davidson', email='djunio239@gmail.com')]]

)
def test_envio_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'djunio239@gmail.com',
        'Curso Python Pro',
        'confira os módolos fantátisco',
    )
    assert len(usuarios) == enviador.enviar.call_count




def test_paramentros_de_spam(sessao):
    usuarios = Usuarios (nome='Davidson', email='djunio239@gmail.com')
    sessao.salvar(usuarios)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'junio239@gmail.com',
        'Curso Python Pro',
        'confira os módolos fantátisco'
    )
    enviador.enviar.assert_called_once_with(
        'junio239@gmail.com',
        'djunio239@gmail.com',
        'Curso Python Pro',
        'confira os módolos fantátisco'
    )