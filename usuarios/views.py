from django.contrib import messages
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from usuarios.forms import UsuarioForm, AlunoForm
from usuarios.models import Aluno


# Create your views here.

#FBV
# def lista_alunos(request):
#     alunos = Aluno.objects.all()
#     return render(request,
#                   'usuarios/aluno/lista.html',
#                   {'alunos':alunos})

#CBV

def dashboard(request):
    return render(request, 'usuarios/aluno/dashboard.html')

class AlunoListView(ListView):
    model = Aluno
    template_name = 'usuarios/aluno/lista.html'
    context_object_name = 'alunos'


def criar_aluno(request):
    if request.method == 'POST':
        user_form = UsuarioForm(request.POST)
        aluno_form = AlunoForm(request.POST)
        if user_form.is_valid() and aluno_form.is_valid():
            try:
                with transaction.atomic():
                    user = user_form.save()
                    aluno = aluno_form.save(commit=False)
                    aluno.user = user
                    aluno.save()
                messages.success(request,'Aluno cadastrado com sucesso!')
                return redirect('usuarios:aluno_lista')
            except Exception:
                messages.error(request,'Não foi possível cadastrar o aluno')

    else:
        user_form = UsuarioForm()
        aluno_form = AlunoForm()
    return render(request, 'usuarios/aluno/form.html',{
            'user_form' : user_form,
            'aluno_form' : aluno_form,
        })

def editar_aluno(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == 'POST':
        aluno_form = AlunoForm(request.POST, instance=aluno)
        if aluno_form.is_valid():
            try:
                aluno_form.save()
                messages.success(request,'Aluno editado com sucesso!')
                return redirect('usuarios:aluno_lista')
            except Exception:
                messages.error(request,'Não foi possível editar o aluno')
    else:
        aluno_form = AlunoForm(instance=aluno)
    return render(request, 'usuarios/aluno/form.html',
                  {'aluno_form': aluno_form})


class AlunoDetalhes(DetailView):
    model = Aluno
    template_name = 'usuarios/aluno/detalhe.html'
    context_object_name = 'aluno'


@require_POST
def excluir_aluno(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    user = aluno.user
    try:
        user.delete()
        messages.success(request,'Aluno excluído com sucesso!')
    except Exception:
        messages.error(request,'Não foi possível excluir o aluno')
    return redirect('usuarios:aluno_lista')