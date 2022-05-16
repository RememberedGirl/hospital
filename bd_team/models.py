from django.contrib.auth.models import User, AbstractUser, Group
from django.core.validators import RegexValidator
from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone



class Status(models.Model):
    name = models.CharField(max_length=100, verbose_name='Статус игры')

    def __str__(self):
        return self.name

    def check_game(self):
        return self.id == 1


class Game(models.Model):

    class Weekday(models.TextChoices):
        mon = "Понедельник", "Понедельник"
        tue = "Вторник", "Вторник"
        wed = "Среда", "Среда"
        thu = "Четверг", "Четверг"
        fri = "Пятница", "Пятница"
        sat = "Суббота", "Суббота"
        sun = "Воскресенье", "Воскресенье"

    time0 = models.TimeField(null=True, verbose_name='Начало')
    time1 = models.TimeField(null=True, verbose_name='Конец')
    day = models.CharField(max_length=11, choices=Weekday.choices, verbose_name='Дата')
    doctor = models.ForeignKey('Player', on_delete=models.PROTECT, verbose_name="Врач", default=1)
    room = models.IntegerField(null=True, verbose_name='Кабинет')

    class Meta():
        ordering = ['day']

    def __str__(self):
        return f"{self.id}.{self.doctpr}_{self.room}"

    def get_absolute_url(self):
        return reverse('game_info', kwargs={'game_id': self.pk})

    def check_status(self):
        return Status.objects.get(name=self.role).check_game()


class Category_Player(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Специализация')

    def __str__(self):
        return self.name


class PublicInfoPlayer(models.Model):
    biog = models.TextField(null=True, blank=True, verbose_name='Отображаемая информация')
    public_photo = models.ImageField(null=True, blank=True, upload_to="photos/", verbose_name="Публичное Фото")
    class Meta:
        abstract = True

class PrivateInfoPlayer(models.Model):
    photo = models.ImageField(null=True, blank=True, upload_to="photos/", verbose_name="Фото")
    weight = models.IntegerField(null=True, verbose_name="Стаж лет")
    date_birth = models.DateField(null=True, verbose_name="Дата рождения")
    citizenship = models.CharField(max_length=100, null=True, verbose_name="Гражданство")
    class Meta:
        abstract = True

class Player(PrivateInfoPlayer, PublicInfoPlayer):
    name = models.CharField(max_length=100, null=False, verbose_name="ФИО")
    role = models.ForeignKey('Category_Player', on_delete=models.PROTECT,  null=True, verbose_name="Специализация")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь", blank=True)
    class Meta():
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('player', kwargs={'player_id': self.pk})

#masha code anamnesis
class Anamnesis(models.Model):
    diagnosis = models.CharField(null=True, verbose_name='Диагноз', max_length=100)
    info1 = models.TextField(null=True, verbose_name='Информация')
    info0 = models.TextField(null=True, verbose_name='Симптомы')
    info2 = models.TextField(null=True, verbose_name='Лечение')
    time0 = models.DateField(null=True, verbose_name='Начало')
    time1 = models.DateField(null=True, verbose_name='Конец',blank=True)
    patient = models.ForeignKey('Patient', on_delete=models.PROTECT, verbose_name="Пациент", default=1)
    doctor = models.ForeignKey('Player', on_delete=models.PROTECT, verbose_name="Врач", default=1)

    class Meta():
        ordering = ['time1']

    def __str__(self):
        return f"{self.id}.{self.patient}_{self.time0}"

    def get_absolute_url(self):
        return reverse('anamnesis_info', kwargs={'patient_id': self.pk})


#end masha code anamnesis



class Patient(models.Model):
    class Sex(models.TextChoices):
        male = "Муж", "Муж"
        female = "Жен", "Жен"

    name = models.CharField(max_length=100, null=False, verbose_name="ФИО")
    sex = models.CharField(max_length=11, choices=Sex.choices, verbose_name='Гендер')
    photo = models.ImageField(null=True, blank=True, upload_to="photos/", verbose_name="Фото")
    date_birth = models.DateField(null=True, verbose_name="Дата рождения")
    citizenship = models.CharField(max_length=100, null=True, verbose_name="Гражданство")

    class Meta():
        ordering = ['name']

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('patient', kwargs={'patient_id': self.pk})

class Player_Game(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, null=False, verbose_name='Игрок')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Игра')
    count_washers = models.IntegerField(default=0, verbose_name='Кол-во шайб')
    yellow_card = models.IntegerField(default=0, verbose_name='Жёлтая карточка')
    read_card = models.IntegerField(default=0, verbose_name='Красная карточка')

    class Meta():
        unique_together = ('player', 'game',)

    def __str__(self):
        return f"{self.player}:{self.game}"

    def get_absolute_url(self):
        return reverse('list_game', kwargs={})

    @staticmethod
    def check_game_status(id_game):
        game = Game.objects.get(id=id_game)
        print(game.check_status())
        return game.check_status()

