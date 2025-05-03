from flask import Flask, render_template

#objeto app
app= Flask (__name__)

#ruta llamado paginas
#llamar layout
@app.route('/')
def home():
    return render_template('layout.html')
    
#llamara rentas
@app.route('/rentas')
def rentas():
    return render_template('rentas.html')

#llamar desarrollo y creacion
@app.route('/desarrollo_y_creacion')
def desycre():
    return render_template('desycre.html')

#llamar soporte tecnico
@app.route('/soporte_tecnico')
def soptec():
    return render_template('soptec.html')

#llamar cotizacion web
@app.route('/cotizacion_web')
def cotweb():
    return render_template('cotweb.html')

if __name__ == "__main__":
    app.run(debug=True)
