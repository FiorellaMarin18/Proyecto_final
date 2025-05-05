from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import CustomUser
from .serializers import RegisterSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

class UserDetailUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth import get_user_model

def custom_logout_view(request):
    logout(request)
    return redirect('login')  # Redirige al login

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

    def form_invalid(self, form):
            messages.error(self.request, "Usuario o contraseña incorrectos.")
            return super().form_invalid(form)

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # INSERT en la base de datos
            messages.success(request, "Usuario creado correctamente. Ahora puedes iniciar sesión.")
            return redirect('login')
        else:
            messages.error(request, "Corrige los errores abajo.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

User = get_user_model()

def reset_password_view(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username_or_email')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if not username_or_email or not new_password or not confirm_password:
            messages.error(request, "Todos los campos son obligatorios.")
            return redirect('reset_password')

        if new_password != confirm_password:
            messages.error(request, "Las contraseñas no coinciden.")
            return redirect('reset_password')

        try:
            user = User.objects.get(username=username_or_email)
        except User.DoesNotExist:
            try:
                user = User.objects.get(email=username_or_email)
            except User.DoesNotExist:
                messages.error(request, "No se encontró ningún usuario con ese nombre o correo.")
                return redirect('reset_password')

        user.set_password(new_password)
        user.save()
        messages.success(request, "Contraseña actualizada correctamente. Inicia sesión.")
        return redirect('login')

    return render(request, 'accounts/reset_password.html')


