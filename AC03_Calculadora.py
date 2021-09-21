import abc
from unittest import TestCase, main

class Calculadora (object):

    def calcular(self, valor1, valor2, operador):
        operacaoFabrica = OperacaoFabrica()
        operacao = operacaoFabrica.criar(operador)
        if(operacao == None):
            return 0 
        else:
            resultado = operacao.executar(valor1, valor2)
            return resultado

class OperacaoFabrica(object):

    def criar(self, operador):
        if(operador == 'soma'):
            return Soma()
        elif (operador == 'subtracao'):
            return Subtracao()
        elif (operador == 'divisao'):
            return Divisao()
        elif (operador == 'multiplicacao'):
            return Multiplicacao()

class Operacao(metaclass=abc.ABCMeta):

    @abc.abstractclassmethod
    def executar(self, valor1, valor2):
        pass

class Soma(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 + valor2
        return resultado 

class Subtracao(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 - valor2
        return resultado

class Multiplicacao(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 * valor2
        return resultado

class Divisao(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 / valor2
        return resultado

class Testes(TestCase):

    def test_soma(self):
        calculador = Calculadora()
        result = calculador.calcular(6,2, 'soma')
        self.assertEqual(result, 8)

    def test_multiplicacao(self):
        calculador2 = Calculadora()
        self.assertEqual(calculador2.calcular(6,2, 'multiplicacao'), 12)

    def test_divisao(self):
        calculadorD = Calculadora()
        self.assertEqual(calculadorD.calcular(6,2, 'divisao'), 3)

    def test_subtracao(self):
        calculador3 = Calculadora()
        result = calculador3.calcular(6,2, 'subtracao')
        print(result)
        self.assertEqual(result, 4)

    def test_subtracao(self):
        calculadorS = Calculadora()
        self.assertEqual(calculadorS.calcular(6,2, 'subtrair'), 0)

calculador = Calculadora()
x = calculador.calcular(6, 2, 'soma')
print(x)

if __name__ == '__main__':

    main()


