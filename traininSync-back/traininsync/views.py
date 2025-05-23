from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render

from .models import Personal, Aluno, Servico, Agenda, ContratoDeServico, RegistroDeProgresso, Pagamento
from .serializers import PersonalSerializer, AlunoSerializer, ServicoSerializer, AgendaSerializer, ContratoDeServicoSerializer, RegistroDeProgressoSerializer, PagamentoSerializer


def api_home(request):
    return render(request, 'api_home.html')

class PersonalViewSet(ModelViewSet):
    queryset = Personal.objects.all()
    serializer_class = PersonalSerializer

class AlunoViewSet(ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class ServicoViewSet(ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer

class AgendaViewSet(ModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer

class ContratoDeServicoViewSet(ModelViewSet):
    queryset = ContratoDeServico.objects.all()
    serializer_class = ContratoDeServicoSerializer

class RegistroDeProgressoViewSet(ModelViewSet):
    queryset = RegistroDeProgresso.objects.all()
    serializer_class = RegistroDeProgressoSerializer

class PagamentoViewSet(ModelViewSet):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer