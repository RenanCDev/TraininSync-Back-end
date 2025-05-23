# pylint: skip-file
# Generated by Django 5.2 on 2025-05-14 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "traininsync",
            "0003_rename_aguacorporaltotal_aluno_agua_corporal_total_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="aluno",
            old_name="data_do_Exame",
            new_name="data_do_exame",
        ),
        migrations.RenameField(
            model_name="aluno",
            old_name="massa_gordura",
            new_name="gordura_corporal",
        ),
        migrations.RenameField(
            model_name="aluno",
            old_name="hora_do_Exame",
            new_name="hora_do_exame",
        ),
        migrations.RenameField(
            model_name="registrodeprogresso",
            old_name="reated_at",
            new_name="created_at",
        ),
        migrations.RenameField(
            model_name="servico",
            old_name="valr_do_servico",
            new_name="valor_do_servico",
        ),
        migrations.RemoveField(
            model_name="aluno",
            name="idade",
        ),
        migrations.RemoveField(
            model_name="aluno",
            name="sexo",
        ),
        migrations.AlterField(
            model_name="pessoa",
            name="estado_civil",
            field=models.CharField(
                choices=[
                    ("solteiro", "Solteiro(a)"),
                    ("casado", "Casado(a)"),
                    ("divorciado", "Divorciado(a)"),
                    ("viuvo", "Viúvo(a)"),
                    ("uniao_estavel", "União Estável"),
                    ("nao_informado", "Prefiro não dizer"),
                ],
                max_length=20,
            ),
        ),
    ]
