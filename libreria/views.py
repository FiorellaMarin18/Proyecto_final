from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import Libro
from .serializer import LibroSerializer

class LibroCreateView(generics.CreateAPIView):
    serializer_class = LibroSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class LibroListView(generics.ListAPIView):
    serializer_class = LibroSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Libro.objects.filter(usuario=self.request.user)

class LibroDetailView(generics.RetrieveAPIView):
    serializer_class = LibroSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Libro.objects.filter(usuario=self.request.user)

class LibroUpdateView(generics.UpdateAPIView):
    serializer_class = LibroSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Libro.objects.filter(usuario=self.request.user)

class LibroDeleteView(generics.DestroyAPIView):
    serializer_class = LibroSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Libro.objects.filter(usuario=self.request.user)

from django.shortcuts import render, get_object_or_404, redirect
from .models import Libro
from .forms import LibroForm
from django.contrib.auth.decorators import login_required

@login_required
def lista_libros(request):
    libros = Libro.objects.filter(usuario=request.user)
    return render(request, 'libreria/lista_libros.html', {'libros': libros})

@login_required
def detalle_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk, usuario=request.user)
    return render(request, 'libreria/detalle_libro.html', {'libro': libro})

@login_required
def agregar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            libro = form.save(commit=False)
            libro.usuario = request.user
            libro.save()
            return redirect('lista-libros')
    else:
        form = LibroForm()
    return render(request, 'libreria/libro_form.html', {'form': form})

@login_required
def editar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk, usuario=request.user)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('lista-libros')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'libreria/libro_form.html', {'form': form})

@login_required
def eliminar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk, usuario=request.user)
    if request.method == 'POST':
        libro.delete()
        return redirect('lista-libros')
    return render(request, 'libreria/libro_confirm_delete.html', {'libro': libro})
