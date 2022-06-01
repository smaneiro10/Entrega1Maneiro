from django.shortcuts import render
from django.db.models import Q
from django.forms.models import model_to_dict

from app_jugadores.models import *
from app_jugadores.forms import *


def index(request):
    return render(request, "home.html")


def jugadores(request):
    jugadores = Jugadores.objects.all()

    context_dict = {
        'jugadores': jugadores
    }

    return render(
        request=request,
        context=context_dict,
        template_name="jugadores.html"
    )


def club(request):
    club = Club.objects.all()

    context_dict = {
        'club': club
    }

    return render(
        request=request,
        context=context_dict,
        template_name="clubes.html"
    )


def liga(request):
    liga = Liga.objects.all()

    context_dict = {
        'liga': liga
    }

    return render(
        request=request,
        context=context_dict,
        template_name="ligas.html"
    )


def form_hmtl(request):

    if request.method == 'POST':
        jugador = Jugadores(nombre=request.POST['nombre'], equipo=request.POST['equipo'])
        jugador.save()

        jugadores = Jugadores.objects.all()
        context_dict = {
            'jugadores': jugadores
        }

        return render(
            request=request,
            context=context_dict,
            template_name="jugadores.html"
        )

    return render(
        request=request,
        template_name='formHTML.html'
    )


def jugador_forms_django(request):
    if request.method == 'POST':
        jugador_form = JugadoresForm(request.POST)
        if jugador_form.is_valid():
            data = jugador_form.cleaned_data
            jugador = Jugadores(nombre=data['nombre'], equipo=data['equipo'], fecha_nacimiento=data['fecha de nacimiento'])
            jugador.save()

            jugadores = Jugadores.objects.all()
            context_dict = {
                'jugadores': jugadores
            }
            return render(
                request=request,
                context=context_dict,
                template_name="C:/Pjugadores/app_jugadores/templates/jugadores.html"
            )

    jugador_form = JugadoresForm(request.POST)
    context_dict = {
        'jugador_form': jugador_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='jugadores_django_forms.html'
    )

def club_forms_django(request):
    if request.method == 'POST':
        club_form = ClubForm(request.POST)
        if club_form.is_valid():
            data = club_form.cleaned_data
            club = Club(nombre=data['club'], provincia=data['provincia'], localidad=data['localidad'])
            club.save()

            clubes = Club.objects.all()
            context_dict = {
                'clubes': clubes
            }
            return render(
                request=request,
                context=context_dict,
                template_name="C:/Pjugadores/app_jugadores/templates/clubes.html"
            )

    club_form = ClubForm(request.POST)
    context_dict = {
        'club_form': club_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='clubes_django_forms.html'
    )


def liga_forms_django(request):
    if request.method == 'POST':
        liga_form = LigaForm(request.POST)
        if liga_form.is_valid():
            data = liga_form.cleaned_data
            liga = Liga(torneo=data['torneo'], equipos=data['equipos'], internacional=data['internacional'])
            liga.save()

            ligas = Liga.objects.all()
            context_dict = {
                'ligas': ligas
            }
            return render(
                request=request,
                context=context_dict,
                template_name="C:/Pjugadores/app_jugadores/templates/ligas.html"
            )

    liga_form = LigaForm(request.POST)
    context_dict = {
        'liga_form': liga_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='ligas_django_forms.html'
    )

# def profesor_forms_django(request):
#     if request.method == 'POST':
#         profesor_form = ProfesorForm(request.POST)
#         if profesor_form.is_valid():
#             data = profesor_form.cleaned_data
#             profesor = Profesor(
#                 name=data['name'],
#                 last_name=data['last_name'],
#                 email=data['email'],
#                 profession=data['profession'],
#             )
#             profesor.save()

#             profesors = Profesor.objects.all()
#             context_dict = {
#                 'profesors': profesors
#             }
#             return render(
#                 request=request,
#                 context=context_dict,
#                 template_name="app_jugadores/profesors.html"
#             )

#     profesor_form = ProfesorForm(request.POST)
#     context_dict = {
#         'profesor_form': profesor_form
#     }
#     return render(
#         request=request,
#         context=context_dict,
#         template_name='app_jugadores/profesor_django_forms.html'
#     )

# def update_profesor(request, pk: int):
#     profesor = Profesor.objects.get(pk=pk)

#     if request.method == 'POST':
#         profesor_form = ProfesorForm(request.POST)
#         if profesor_form.is_valid():
#             data = profesor_form.cleaned_data
#             profesor.name = data['name']
#             profesor.last_name = data['last_name']
#             profesor.email = data['email']
#             profesor.profession = data['profession']
#             profesor.save()

#             profesors = Profesor.objects.all()
#             context_dict = {
#                 'profesors': profesors
#             }
#             return render(
#                 request=request,
#                 context=context_dict,
#                 template_name="app_jugadores/profesors.html"
#             )

#     profesor_form = ProfesorForm(model_to_dict(profesor))
#     context_dict = {
#         'profesor': profesor,
#         'profesor_form': profesor_form,
#     }
#     return render(
#         request=request,
#         context=context_dict,
#         template_name='app_jugadores/profesor_form.html'
#     )


# def delete_profesor(request, pk: int):
#     profesor = Profesor.objects.get(pk=pk)
#     if request.method == 'POST':
#         profesor.delete()

#         profesors = Profesor.objects.all()
#         context_dict = {
#             'profesors': profesors
#         }
#         return render(
#             request=request,
#             context=context_dict,
#             template_name="app_jugadores/profesors.html"
#         )

#     context_dict = {
#         'profesor': profesor,
#     }
#     return render(
#         request=request,
#         context=context_dict,
#         template_name='app_jugadores/profesor_confirm_delete.html'
#     )


# def homework_forms_django(request):
#     if request.method == 'POST':
#         homework_form = HomeworkForm(request.POST)
#         if homework_form.is_valid():
#             data = homework_form.cleaned_data
#             homework = Homework(
#                 name=data['name'],
#                 due_date=data['due_date'],
#                 is_delivered=data['is_delivered'],
#             )
#             homework.save()

#             homeworks = Homework.objects.all()
#             context_dict = {
#                 'homeworks': homeworks
#             }
#             return render(
#                 request=request,
#                 context=context_dict,
#                 template_name="app_jugadores/homeworks.html"
#             )

#     homework_form = HomeworkForm(request.POST)
#     context_dict = {
#         'homework_form': homework_form
#     }
#     return render(
#         request=request,
#         context=context_dict,
#         template_name='app_jugadores/homework_django_forms.html'
#     )


def search(request):
    context_dict = dict()
    if request.GET['jugador_search']:
        search_param = request.GET['jugador_search']
        jugadores = Jugadores.objects.filter(jugador__contains=search_param)
        context_dict = {
            'jugadores': jugadores
        }
    elif request.GET['club_search']:
        search_param = request.GET['club_search']
        clubes = Club.objects.filter(club__contains=search_param)
        context_dict = {
            'clubes': clubes
        }
    elif request.GET['all_search']:
        search_param = request.GET['all_search']
        query = Q(jugador__contains=search_param)
        query.add(Q(club__contains=search_param), Q.OR)
        jugadores = Jugadores.objects.filter(query)
        context_dict = {
            'jugadores': jugadores
        }

    return render(
        request=request,
        context=context_dict,
        template_name="app_jugadores/home.html",
    )

from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class JugadoresListView(ListView):
    model = Jugadores
    template_name = "jugadores_list.html"


class JugadoresDetailView(DetailView):
    model = Jugadores
    template_name = "jugadores_detail.html"


class JugadoresCreateView(CreateView):
    model = Jugadores
    template_name = "jugadores_form.html"
    # success_url = "/app_jugadores/courses"
    success_url = reverse_lazy('jugadores-list')
    fields = ['nombre', 'equipo', 'fecha_nacimiento']


class JugadoresUpdateView(UpdateView):
    model = Jugadores
    template_name = "jugadores_form.html"
    # success_url = "jugadores.html"
    success_url = reverse_lazy('jugadores-list')
    fields = ['nombre', 'equipo', 'fecha_nacimiento']


class JugadoresDeleteView(DeleteView):
    model = Jugadores
    template_name = "jugadores_confirm_delete.html"
    # success_url = "/app_jugadores/courses"
    success_url = reverse_lazy('jugadores-list')

#################

class ClubListView(ListView):
    model = Club
    template_name = "clubes_list.html"


class ClubDetailView(DetailView):
    model = Club
    template_name = "clubes_detail.html"


class ClubCreateView(CreateView):
    model = Club
    template_name = "clubes_form.html"
    # success_url = "/app_jugadores/courses"
    success_url = reverse_lazy('clubes-list')
    fields = ['nombre', 'provincia', 'localidad']


class ClubUpdateView(UpdateView):
    model = Club
    template_name = "clubes_form.html"
    # success_url = "jugadores.html"
    success_url = reverse_lazy('clubes-list')
    fields = ['nombre', 'provincia', 'localidad']


class ClubDeleteView(DeleteView):
    model = Club
    template_name = "clubes_confirm_delete.html"
    # success_url = "/app_jugadores/courses"
    success_url = reverse_lazy('clubes-list')

#################

class LigaListView(ListView):
    model = Liga
    template_name = "ligas_list.html"


class LigaDetailView(DetailView):
    model = Liga
    template_name = "ligas_detail.html"


class LigaCreateView(CreateView):
    model = Liga
    template_name = "ligas_form.html"
    # success_url = "/app_jugadores/courses"
    success_url = reverse_lazy('ligas-list')
    fields = ['torneo', 'equipos', 'internacional']


class LigaUpdateView(UpdateView):
    model = Liga
    template_name = "ligas_form.html"
    # success_url = "jugadores.html"
    success_url = reverse_lazy('ligas-list')
    fields = ['torneo', 'equipos', 'internacional']


class LigaDeleteView(DeleteView):
    model = Liga
    template_name = "ligas_confirm_delete.html"
    # success_url = "/app_jugadores/courses"
    success_url = reverse_lazy('ligas-list')