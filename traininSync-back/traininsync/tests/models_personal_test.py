from django.test import TestCase
from datetime import date
from ..models import Pessoa, Personal, DadosBancarios

class PersonalModelTestCase(TestCase):
    def setUp(self):
        self.dados_bancarios = DadosBancarios.objects.create(
            numero_conta="12345-6",
            agencia="0001"
        )
        self.pessoa_data = {
            "nome": "Carlos Souza",
            "cpf": "12345678900",
            "data_de_nascimento": date(1988, 10, 20),
            "email": "carlos@example.com",
            "numero_de_celular": "11977776666",
            "sexo": "M",
            "etnia": "branco",
            "estado_civil": "casado"
        }
        self.personal = Personal.objects.create(
            dados_bancarios=self.dados_bancarios,
            status=True,
            cref="012345-G/SP",
            especialidades="Musculação, Funcional",
            experiencia_profissional="5 anos",
            horarios_disponiveis=20.5,
            locais_disponiveis="Academia A, Parque B",
            **self.pessoa_data
        )

    def test_criar_personal(self):
        self.assertEqual(self.personal.nome, "Carlos Souza")
        self.assertTrue(self.personal.status)
        self.assertEqual(self.personal.cref, "012345-G/SP")
        self.assertEqual(self.personal.especialidades, "Musculação, Funcional")

    def test_ativar_personal(self):
        self.personal.reativar_personal()
        personal_db = Personal.objects.get(id=self.personal.id)
        self.assertTrue(personal_db.status)

    def test_desativar_personal(self):
        self.personal.desativar_personal()
        personal_db = Personal.objects.get(id=self.personal.id)
        self.assertFalse(personal_db.status)

    @classmethod
    def consultar_por_cpf(cls, cpf):
        return Personal.consultar_por_cpf(cpf)

    def test_consultar_por_cpf(self):
        personal = PersonalModelTestCase.consultar_por_cpf("12345678900")
        self.assertIsNotNone(personal)
        self.assertEqual(personal.id, self.personal.id)