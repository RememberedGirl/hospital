import json
import pandas as pd
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.views import LoginView
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, SimpleDocTemplate, Table, TableStyle, Spacer,KeepTogether,tables
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import A4,landscape
from reportlab.lib.units import inch,cm,mm
from reportlab.platypus import PageBreak
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import fileName2FSEnc

from .forms import *
from .permission import *
from .DataMixin import *

class MainPage(DataMixin, ListView):
    model = Player
    login_url = reverse_lazy('login')
    template_name = 'bd_team/main.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        context = dict(list(context.items()) + list(c_def.items()))
        return context

# -------Work player -------

class AddPlayer(DataMixin, MyPermissionMixin, CreateView):
    raise_exception = False
    model = Player
    fields = '__all__'
    permission_required = 'bd_team.add_player'
    template_name = 'bd_team/add_player.html'
    success_url = reverse_lazy('list_players')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление врача")
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class PlayerUpdateView(DataMixin, MyPermissionMixin, DoctorPermissionMixin, UpdateView):
    model = Player
    permission_required = 'bd_team.change_player'
    template_name = 'bd_team/update.html'
    form_class = PlayerForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Изменение данных врача")
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class PlayerDeleteView(DataMixin, MyPermissionMixin, DeleteView):
    model = Player
    permission_required = 'bd_team.delete_player'
    fields = '__all__'
    success_url = reverse_lazy('list_players')
    template_name = 'bd_team/delete.html'

#@permission_required('bd_team.view_player')
def show_player_card(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    context = get_user_context()
    context['player'] = player
    context['title'] = 'Карточка врача'
    return render(request, 'bd_team/card_player.html', context)

#masha code patient
class AddPatient(DataMixin, MyPermissionMixin, CreateView):
    raise_exception = False
    model = Patient
    fields = '__all__'
    permission_required = 'bd_team.add_patient'
    template_name = 'bd_team/add_patient.html'
    success_url = reverse_lazy('list_patients')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление пациента")
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class PatientUpdateView(DataMixin, MyPermissionMixin, UpdateView):
    model = Patient
    permission_required = 'bd_team.change_patient'
    template_name = 'bd_team/update_patient.html'
    form_class = PatientForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Изменение данных пациента")
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class PatientDeleteView(DataMixin, MyPermissionMixin, DeleteView):
    model = Patient
    permission_required = 'bd_team.delete_patient'
    fields = '__all__'
    success_url = reverse_lazy('list_patients')
    template_name = 'bd_team/delete_patient.html'


@permission_required('bd_team.view_patient')
def show_patient_card(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    context = get_user_context()
    context['patient'] = patient
    context['title'] = 'Карточка пациента'
    return render(request, 'bd_team/card_patient.html', context)
#end masha code patiente

class AnamnesisCreateView(DataMixin, MyPermissionMixin, CreateView):
    model = Anamnesis
    permission_required = 'bd_team.add_anamnesis'
    template_name = 'bd_team/add_anamnesis.html'
    success_url = reverse_lazy('list_anamnesis')
    fields = '__all__'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление болезни")
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class AnamnesisUpdateView(DataMixin, MyPermissionMixin, UpdateView):
    model = Anamnesis
    permission_required = 'bd_team.change_anamnesis'
    template_name = 'bd_team/update.html'
    success_url = reverse_lazy('list_anamnesis')
    form_class = AnamnesisForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title= "Изменение время")
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class AnamnesisDeleteView(DataMixin, MyPermissionMixin, DeleteView):
    model = Anamnesis
    permission_required = 'bd_team.delete_anamnesis'
    fields = '__all__'
    success_url = reverse_lazy('list_anamnesis')
    template_name = 'bd_team/delete.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удаление время")
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class ListChartAnamnesis(DataMixin, ListView):
    model = Anamnesis
    template_name = 'bd_team/list_anamnesis.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="История болезней",
                                      head= ['Диагноз', 'Начало', 'Конец', 'Описание', 'Симптомы', 'Лечение', 'Лечащий Врач'], act=True
                                      )
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class ListChartAnamnesisDoctor(DataMixin, ListView):
    model = Anamnesis
    template_name = 'bd_team/list_anamnesis.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        patientid = self.kwargs['patient']
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="История болезни",
                                      doctor = patientid,
                                      #head =['Кабинет', 'Начало', 'Конец', 'День недели', 'Врач'], act=True
                                      head= ['Диагноз', 'Начало', 'Конец', 'Описание', 'Симптомы', 'Лечение', 'Лечащий Врач'], act=True
                                      )
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#end masha code anamnesis

class ListPlayer(DataMixin, ListView):
    model = Player
    template_name = 'bd_team/players_list.html'

    permission_required = 'bd_team.view_players'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title= "Список врачей", head= [ 'Имя', 'Специализация'])
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#@permission_required('bd_team.view_patient')
class ListPatient(DataMixin, MyPermissionMixin, ListView):
    model = Patient
    template_name = 'bd_team/patients_list.html'

    permission_required = 'bd_team.view_patient'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title= "Список пациентов", head= ['Имя', 'Гендер', 'Дата рождения'])
        context = dict(list(context.items()) + list(c_def.items()))
        return context



# -------Work game -------

class GameCreateView(DataMixin, MyPermissionMixin, CreateView):
    model = Game
    permission_required = 'bd_team.add_game'
    template_name = 'bd_team/add_game.html'
    success_url = reverse_lazy('list_game')
    fields = '__all__'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление время")
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class GameUpdateView(DataMixin, MyPermissionMixin, UpdateView):
    model = Player_Game
    permission_required = 'bd_team.change_game'
    template_name = 'bd_team/update.html'
    success_url = reverse_lazy('list_game')
    form_class = GamePlayerForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title= "Изменение время")
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class GameDeleteView(DataMixin, MyPermissionMixin, DeleteView):
    model = Game
    permission_required = 'bd_team.delete_game'
    fields = '__all__'
    success_url = reverse_lazy('list_game')
    template_name = 'bd_team/delete.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Удаление время")
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class ListChartGame(DataMixin, ListView):
    model = Game
    template_name = 'bd_team/list_game.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Расписание врачей",
                                      head =['Кабинет', 'Начало', 'Конец', 'День недели', 'Врач'], act=True
                                      )
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class ListChartGameDoctor(DataMixin, ListView):
    model = Game
    template_name = 'bd_team/list_game.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        doctorid = self.kwargs['doctor']
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Расписание для врача",
                                      doctor = doctorid,
                                      head =['Кабинет', 'Начало', 'Конец', 'День недели', 'Врач'], act=True
                                      )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


# -------Work game info -------

def game_info(request, game_id):
    p_game = Player_Game.objects.filter(game_id=game_id).order_by('-count_washers')
    if Player_Game.check_game_status(game_id):
        context = get_user_context()
        context['title'] = 'Состав игроков'
        context['p_game'] = p_game
        context['head'] = ['№', 'Игрок', 'Кол-во шайб', 'Желтая карточка', 'Красная карточка']
        return render(request, 'bd_team/info_game.html', context)
    else:
        return redirect('list_game')


@permission_required('bd_team.add_player_game')
def add_game_info(request, game_id):
    if Player_Game.check_game_status(game_id):
        if request.method == 'POST':
            form = GamePlayerForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('list_game')
        else:
            form = GamePlayerForm(initial={'game': game_id})
        context = get_user_context()
        context['game_id'] = game_id
        context['title'] = 'Добавление в состав игры'
        context['form'] = form
        return render(request, 'bd_team/add_game_info.html', context)
    else:
        return redirect('list_game')


# -------Work archive -------



# -------User -------
def error(request):
    return render(request, 'bd_team/error.html', {})


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'bd_team/login.html'

    def get_success_url(self):
        return reverse_lazy('main_page')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Авторизация"
        context['but'] = "Войти"
        return context


def logout_user(request):
    logout(request)
    return redirect('login')



class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'bd_team/login.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Добавление пользователя"
        context['but'] = "Добавить"
        return context


# -------Export -------

def export_exel_game(request):
    game = Game.objects.values()
    #.filter(archive=fl).values()
    df = pd.DataFrame(game)
    #if fl:
    #    df.to_excel('F:/file/game_archive.xlsx')
    #    return redirect('archive_game')
    #else:
    df.to_excel('C:/Users/quuu131/Documents/bgtu/export/game_active.xlsx')
    return redirect('list_game')


def export_json_game(request):
    game = Game.objects.all()
    #.filter(archive=fl)
    game_json = serializers.serialize('json', game)
    with open('C:/Users/quuu131/Documents/bgtu/export/game_active.json', 'w') as f:
        f.write(json.dumps(game_json))
    return redirect('list_game')


def export_pdf_game(request):
    game = Game.objects.all()
    #.filter(archive=fl)
    styleSheet = getSampleStyleSheet()

    pdfmetrics.registerFont(TTFont('DejaVuSerif', 'DejaVuSerif.ttf', 'UTF-8'))

    def StringGuy(text):
        return f'<font name="DejaVuSerif">{text}</font>'

    def ParagGuy(text, style=styleSheet['Normal']):
        return Paragraph(StringGuy(text), styleSheet['Normal'])

    data = [[ParagGuy('Кабинет'),
             ParagGuy('Начало приёма'),
             ParagGuy('Конец приёма'),
             ParagGuy('день недели'),
             ParagGuy('Врач'),
             ]
            ]
    list = []

    for g in game:
        #['room', 'time0', 'time1', 'day', 'doctor']
        list.append(ParagGuy(g.room))
        list.append(ParagGuy(g.time0))
        list.append(ParagGuy(g.time1))
        list.append(ParagGuy(g.day))
        list.append(ParagGuy(g.doctor))
        data.append(list)
        list = []
        fileName = 'C:/Users/quuu131/Documents/bgtu/export/ActiveGame.pdf'

    pdf = SimpleDocTemplate(
        fileName,
        pagesize=letter
    )

    table = Table(data)

    style = TableStyle([
        ('BACKGROUND', (0, 0), (6, 0), colors.green),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Courier-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ])
    table.setStyle(style)

    table.setStyle(TableStyle([('ALIGN', (1, 1), (-2, -2), 'RIGHT'),
                            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                            ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
                            ]))
    elems = []
    elems.append(table)
    pdf.build(elems)

    return redirect('list_game')
