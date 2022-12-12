from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from .models import Portafoleos
from .forms import formularioproyecto


# Create your views here.

def iniciar(request):
    yoselin = Portafoleos.objects.all()
    return render(request, 'index.html',{'yoselin':yoselin})

@login_required(login_url='login')
def portafoleo(request):
    formpro = formularioproyecto

    if request.method == 'POST':
        create_form = formularioproyecto(request.POST)

        if create_form.is_valid():
            titulo = request.POST.get('Titulos')
            descripcion = request.POST.get('Descripciones')
            tags = request.POST.get('Tags')
            imagen = request.POST.get('Fotos')
            url_github = request.POST.get('URL_GIT')

            proyecto = Portafoleos(imagenes=imagen,
                                titulos=titulo,
                                descripciones=descripcion,
                                tag=tags,
                                url_github=url_github)
            proyecto.save()

            return redirect('portafoleo')
        else:
            messages.warning(request, create_form.errors)
            return redirect('portafoleo')
    else:
        return render(request, 'portafoleo.html', {'forms': formpro})



@login_required(login_url='login')
def documento(request):
    return render(request, 'portafoleo.html')


def login(request):
    if request.method == 'POST':
        user = request.POST['user']
        paswoord = request.POST['paswoord']
        user = auth.authenticate(username=user, password=paswoord)
        if user is not None:
            auth.login(request, user)
            print("se logeo")
            return redirect('portafoleo')
        else:
            messages.success(request, 'Los datos son invalidos')
            return redirect('login')
    else:
        return render(request, 'login.html')



def insertar(request):
    # Si el motodo es POST
    if request.method == 'POST':
        user = request.POST['user']
        correo = request.POST['correo']
        name = request.POST["name"]
        apellido = request.POST["apellido"]
        paswoord = request.POST['paswoord']
        paswoords = request.POST['paswoords']

        # Compáro variables y los guardo en las variables
        if paswoord == paswoords:
            user = User.objects.create_user(
                username=user,
                first_name=name,
                last_name=apellido,
                email=correo, password=paswoord)
            user.save()
            #return redirect('logeador')
        else:
            messages.success(request, 'Las contraseñas no conciden')
            return redirect('insertar')

    return render(request, 'insertar.html')