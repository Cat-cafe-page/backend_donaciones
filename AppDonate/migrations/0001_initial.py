# Generated by Django 3.2.9 on 2022-02-03 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id_donation', models.BigAutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('cardNumber', models.IntegerField(max_length=20, verbose_name='Numero de tarjeta')),
                ('nameOnCard', models.CharField(max_length=50, verbose_name='Nombre en la tarjeta')),
                ('amount', models.IntegerField(default=0)),
                ('city', models.CharField(max_length=30, verbose_name='Ciudad')),
            ],
        ),
    ]
