from django.test import TestCase
from ..models import Servico

class ServicoTestCase(TestCase):
    def setUp(self):
        self.servico = Servico.objects.create(
            tipo_de_servico="Treino Personalizado",
            descricao_do_servico="Plano de treino individualizado",
            valor_do_servico=150.0
        )

    def test_criar_servico(self):
        self.assertEqual(self.servico.tipo_de_servico, "Treino Personalizado")
        self.assertEqual(self.servico.valor_do_servico, 150.0)

    def test_consultar_servico(self):
        servico_consultado = Servico.objects.filter(tipo_de_servico="Treino Personalizado").first()
        self.assertIsNotNone(servico_consultado)
        self.assertEqual(servico_consultado.id, self.servico.id)
