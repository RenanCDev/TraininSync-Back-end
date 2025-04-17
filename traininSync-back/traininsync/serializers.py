from rest_framework import serializers

from .models import Personal, DadosBancarios, Pessoa, Aluno


class DadosBancariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = DadosBancarios
        fields = '__all__'

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = '__all__'

class PersonalSerializer(serializers.ModelSerializer):
    dados_bancarios = DadosBancariosSerializer()

    class Meta:
        model = Personal
        fields = '__all__'

    def create(self, validated_data):
        dados_bancarios_data = validated_data.pop('dados_bancarios')
        dados_bancarios = DadosBancarios.objects.create(**dados_bancarios_data)
        personal = Personal.objects.create(dados_bancarios=dados_bancarios, **validated_data)
        return personal

    def update(self, instance, validated_data):
        dados_bancarios_data = validated_data.pop('dados_bancarios', None)

        if dados_bancarios_data:
            for attr, value in dados_bancarios_data.items():
                setattr(instance.dados_bancarios, attr, value)
            instance.dados_bancarios.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
    
class AlunoSerializer(serializers.ModelSerializer):
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