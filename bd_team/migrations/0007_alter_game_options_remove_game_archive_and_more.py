# Generated by Django 4.0.3 on 2022-05-09 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bd_team', '0006_alter_player_options_remove_player_base_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='game',
            options={'ordering': ['room']},
        ),
        migrations.RemoveField(
            model_name='game',
            name='archive',
        ),
        migrations.RemoveField(
            model_name='game',
            name='area',
        ),
        migrations.RemoveField(
            model_name='game',
            name='date',
        ),
        migrations.RemoveField(
            model_name='game',
            name='judge',
        ),
        migrations.RemoveField(
            model_name='game',
            name='opponent',
        ),
        migrations.RemoveField(
            model_name='game',
            name='role',
        ),
        migrations.RemoveField(
            model_name='game',
            name='score',
        ),
        migrations.AddField(
            model_name='game',
            name='day',
            field=models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Sunday', 'Sunday')], default=0, max_length=10, verbose_name='Дата'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='doctor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='bd_team.player', verbose_name='Врач'),
        ),
        migrations.AddField(
            model_name='game',
            name='room',
            field=models.IntegerField(null=True, verbose_name='Кабинет'),
        ),
        migrations.AddField(
            model_name='game',
            name='time0',
            field=models.TimeField(null=True, verbose_name='Начало'),
        ),
        migrations.AddField(
            model_name='game',
            name='time1',
            field=models.TimeField(null=True, verbose_name='Конец'),
        ),
    ]
