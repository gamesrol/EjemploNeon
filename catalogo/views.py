from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Group, Permission
from .models import Autor, Categoria, Libro
from .forms import AutorForm, CategoriaForm, LibroForm, RegistroUsuarioForm

# EL LISTADO (READ múltiple del CRUD)
def vista_catalogo(request):
    # ORM: Toma todos los libros de la base de datos
    todos_los_libros = Libro.objects.all()
    # 'render' une el diccionario de ingredientes Python con el diseño HTML base.
    return render(request, 'catalogo.html', {'libros': todos_los_libros})

# EL DETALLE (READ individual del CRUD)
def vista_detalle(request, id_libro):
    # Si piden el id 99 pero no existe, levanta de golpe una pantalla 404 Not Found automáticamente
    libro_seleccionado = get_object_or_404(Libro, id=id_libro)
    return render(request, 'detalle_libro.html', {'libro': libro_seleccionado})

@permission_required('catalogo.add_libro')
def vista_crear_libro(request):
    if request.method == "POST":
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save() # ¡PUM! INSERT mágico a la base de datos sin SQL
            return redirect('catalogo')
    else:
        form = LibroForm() # Formulario en blanco esperando
        
    return render(request, 'formulario.html', {'form': form})

@permission_required('catalogo.change_libro')
def vista_editar_libro(request, id_libro):
    libro_viejo = get_object_or_404(Libro, id=id_libro)
    if request.method == "POST":
        # Metemos los datos nuevos (POST), pero avisando de que sobreescriban a (instance=libro_viejo)
        form = LibroForm(request.POST, instance=libro_viejo)
        if form.is_valid():
            form.save()
            return redirect('detalle', id_libro=libro_viejo.id)
    else:
        form = LibroForm(instance=libro_viejo) # Formulario YA relleno
    return render(request, 'formulario.html', {'form': form})


@permission_required('catalogo.delete_libro')
def vista_borrar_libro(request, id_libro):
    libro = get_object_or_404(Libro, id=id_libro)
    if request.method == "POST":
        libro.delete()
        return redirect('catalogo')
    return render(request, 'confirmar_borrado.html', {'libro': libro})


# EL REGISTRO: crea el usuario y lo mete en el grupo "Autores Junior":
def vista_registro(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()

            # Crear el grupo si aún no existe y darle permiso para gestionar libros
            grupo, _ = Group.objects.get_or_create(name='Autores Junior')
            grupo.permissions.set([
                Permission.objects.get(codename='add_libro'),
                Permission.objects.get(codename='change_libro'),
            ])
            usuario.groups.add(grupo)

            login(request, usuario)  # Login automático tras registrarse
            return redirect('catalogo')
    else:
        form = RegistroUsuarioForm()

    return render(request, 'registration/registro.html', {'form': form})


def vista_lista_autores(request):
    todos_los_autores = Autor.objects.all()
    return render(request, 'lista_autores.html', {'autores': todos_los_autores})


def vista_lista_categorias(request):
    todas_las_categorias = Categoria.objects.all()
    return render(request, 'lista_categorias.html', {'categorias': todas_las_categorias})


@permission_required('catalogo.add_autor')
def vista_crear_autor(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('autores')
    else:
        form = AutorForm()

    return render(request, 'formulario.html', {'form': form, 'titulo_formulario': '✍️ Añadir autor'})


@permission_required('catalogo.change_autor')
def vista_editar_autor(request, id_autor):
    autor = get_object_or_404(Autor, id=id_autor)
    if request.method == "POST":
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('autores')
    else:
        form = AutorForm(instance=autor)

    return render(request, 'formulario.html', {'form': form, 'titulo_formulario': '✏️ Editar autor'})


@permission_required('catalogo.delete_autor')
def vista_borrar_autor(request, id_autor):
    autor = get_object_or_404(Autor, id=id_autor)
    if request.method == "POST":
        autor.delete()
        return redirect('autores')
    return render(request, 'confirmar_borrado_generico.html', {
        'objeto': autor,
        'tipo_nombre': 'el autor',
    })


@permission_required('catalogo.add_categoria')
def vista_crear_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categorias')
    else:
        form = CategoriaForm()

    return render(request, 'formulario.html', {'form': form, 'titulo_formulario': '🏷️ Añadir categoría'})


@permission_required('catalogo.change_categoria')
def vista_editar_categoria(request, id_categoria):
    categoria = get_object_or_404(Categoria, id=id_categoria)
    if request.method == "POST":
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('categorias')
    else:
        form = CategoriaForm(instance=categoria)

    return render(request, 'formulario.html', {'form': form, 'titulo_formulario': '✏️ Editar categoría'})


@permission_required('catalogo.delete_categoria')
def vista_borrar_categoria(request, id_categoria):
    categoria = get_object_or_404(Categoria, id=id_categoria)
    if request.method == "POST":
        categoria.delete()
        return redirect('categorias')
    return render(request, 'confirmar_borrado_generico.html', {
        'objeto': categoria,
        'tipo_nombre': 'la categoría',
    })