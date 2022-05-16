menu = [{'title': "Врачи", 'url_name': 'list_players'},
        {'title': "Пациенты", 'url_name': 'list_patients'},
        {'title': "Расписание врачей", 'url_name': 'list_game'},
        {'title': "Выход", 'url_name': 'logout'},
        ]

class DataMixin:

    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context

def get_user_context():
    context = {
        'menu': menu,
    }
    return context