from flask import Flask, request, redirect, render_template_string
import json
import os

app = Flask(__name__)
ARCHIVO_JSON = 'Libros.json'

def leer_libros():
    if not os.path.exists(ARCHIVO_JSON):
        return []
    with open(ARCHIVO_JSON, 'r', encoding='utf-8') as f:
        return json.load(f)

def guardar_libros(libros):
    with open(ARCHIVO_JSON, 'w', encoding='utf-8') as f:
        json.dump(libros, f, indent=2, ensure_ascii=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        titulo = request.form.get('titulo', '').strip()
        autor = request.form.get('autor', '').strip()
        fecha = request.form.get('fecha', '').strip()
        editorial = request.form.get('editorial', '').strip()

        if titulo and autor:
            libros = leer_libros()
            nuevo_libro = {
                'titulo': titulo,
                'autor': autor,
                'fecha_publicacion': fecha,
                'editorial': editorial
            }
            libros.append(nuevo_libro)
            guardar_libros(libros)
        return redirect('/')

    libros = leer_libros()

    html = '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Parte 3</title>
        <style>
            body {
                font-family: Arial, sans-serif;
            }
            .seccion {
                display: none;
                margin-top: 20px;
            }
            .botones {
                margin-top: 10px;
            }
        </style>
    </head>
    <body>
        <h1>Parte 3</h1>
        <h2>Libros Libritos</h2>

        <div class="botones">
            <button onclick="mostrarInicio()">Inicio</button>
            <button onclick="mostrarSeccion('formulario')">Agregar libro</button>
            <button onclick="mostrarSeccion('lista')">Listar libros</button>
        </div>

        <div id="inicio" class="seccion" style="display: block;">
            <p><em>Aquí pondría la publicidad, esta página no se paga sola</em></p>
        </div>

        <div id="formulario" class="seccion">
            <h3>Agregar Libro</h3>
            <form method="post">
                <label>Título: <input type="text" name="titulo" required></label><br>
                <label>Autor: <input type="text" name="autor" required></label><br>
                <label>Fecha de Publicación: <input type="text" name="fecha"></label><br>
                <label>Editorial: <input type="text" name="editorial"></label><br>
                <button type="submit">Agregar</button>
            </form>
        </div>

        <div id="lista" class="seccion">
            <h3>Libros guardados</h3>
            <ul>
            {% for libro in libros %}
                <li>
                    <strong>{{ libro.titulo }}</strong> - {{ libro.autor }}
                    {% if libro.fecha_publicacion %} ({{ libro.fecha_publicacion }}){% endif %}
                    {% if libro.editorial %} | Editorial: {{ libro.editorial }}{% endif %}
                </li>
            {% else %}
                <li>No hay libros guardados aún.</li>
            {% endfor %}
            </ul>
        </div>

        <script>
            function ocultarTodo() {
                document.getElementById('inicio').style.display = 'none';
                document.getElementById('formulario').style.display = 'none';
                document.getElementById('lista').style.display = 'none';
            }

            function mostrarSeccion(id) {
                ocultarTodo();
                document.getElementById(id).style.display = 'block';
            }

            function mostrarInicio() {
                ocultarTodo();
                document.getElementById('inicio').style.display = 'block';
            }
        </script>
    </body>
    </html>
    '''
    return render_template_string(html, libros=libros)

if __name__ == '__main__':
    app.run(debug=True)
