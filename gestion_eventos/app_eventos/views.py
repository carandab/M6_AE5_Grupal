from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import permission_required
from django.views.generic import TemplateView
from .models import CustomUser
from .mixins import ProtectedTemplateView, PermissionProtectedTemplateView
from .forms import EventoForm, ParticipanteForm 

def inicio(request):
    return render(request, 'inicio.html')

def registrar_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            # Procesar datos
            nombre = form.cleaned_data['nombre']
            fecha = form.cleaned_data['fecha']
            ubicacion = form.cleaned_data['ubicacion']
            # Realizar alguna acción con los datos, como enviar un correo
            return render(request, 'formulario_exito.html', {'nombre': nombre})
    else:
        form = EventoForm()
    
    return render(request, 'formulario1.html', {'form': form})

def registrar_persona(request):
    if request.method == 'POST':
        form = ParticipanteForm(request.POST)
        if form.is_valid():
            # Procesar datos
            nombre = form.cleaned_data['nombre']
            correo = form.cleaned_data['correo']
            # Realizar algunaacción con los datos, como enviar un correo
            return render(request, 'formulario_exito.html', {'nombre': nombre})
    else:
        form = ParticipanteForm()
    
    return render(request, 'formulario2.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicio')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return render(request, 'logout.html')


def signup_view(request):
    from django.contrib.auth.models import Group
    
    # Creamos una clase inline que use CustomUser
    class CustomUserCreationForm(UserCreationForm):
        class Meta:
            model = CustomUser
            fields = ('username', 'email', 'first_name', 'last_name')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Asignar grupo según la selección del usuario
            group_name = request.POST.get('group')
            if group_name:
                try:
                    group = Group.objects.get(name=group_name)
                    user.groups.add(group)
                except Group.DoesNotExist:
                    # Si el grupo no existe, asignar permisos básicos
                    pass
            
            login(request, user)
            return redirect('inicio')
    else:
        form = CustomUserCreationForm()
    
    # Obtener grupos disponibles para mostrar en el template
    groups = Group.objects.all()
    
    return render(request, 'signup.html', {'form': form, 'groups': groups})
