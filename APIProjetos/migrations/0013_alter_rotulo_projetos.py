# Generated by Django 4.2.6 on 2023-10-15 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIProjetos', '0012_alter_imagem_usuario_alter_imagemrotulada_usuario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rotulo',
            name='projetos',
            field=models.ManyToManyField(blank=True, related_name='rotulos', to='APIProjetos.projeto'),
        ),
    ]
