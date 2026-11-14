from flask import Flask
import random

app = Flask(__name__)

facts_list = [
    "La dependencia tecnológica puede llevar a la pérdida de habilidades básicas.",
    "El uso excesivo de la tecnología puede afectar la salud mental y física.",
    "La tecnología puede crear una brecha entre generaciones.",
    "La dependencia tecnológica puede afectar la productividad y la concentración.",
    "El uso constante de dispositivos electrónicos puede afectar la calidad del sueño."]


@app.route("/")
def index():
    return '<h1>Hola, en esta pagina puedes aprender sobre la dependencia tecnologica</h1><a href="/random_facts">Click para un dato aleatorio<a>\n <a href="/about">Sobre esta pagina<a> '
    

@app.route("/random_facts")
def facts():
    return f'<p>{random.choice(facts_list)}</p>'

@app.route("/about")
def about():
    return'<p>Esta pagina fue hecha para concientizar sobre la dependencia tecnologica<p>'

@app.route("/super_ultra_secret_website_thingy_lol")
def FUNCTION_NAME():
    return'<p>?????<p>'
app.run(debug=True)
