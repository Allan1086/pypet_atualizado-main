# Generated by Django 4.2.4 on 2023-08-31 18:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('divulgar', '0002_alter_pet_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido_Adocao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_solicitacao', models.DateTimeField()),
                ('status_pedido', models.CharField(choices=[('AG', 'Aguardando Aprovacão'), ('AP', 'Aprovado'), ('RE', 'Rejeitado')], default='AG', max_length=2)),
                ('adotante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='divulgar.pet')),
            ],
        ),
    ]