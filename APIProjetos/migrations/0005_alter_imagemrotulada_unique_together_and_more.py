# Generated by Django 4.2.6 on 2023-10-06 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APIProjetos', '0004_alter_rotulo_projetos'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='imagemrotulada',
            unique_together={('rotulo', 'imagem')},
        ),
        migrations.RemoveField(
            model_name='imagemrotulada',
            name='projeto',
        ),
    ]
