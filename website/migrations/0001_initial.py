# Generated by Django 2.2.3 on 2019-07-25 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('sobrenome', models.CharField(max_length=255, verbose_name='Sobrenome')),
                ('genero', models.CharField(choices=[('M', 'masculino'), ('F', 'feminino'), ('O', 'outros')], max_length=255, verbose_name='Gênero')),
                ('email', models.EmailField(max_length=255, verbose_name='Email')),
                ('data_de_criacao', models.DateTimeField(auto_now_add=True)),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
    ]
