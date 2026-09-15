from django.urls import path

from . import views

app_name = 'usuarios'

urlpatterns = [
    #FBV
    # path('alunos/',views.lista_alunos, name='aluno_lista'),
    #CBV
    path('alunos/', views.dashboard, name='aluno_dashboard'),
    path('alunos/lista/',views.AlunoListView.as_view(),name='aluno_lista'),
    path('alunos/novo/',views.criar_aluno,name='aluno_novo'),
    path('alunos/<int:pk>/editar',views.editar_aluno,name='aluno_editar'),
    path('aluno/<int:pk>',views.AlunoDetalhes.as_view(), name='aluno_detalhe'),
    path('alunos/<int:pk>/excluir',views.excluir_aluno, name='aluno_excluir'),
]