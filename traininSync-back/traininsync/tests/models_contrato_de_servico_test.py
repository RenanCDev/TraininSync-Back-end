from django.test import TestCase
from datetime import date, time

from ..models import Pessoa, Aluno, DadosBancarios, Personal, Servico, ContratoDeServico


class ContratoDeServicoTestCase(TestCase):
    def setUp(self):
        dados_bancarios = DadosBancarios.objects.create(numero_conta="123456", agencia="0001")
        personal = Personal.objects.create(
            nome="Personal Teste",
            cpf="98765432100",
            data_de_nascimento=date(1985, 5, 20),
            email="personal@teste.com",
            numero_de_celular="11988888888",
            sexo="M",
            etnia="branca",
            estado_civil="solteiro",
            cref="CREF54321",
            especialidades="Musculação",
            experiencia_profissional="10 anos",
            dados_bancarios=dados_bancarios,
            horarios_disponiveis=20.0,
            locais_disponiveis="Academia Central",
        )
        pessoa = Pessoa.objects.create(
            nome="Aluno Teste",
            cpf="12345678909",
            data_de_nascimento="1995-01-01",
            email="aluno@teste.com",
            numero_de_celular="11999999999",
            sexo="M",
            etnia="branca",
            estado_civil="solteiro",
        )
        aluno = Aluno.objects.create(
            pessoa=pessoa,
            bioimpedancia="BIO1234567890",
            altura=1.75,
            data_do_exame=date.today(),
            hora_do_exame="08:00",
            peso=70.0,
        )
        servico = Servico.objects.create(
            tipo_de_servico="Treino Avançado",
            descricao_do_servico="Treino focado em hipertrofia",
            valor_do_servico=200.0,
        )
        self.contrato = ContratoDeServico.objects.create(
            personal=personal,
            aluno=aluno,
            servico_desejado=servico,
            localidade_desejada="Academia Central",
        )

    def test_criar_contrato(self):
        self.assertEqual(self.contrato.localidade_desejada, "Academia Central")
        self.assertEqual(self.contrato.servico_desejado.tipo_de_servico, "Treino Avançado")
        self.assertEqual(self.contrato.personal.nome, "Personal Teste")
        self.assertEqual(self.contrato.aluno.pessoa.nome, "Aluno Teste")

    def test_desativar_contrato(self):
        self.contrato.save()
        contrato_db = ContratoDeServico.objects.get(id=self.contrato.id)

    def test_ativar_contrato(self):
        self.contrato.save()
        self.contrato.save()
        contrato_db = ContratoDeServico.objects.get(id=self.contrato.id)

    def test_consultar_contrato(self):
        contrato_consultado = ContratoDeServico.objects.filter(localidade_desejada="Academia Central").first()
        self.assertIsNotNone(contrato_consultado)
        self.assertEqual(contrato_consultado.id, self.contrato.id)

