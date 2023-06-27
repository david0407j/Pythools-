import pytest

from libpythonpro2.spam.enviador_de_email import Enviador, Emailinvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['cleide.22.@gmail.com', 'djunio239@gmail.com']
)
def test_remetente(remetente):
     enviador= Enviador()
     resultado = enviador.enviar(
          remetente,
         'deivisonj1@hotmail.com',
         'Curso Python Pro',
         'Primeira Turma Guido Von Rossum Aberta.'
     )
     assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'davidson']
)
def test_remetente_invalido(remetente):
     enviador = Enviador()
     with pytest.raises(Emailinvalido):
        enviador.enviar(
          remetente,
          'deivisonj1@hotmail.com',
          'Curso Python Pro',
          'Primeira Turma Guido Von Rossum Aberta.'
        )

