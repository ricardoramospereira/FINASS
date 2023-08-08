from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.messages import constants
from django.contrib.auth.models import User



def is_password_similar_to_username(password, username):
    """
    Verifica se a senha é muito semelhante ao nome de usuário.
    Retorna True se a senha for semelhante, False caso contrário.
    """
    password = password.lower()
    username = username.lower()
    return username in password


def register(request):
    if request.method == 'GET':    
        return render(request, 'users/register.html')
    
    elif request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # TODO: validações 
        if (len(name.strip()) == 0) or (len(email.strip()) == 0) or (len(password.strip()) == 0) or (len(confirm_password.strip()) == 0):
            messages.add_message(request, constants.ERROR, "Todos os campos devem ser preenchidos")
            return redirect('/auth/register')
        
        if password != confirm_password:
            messages.add_message(request, constants.ERROR, "As senhas não correspondem")
            return redirect('/auth/register')
        
           # Verificar se a senha é semelhante ao nome de usuário
        if is_password_similar_to_username(password, name):
            messages.add_message(request, constants.ERROR, "A senha é muito semelhante ao nome de usuário")
            return redirect('/auth/register')
        
        user = User.objects.filter(email=email)

        if user.exists():
            messages.add_message(request, constants.ERROR, "O email já existe")
            return redirect('/auth/register')
        
        else:
            try:
                user = User.objects.create_user(username=name, email=email, password=password)
                
                user.save()
                messages.add_message(request, constants.SUCCESS, "Usuário cadastrado com sucesso")
                return redirect('/auth/register')
            
            except:
                messages.add_message(request, constants.ERROR, "Erro interno do sistema")
                return redirect('/auth/register')
                



def login(request):
    return render(request, 'users/login.html')