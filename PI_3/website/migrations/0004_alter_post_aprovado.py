# Generated by Django 5.1.3 on 2024-11-16 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_post_aprovado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='aprovado',
            field=models.BooleanField(default=False),
        ),
    ]