# Generated by Django 4.0.3 on 2022-05-09 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bd_team', '0007_alter_game_options_remove_game_archive_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='game',
            options={'ordering': ['day']},
        ),
        migrations.AlterField(
            model_name='game',
            name='day',
            field=models.CharField(choices=[('0', 'Понедельник'), ('1', 'Вторник'), ('2', 'Среда'), ('3', 'Четверг'), ('4', 'Пятница'), ('5', 'Суббота'), ('6', 'Воскресенье')], max_length=10, verbose_name='Дата'),
        ),
    ]