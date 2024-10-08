# Generated by Django 5.1.1 on 2024-09-19 06:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('nome', models.CharField(max_length=255)),
                ('whatsapp', models.CharField(max_length=15)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('data_ultimo_acesso', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Senha',
            fields=[
                ('senha_id', models.AutoField(primary_key=True, serialize=False)),
                ('senha_hash', models.CharField(max_length=255)),
                ('salt', models.CharField(max_length=255)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ia2eccApp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('animal_id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('especie', models.CharField(choices=[('cao', 'Cão'), ('gato', 'Gato')], max_length=4)),
                ('raca', models.CharField(max_length=255)),
                ('data_nascimento', models.DateField()),
                ('peso', models.DecimalField(decimal_places=2, max_digits=5)),
                ('condicao_corporal', models.IntegerField()),
                ('gestacao', models.BooleanField(default=False)),
                ('semana_gestacao', models.IntegerField(blank=True, null=True)),
                ('lactacao', models.IntegerField(blank=True, null=True)),
                ('semana_lactacao', models.IntegerField(blank=True, null=True)),
                ('foto', models.CharField(blank=True, max_length=255, null=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ia2eccApp.user')),
            ],
        ),
    ]
