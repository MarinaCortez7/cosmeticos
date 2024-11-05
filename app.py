from flask import Flask,g,render_template,request,redirect
import sqlite3

def ligar_banco():
    banco=g._database=sqlite3.connect('Produtos.db')
    return banco

app = Flask(__name__)

@app.teardown_appcontext
def fechar_banco(exception):
    banco=ligar_banco()
    banco.close()


@app.route('/')
def home():
    return render_template('home.html', Titulo='Cadastro de Cosméticos')


@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html', Titulo='Cadastro de Produtos')

@app.route('/criar', methods=['POST','GET'])
def criar():
    banco=ligar_banco()
    cursor=banco.cursor()
    nome=request.form['nome']
    dataValidade=request.form['datavalidade']
    marca=request.form['marca']
    categoria=request.form['categoria']
    quantidade=request.form['quantidade']
    preco=request.form['preco']
    descricao=request.form['descricao']
    tipo= request.form['tipo']
    cursor.execute('''
        INSERT INTO Produtos
        (Nome,DataValidade,Marca,Categoria,Quantidade,Preço,Descrição,Tipo)
        VALUES (?,?,?,?,?,?,?,?);
    ''',
    (nome,dataValidade,marca,categoria,quantidade,preco,descricao,tipo)
    )
    banco.commit()
    return redirect('/produtos')

@app.route('/produtos')
def produtos():
    banco=ligar_banco()
    cursor=banco.cursor()
    cursor.execute('SELECT * FROM Produtos;')
    Produtos=cursor.fetchall()
    return render_template('cosmeticos.html', Titulo='Cadastro de Produtos', ListaProdutos=Produtos)



if __name__ == '__main__':
    app.run()
