# Generated by Django 4.2.6 on 2023-10-10 17:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('APIProjetos', '0011_imagem_usuario_imagemrotulada_usuario_rotulo_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagem',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='imagenscriadas', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='imagemrotulada',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='imagensrotuladas', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='rotulo',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='rotulos', to=settings.AUTH_USER_MODEL),
        ),
    ]
