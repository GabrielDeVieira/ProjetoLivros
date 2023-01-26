# Generated by Django 4.1.4 on 2023-01-24 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livros',
            fields=[
                ('liv_codigo', models.AutoField(primary_key=True, serialize=False)),
                ('liv_numerodepaginas', models.IntegerField(default=None)),
                ('liv_nome', models.CharField(max_length=100)),
                ('liv_dataleitura', models.DateField(blank=True, null=True)),
                ('liv_autor', models.CharField(max_length=120)),
                ('liv_avaliacao', models.TextField(blank=True, null=True)),
                ('liv_leitura', models.BooleanField()),
            ],
        ),
    ]