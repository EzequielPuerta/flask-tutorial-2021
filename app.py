from flask import Flask

app = Flask(__name__)

# * 1) La primera ruta, vinculada con una función.
# *    Al ingresar a 127.0.0.1:5000, se evaluará la función hello()
@app.route("/")
def hello():
    return "Hello, world!"

# * 2) Es posible definir nuevas funciones para diferentes rutas...
# ?    Nota: ingresá a 127.0.0.1:5000/good_bye/
@app.route("/good_bye/")
def good_bye():
    return "Good bye cruel world..."

# * 3) También es posible vincular varias rutas con una misma función
# ?    Nota: De esto se deduce que la función no tiene porque llamarse
# ?          igual que la ruta a la que se vincula.
@app.route("/first/")
@app.route("/second/")
def times():
    return "Keep on trying!"

# * 4) Notar que las rutas deben terminar con '/' al ser definidas.
# *    De esta manera, podremos entrar indistintamente a 
# *     - 127.0.0.1:5000/good_bye/ ó
# *     - 127.0.0.1:5000/good_bye
# *    y ambas funcionarán. Algo que no funciona con la siguiente ruta:
@app.route("/failure")
def failure():
    return "Try entering 127.0.0.1:5000/failure/"

# * 5) Las funciones vinculadas a rutas pueden retornar básicamente
# *    strings, diccionarios y tuplas. También instancias de Response 
# *    y funciones WSGI, pero lo dejamos para más adelante. 
# ?    Dentro de un string, tranquilamente podemos incluir elementos 
# ?    HTML (aunque no sea lo mejor).
@app.route("/return/string/")
def return_string():
    return "<h1>Welcome!</1></br><h2>This is an example</h2>"

# ?    Dentro de un dicccionario, trabajaremos como si fuera un JSON
@app.route("/return/dict/")
def return_dict():
    return {
        "title":"<h1>Welcome!</h1>", 
        "subtitle":"<h2>This is an example</h2>",
        "string":"something...",
        "int":123,
        "float":3.1415,
        "bool":True,
        "list":[1,2,3],
        "tuple":(1,2,3),
        "dict":{"a":"1", "b":"2"}}

# ?    En el caso de las tuplas, son de la forma:
# ?     - (body, status, headers)
# ?     - (body, status)
# ?     - (body, headers)
# ?    Donde:
# ?     - body es nuevamente un string, dict o tupla.
# ?     - status es un int
# ?     - headers es un iterable
@app.route("/return/tuple/")
def return_tuple():
    return ("<h1>Welcome!</1></br><h2>This is an example</h2>", 200)

# * 6) Hasta ahora solo usamos rutas estáticas. Pero podemos generar 
# *    rutas dinámicas y obtener variables de ellas!
# ?    Nota: las rutas pueden ser tan largas como uno quiera y la
# ?          variable debe mantener el mismo nombre.
@app.route("/dynamic/random/<stuff>/")
def dynamic(stuff):
    return str(stuff)

# * 7) Podemos indicarle a Flask el tipo esperado de variable.
# ?    Nota: tipos válidos -> string, int, float, path, uuid
@app.route("/dynamic/string/<string:the_string_value>/")
def dynamic_string(the_string_value):
    return f"""Valor: {the_string_value}</br>
    Es string?: {isinstance(the_string_value, str)}</br>
    Representación: {repr(the_string_value)}"""

@app.route("/dynamic/int/<int:the_int_value>/")
def dynamic_int(the_int_value):
    return f"""Valor: {the_int_value}</br>
    Es entero?: {isinstance(the_int_value, int)}</br>
    Doble!: {the_int_value*2}</br>
    Representación: {repr(the_int_value)}"""

@app.route("/dynamic/float/<float:the_float_value>/")
def dynamic_float(the_float_value):
    return f"""Valor: {the_float_value}</br>
    Es decimal?: {isinstance(the_float_value, float)}</br>
    Doble!: {the_float_value*2}</br>
    Representación: {repr(the_float_value)}"""

@app.route("/dynamic/path/<path:the_path_value>/")
def dynamic_path(the_path_value):
    return f"""Valor: {the_path_value}</br>
    Es string?: {isinstance(the_path_value, str)}</br>
    Representación: {repr(the_path_value)}"""

# Ejemplo de UUID: 670b9562-b30d-52d5-b827-655787600000
@app.route("/dynamic/uuid/<uuid:the_uuid_value>/")
def dynamic_uuid(the_uuid_value):
    return f"""Valor: {the_uuid_value}</br>
    Es string?: {isinstance(the_uuid_value, str)}</br>
    Representación: {repr(the_uuid_value)}"""

# ! Incluyendo las siguientes líneas podremos activar el modo debug
# ! y ver los cambios sin tener que bajar y subir el servidor...
if __name__ == "__main__":
    app.run(debug=True)