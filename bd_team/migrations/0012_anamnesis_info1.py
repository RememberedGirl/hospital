# Generated by Django 4.0.3 on 2022-05-10 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bd_team', '0011_anamnesis'),
    ]

    operations = [
        migrations.AddField(
            model_name='anamnesis',
            name='info1',
            field=models.TextField(null=True, verbose_name='Информация'),
        ),
    ]
