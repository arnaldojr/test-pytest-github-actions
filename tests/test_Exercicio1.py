import nbformat
import sys
from io import StringIO
from IPython import get_ipython

# Função para executar o notebook e obter a função soma
def get_function_from_notebook(notebook_path):
    with open(notebook_path, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)
        for cell in nb.cells:
            if cell.cell_type == "code":
                exec(cell.source, globals())

get_function_from_notebook("exercicios/Exercicio1.ipynb")


def test_exercicio1():
    assert nome == "Python"

def test_exercicio2():
    assert tipo_valor == type(123.45)

def test_exercicio3():
    assert resultado_soma == 30

def test_exercicio4():
    assert x_maior_que_y == True


def test_soma():
    assert soma(2, 3) == 5
    assert soma(4, 5) == 9
    assert soma(-1, 1) == 0 

def test_soma_real():
    assert soma(2.3, 3) == 5.3
    assert soma(4, 5.02) == 9.02
    assert round(soma(-1.01, 1),2) == -0.01 

def test_subtrai():
    assert subtrai(3, 2) == 1
    assert subtrai(4, 5) == -1
    assert subtrai(-1, 1) == -2 

def test_multiplica():
    assert multiplica(3, 2) == 6
    assert multiplica(-4, 5) == -20
    assert multiplica(-1, 1) == -1 




