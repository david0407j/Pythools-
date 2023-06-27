class Enviador:
    def enviar(self, remetente, destinatario, assunto, corpo ):
        if '@' not in remetente:
            raise Emailinvalido(f'f email do remetente invalido: {remetente} ')
        return remetente


class Emailinvalido(Exception):
    pass
