# Generated by Django 5.1.1 on 2024-09-03 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_portfolio_opcoes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='opcoes',
        ),
        migrations.AddField(
            model_name='portfolio',
            name='variavel1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='variavel2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='variavel3',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Resultado',
        ),
    ]
