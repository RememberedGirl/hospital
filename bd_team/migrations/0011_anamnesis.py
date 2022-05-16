# Generated by Django 4.0.3 on 2022-05-10 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bd_team', '0010_patient'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anamnesis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnosis', models.CharField(max_length=100, null=True, verbose_name='Диагноз')),
                ('info0', models.TextField(null=True, verbose_name='Симптомы')),
                ('info2', models.TextField(null=True, verbose_name='Лечение')),
                ('time0', models.DateField(null=True, verbose_name='Начало')),
                ('time1', models.DateField(verbose_name='Конец')),
                ('doctor', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='bd_team.player', verbose_name='Врач')),
                ('patient', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='bd_team.patient', verbose_name='Пациент')),
            ],
            options={
                'ordering': ['time1'],
            },
        ),
    ]
