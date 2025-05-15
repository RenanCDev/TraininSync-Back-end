from django.test import TestCase
from ..models import DadosBancarios

class DadosBancariosTestCase(TestCase):
    def setUp(self):
        self.dados_bancarios = DadosBancarios.objects.create(
            numero_conta="123456",
            agencia="0001",
        )

    def test_criar_dados_bancarios(self):
        self.assertEqual(self.dados_bancarios.numero_conta, "123456")
        self.assertEqual(self.dados_bancarios.agencia, "0001")

    def test_desativar_dados_bancarios(self):
        self.dados_bancarios.ativo = False
        self.dados_bancarios.save()
        dados_db = DadosBancarios.objects.get(id=self.dados_bancarios.id)

    def test_ativar_dados_bancarios(self):
        self.dados_bancarios.ativo = False
        self.dados_bancarios.save()
        self.dados_bancarios.ativo = True
        self.dados_bancarios.save()
        dados_db = DadosBancarios.objects.get(id=self.dados_bancarios.id)

    def test_consultar_dados_bancarios(self):
        dados_consultado = DadosBancarios.objects.filter(numero_conta="123456").first()
        self.assertIsNotNone(dados_consultado)
        self.assertEqual(dados_consultado.id, self.dados_bancarios.id)
