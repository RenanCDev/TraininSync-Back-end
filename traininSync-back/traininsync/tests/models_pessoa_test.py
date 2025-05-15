from django.test import TestCase
from datetime import date
from ..models import Pessoa

class PessoaTestCase(TestCase):
    def setUp(self):
        self.pessoa = Pessoa.objects.create(
            nome="João Silva",
            cpf="12345678909",
            data_de_nascimento=date(1990, 1, 1),
            email="joao@example.com",
            numero_de_celular="11999999999",
            sexo="M",
            etnia="branca",
            estado_civil="solteiro"
        )

    def test_criar_pessoa(self):
        self.assertEqual(self.pessoa.nome, "João Silva")
        self.assertEqual(self.pessoa.cpf, "12345678909")
        self.assertEqual(self.pessoa.email, "joao@example.com")

    def test_ativar_pessoa(self):
        self.pessoa.email = "joao_ativado@example.com"
        self.pessoa.save()
        pessoa_db = Pessoa.objects.get(id=self.pessoa.id)
        self.assertEqual(pessoa_db.email, "joao_ativado@example.com")

    def test_desativar_pessoa(self):
        self.pessoa.email = "joao_desativado@example.com"
        self.pessoa.save()
        pessoa_db = Pessoa.objects.get(id=self.pessoa.id)
        self.assertEqual(pessoa_db.email, "joao_desativado@example.com")

    @classmethod
    def consultar_por_cpf(cls, cpf):
        return Pessoa.objects.filter(cpf=cpf).first()

    def test_consultar_por_cpf(self):
        pessoa = PessoaTestCase.consultar_por_cpf("12345678909")
        self.assertIsNotNone(pessoa)
        self.assertEqual(pessoa.id, self.pessoa.id)