from django.test import TestCase
from datetime import date, time

from ..models import Personal, DadosBancarios, Agenda


class AgendaTestCase(TestCase):
    def setUp(self):
        dados_bancarios = DadosBancarios.objects.create(numero_conta="123456", agencia="0001")
        self.personal = Personal.objects.create(
            nome="Teste Personal",
            cpf="12345678909",
            data_de_nascimento="1980-01-01",
            email="personal@teste.com",
            numero_de_celular="11999999999",
            sexo="M",
            etnia="branca",
            estado_civil="solteiro",
            cref="CREF12345",
            especialidades="Musculação",
            experiencia_profissional="5 anos",
            dados_bancarios=dados_bancarios,
            horarios_disponiveis=20.0,
            locais_disponiveis="Academia Central",
        )

    def test_criar_agenda(self):
        agenda = Agenda.objects.create(
            personal=self.personal,
            dia=date(2025, 5, 20),
            hora_inicio=time(9, 0),
            hora_fim=time(10, 0),
            local="Academia Central",
            disponivel=True,
        )
        self.assertEqual(agenda.personal, self.personal)
        self.assertEqual(agenda.dia, date(2025, 5, 20))
        self.assertEqual(agenda.hora_inicio.hour, 9)
        self.assertEqual(agenda.hora_fim.hour, 10)
        self.assertTrue(agenda.disponivel)

    def test_hora_inicio_menor_hora_fim(self):
        agenda = Agenda(
            personal=self.personal,
            dia=date(2025, 5, 21),
            hora_inicio=time(11, 0),
            hora_fim=time(10, 0),
            local="Academia Central",
        )
        with self.assertRaises(Exception):
            agenda.clean()
