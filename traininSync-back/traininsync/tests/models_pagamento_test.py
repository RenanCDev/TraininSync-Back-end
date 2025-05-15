from django.test import TestCase
from datetime import date

from ..models import Pessoa, Aluno, Personal, DadosBancarios, Servico, ContratoDeServico, Pagamento

class PagamentoTestCase(TestCase):
    def setUp(self):
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
        self.aluno = Aluno.objects.create(
            pessoa=pessoa,
            bioimpedancia="BIO1234567890",
            altura=1.75,
            data_do_exame=date.today(),
            hora_do_exame="08:00",
            peso=70.0,
        )
        dados_bancarios = DadosBancarios.objects.create(numero_conta="123456", agencia="0001")
        personal = Personal.objects.create(
            nome="Personal Teste",
            cpf="98765432100",
            data_de_nascimento="1980-01-01",
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
        servico = Servico.objects.create(
            tipo_de_servico="Treino Avançado",
            descricao_do_servico="Treino focado em hipertrofia",
            valor_do_servico=200.0
        )
        self.contrato = ContratoDeServico.objects.create(
            personal=personal,
            aluno=self.aluno,
            servico_desejado=servico,
            localidade_desejada="Academia Central"
        )
        self.pagamento = Pagamento.objects.create(
            aluno=self.aluno,
            contrato=self.contrato,
            valor=200.00,
            descricao="Pagamento mensal do serviço"
        )

    def test_criar_pagamento(self):
        self.assertEqual(self.pagamento.aluno, self.aluno)
        self.assertEqual(self.pagamento.contrato, self.contrato)
        self.assertEqual(self.pagamento.valor, 200.00)
        self.assertIn("Pagamento mensal", self.pagamento.descricao)

    def test_consultar_pagamento(self):
        pagamento_consultado = Pagamento.objects.filter(descricao__icontains="mensal").first()
        self.assertIsNotNone(pagamento_consultado)
        self.assertEqual(pagamento_consultado.id, self.pagamento.id)

    def test_ativar_pagamento(self):
        self.pagamento.descricao = "Pagamento Ativo"
        self.pagamento.save()
        pagamento_db = Pagamento.objects.get(id=self.pagamento.id)
        self.assertEqual(pagamento_db.descricao, "Pagamento Ativo")

    def test_desativar_pagamento(self):
        self.pagamento.descricao = "Pagamento Desativado"
        self.pagamento.save()
        pagamento_db = Pagamento.objects.get(id=self.pagamento.id)
        self.assertEqual(pagamento_db.descricao, "Pagamento Desativado")
