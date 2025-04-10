from flask import Flask, render_template, request, redirect

app = Flask(__name__)

personas = []

@app.route('/')
def index():
    return render_template('index.html', personas=personas)

@app.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = request.form['edad']
        personas.append({'id': len(personas)+1, 'nombre': nombre, 'edad': edad})
        return redirect('/')
    return render_template('crear.html')

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    persona = next((p for p in personas if p['id'] == id), None)
    if request.method == 'POST':
        persona['nombre'] = request.form['nombre']
        persona['edad'] = request.form['edad']
        return redirect('/')
    return render_template('editar.html', persona=persona)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    global personas
    personas = [p for p in personas if p['id'] != id]
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
