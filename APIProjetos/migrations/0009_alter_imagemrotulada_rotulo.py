# Generated by Django 4.2.6 on 2023-10-06 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('APIProjetos', '0008_alter_imagemrotulada_imagem_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemrotulada',
            name='rotulo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagensrotuladas', to='APIProjetos.rotulo'),
        ),
    ]