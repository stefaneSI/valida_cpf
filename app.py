from flask import Flask, request, render_template
import valida

app = Flask(__name__)

@app.route('/health')
def index():
    return render_template('index.html')

if valida.verifica_digitos('654654654528') == False:
    print('CPF invalido')
else:
    if valida.valida_cpf('654654654528') == False:
        print('CPF INVALIDO')
    else:
        print('CPF VALIDO')
    


#roda a aplicação localhost na porta 9095
if __name__ == '__main__':
    app.run(port=9095, host = '', debug=True)