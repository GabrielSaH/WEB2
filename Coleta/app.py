from flask import Flask, render_template, request, redirect
import db

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/create-point")
def create_point():
    return render_template('create-point.html')


@app.route('/search-results', methods=['POST'])
def search_results():
    search_form = request.form.get('search')
    string_retorno = ""
    lista_pontos = db.search_and_get_by_city(search_form)
    for i in lista_pontos:
        string_result = ""
        for j in i:
            string_result += str(j) + ", "
        string_retorno += string_result + "<br>" 

    return string_retorno


# def search_results():
#     return render_template('search-results.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Extracting data from the form
    name = request.form.get('name')
    address = request.form.get('address')
    address2 = request.form.get('address2')
    state = request.form.get('uf')
    city = request.form.get('city')
    items = request.form.get('items')
    
    # The DB cant have any entry with " or ', it would break the query

    name = name.replace("'", "")
    name = name.replace('"', '')
    
    address = address.replace("'", "")
    address = address.replace('"', '')

    city = city.replace("'", "")
    city = city.replace('"', '')

    # Adding to the DB
    db.add_into_pontoColeta(name, address, address2, state, city, items)

    return redirect("/")