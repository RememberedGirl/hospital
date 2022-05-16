# Generated by Django 4.0 on 2021-12-28 17:27

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category_Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Специализация')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ФИО')),
                ('date_birth', models.DateField(null=True, verbose_name='Дата рождения')),
                ('citizenship', models.CharField(max_length=100, null=True, verbose_name='Гражданство')),
                ('photo', models.ImageField(null=True, upload_to='photos/', verbose_name='Фото')),
                ('base', models.BooleanField(default=False, verbose_name='Основа')),
                ('role', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='bd_team.category_player', verbose_name='Специализация')),
            ],
            options={
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Статус игры')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True, verbose_name='Дата')),
                ('opponent', models.CharField(max_length=100, null=True, verbose_name='Соперник')),
                ('area', models.BooleanField(default=False, null=True, verbose_name='Домашняя игра')),
                ('score', models.CharField(blank=True, max_length=5, null=True, validators=[django.core.validators.RegexValidator(message='Формат: 0:0', regex='\\d+:\\d+')], verbose_name='Счёт')),
                ('judge', models.CharField(blank=True, max_length=100, null=True, verbose_name='Cудья')),
                ('archive', models.BooleanField(default=False, verbose_name='Архив')),
                ('role', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='bd_team.status', verbose_name='Статус игры')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='BoardPlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indicator', models.IntegerField(default=0, verbose_name='Красная карточка')),
                ('biog', models.TextField(null=True)),
                ('player', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bd_team.player', verbose_name='Игрок')),
            ],
        ),
        migrations.CreateModel(
            name='Player_Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count_washers', models.IntegerField(default=0, verbose_name='Кол-во шайб')),
                ('yellow_card', models.IntegerField(default=0, verbose_name='Жёлтая карточка')),
                ('read_card', models.IntegerField(default=0, verbose_name='Красная карточка')),
                ('game', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bd_team.game', verbose_name='Игра')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bd_team.player', verbose_name='Игрок')),
            ],
            options={
                'unique_together': {('player', 'game')},
            },
        ),
    ]
