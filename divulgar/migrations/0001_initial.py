# Generated by Django 4.2.4 on 2023-08-30 23:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from divulgar.variaveis import para_adocao,pelagem_curta,pelagem_longa,protetor,adestrado,adotado,agitado,docil,bravo,carinhoso,manso,castrado,especial,vacinado,resgatado,hipoalergico


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Raca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raca', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especie', models.CharField(choices=[('C', 'Cachorro'), ('G', 'Gato')], max_length=1)),
                ('nome', models.CharField(max_length=120)),
                ('descricao', models.TextField()),
                ('cidade', models.CharField(max_length=120)),
                ('telefone', models.CharField(max_length=14)),
                ('status', models.CharField(choices=[(adotado, adotado), (para_adocao, para_adocao)], default=para_adocao, max_length=20)),
                ('tag1', models.CharField(blank=True, choices=[(docil, docil), (bravo, bravo), (carinhoso, carinhoso), (manso, manso), (protetor, protetor), (agitado, agitado), (vacinado, vacinado), (castrado, castrado), (pelagem_longa, pelagem_longa), (especial, especial), (resgatado, resgatado), (pelagem_curta, pelagem_curta), (adestrado, adestrado), (hipoalergico, hipoalergico)], max_length=120, null=True)),
                ('tag2', models.CharField(blank=True, choices=[(docil, docil), (bravo, bravo), (carinhoso, carinhoso), (manso, manso), (protetor, protetor), (agitado, agitado), (vacinado, vacinado), (castrado, castrado), (pelagem_longa, pelagem_longa), (especial, especial), (resgatado, resgatado), (pelagem_curta, pelagem_curta), (adestrado, adestrado), (hipoalergico, hipoalergico)], max_length=120, null=True)),
                ('tag3', models.CharField(blank=True, choices=[(docil, docil), (bravo, bravo), (carinhoso, carinhoso), (manso, manso), (protetor, protetor), (agitado, agitado), (vacinado, vacinado), (castrado, castrado), (pelagem_longa, pelagem_longa), (especial, especial), (resgatado, resgatado), (pelagem_curta, pelagem_curta), (adestrado, adestrado), (hipoalergico, hipoalergico)], max_length=120, null=True)),
                ('tag4', models.CharField(blank=True, choices=[(docil, docil), (bravo, bravo), (carinhoso, carinhoso), (manso, manso), (protetor, protetor), (agitado, agitado), (vacinado, vacinado), (castrado, castrado), (pelagem_longa, pelagem_longa), (especial, especial), (resgatado, resgatado), (pelagem_curta, pelagem_curta), (adestrado, adestrado), (hipoalergico, hipoalergico)], max_length=120, null=True)),
                ('foto', models.ImageField(upload_to='pets')),
                ('raca', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='divulgar.raca')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
