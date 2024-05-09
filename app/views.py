from django.shortcuts import render, redirect
from .models import Tarefa
from .forms import TarefaForm, LoginForm, CustomUserCreation
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


def login_page(request):    
    if request.method == 'POST':  # Verifica se o usuário está enviando dados através do método POST
        form = LoginForm(request.POST)  # Instancia o formulário com os dados submetidos pelo usuário
        
        if form.is_valid():  # Verifica se os dados submetidos são válidos de acordo com as regras do formulário
            user = authenticate(
                username=form.cleaned_data['nome'],  # Obtém o nome de usuário do formulário validado
                password=form.cleaned_data['senha'],  # Obtém a senha do formulário validado
            )  
            
            if user is not None:  # Verifica se o usuário foi autenticado com sucesso
                login(request, user)  # Autentica o usuário na sessão
                return redirect('/')  # Redireciona para a página inicial após o login
            else:
                form.add_error(None, 'Usuario ou senha incorreto')
    else:
        form = LoginForm()  # Se a requisição não for do tipo POST, instancia um novo formulário vazio
        
    context = {
        'form': form,  # Define o formulário como parte do contexto para ser renderizado no template
    }
    return render(request, 'app/login.html', context)  # Renderiza o template de login com o formulário


def custom_signup(request):
    if request.method == 'POST':
        form = CustomUserCreation(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = CustomUserCreation()
    context = {'form':form}
    return render(request, 'app/register_page.html', context)


@login_required
def sair_pagina(request):
    logout(request)
    return redirect('login')


@login_required
def index(request):
    form = TarefaForm()  # Aqui eu crio uma instância do TarefaForm para exibir no template

    if request.method == 'POST':  # Verifica se o usuário está submetendo um formulário
        form = TarefaForm(request.POST)  # Aqui eu crio uma instância do TarefaForm com os dados submetidos
        if form.is_valid():  # Verifica se os dados do formulário são válidos
            tarefa = form.save(commit=False)  # Salva os dados do formulário temporariamente no objeto tarefa sem salvar no banco de dados ainda
            tarefa.user = request.user  # Define o usuário da tarefa como o usuário atualmente logado
            tarefa.save()  # Salva a tarefa no banco de dados
            return redirect('/')  # Redireciona o usuário de volta para a página inicial após a submissão do formulário
    else:
        form = TarefaForm()  # Se não for uma solicitação POST, apenas crio uma nova instância do TarefaForm para exibir no template

    tarefas = Tarefa.objects.filter(user=request.user)  # Aqui eu filtro as tarefas do banco de dados para exibir apenas as do usuário atual

    context = {'tarefas': tarefas, 'form': form}  # Passa as tarefas e o formulário para o template

    return render(request, 'app/index.html', context)  # Renderiza o template


@login_required  # Define que é necessário estar logado para acessar essa view
def update_task(request, pk):  # Define uma função de view para atualizar uma tarefa com base no seu ID (pk)
    # Obtém a instância da tarefa com base no ID fornecido
    tarefa = Tarefa.objects.get(id=pk)

    if request.method == 'POST':  # Verifica se o método da requisição é POST (ou seja, se o formulário foi submetido)
        # Se a requisição for do tipo POST, cria um formulário com os dados da requisição e a instância da tarefa
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():  # Verifica se os dados submetidos são válidos de acordo com as regras do formulário
            form.save()  # Salva os dados da tarefa atualizados no banco de dados
            return redirect('/')  # Redireciona o usuário para a página inicial após a atualização da tarefa
    else:
        # Se a requisição não for do tipo POST, cria um formulário com a instância da tarefa
        form = TarefaForm(instance=tarefa)
        
    # Cria um contexto contendo o formulário para ser usado no template
    context = {'form':form}
    # Renderiza o template 'update_task.html', passando o contexto criado
    return render(request, 'app/update_task.html', context)



@login_required
def delete_task(request, pk):
    item = Tarefa.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')
        
    context = {'item':item}
    return render(request, 'app/delete_task.html', context)


    

