# Generated by Django 5.1.3 on 2024-11-17 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_solicitacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitacao',
            name='cpf',
            field=models.CharField(default=11122233344, max_length=14),
            preserve_default=False,
        ),
    ]
