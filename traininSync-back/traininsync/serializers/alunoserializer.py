from rest_framework import serializers

from .pessoaserializers import PessoaSerializer
from .serializers_base import StringNormalizerSerializer

from ..models import Pessoa, Aluno

class AlunoSerializer(StringNormalizerSerializer):
    pessoa = PessoaSerializer()

    class Meta:
        model = Aluno
        fields = '__all__'

    def create(self, validated_data):
        pessoa_data = validated_data.pop('pessoa')
        pessoa = Pessoa.objects.create(**pessoa_data)
        aluno = Aluno.objects.create(pessoa=pessoa, **validated_data)
        return aluno

    def update(self, instance, validated_data):
        pessoa_data = validated_data.pop('pessoa', None)

        if pessoa_data:
            for attr, value in pessoa_data.items():
                setattr(instance.pessoa, attr, value)
            instance.pessoa.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance