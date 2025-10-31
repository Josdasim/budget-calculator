import pytest
from datetime import datetime
from src.budget_calculator.models import Budget, Transaction


def test_create_budget_success():
    """Verifica que se puede crear un presupuesto vacio"""

    name_budget = "Presupuesto de Noviembre de 2025"
    budget = Budget(name = name_budget)

    assert isinstance(budget.budget_id, str)
    assert budget.name == name_budget
    assert isinstance(budget.created_at, datetime)
    assert len(budget.transactions) == 0


def test_add_transaction():
    """Comprueba que se puede agregar transacciones al presupuesto"""

    budget = Budget(name = "Presupuesto de la semana 1")
    transaction_1 = Transaction(transaction_type= "ingreso",description="T1",amount=2000,category="C1")
    budget.add_transaction(transaction_1)

    assert len(budget.transactions) == 1
    assert budget.transactions[0] == transaction_1


def test_get_all_transactions():
    """Verifica que se pueden obtener todas las transacciones registradas"""

    budget = Budget(name = "Presupuesto de la semana 1")
    transaction_1 = Transaction(transaction_type= "ingreso",description="T1",amount=2000,category="C1")
    transaction_2= Transaction(transaction_type= "ingreso",description="T3 ",amount=500,category="C3")
    transaction_3 = Transaction(transaction_type= "gasto",description="T2",amount=750,category="C2")
    budget.add_transaction(transaction_1)
    budget.add_transaction(transaction_2)
    budget.add_transaction(transaction_3)

    all_transactions = budget.get_all_transactions()
    assert len(all_transactions) == 3 

def test_get_incomes():
    """Valida que se obtenga una lista de todos los ingresos registrados"""

    budget = Budget(name = "test obtener lista de ingresos")
    transaction_1 = Transaction(transaction_type= "ingreso",description="T1",amount=2000,category="C1")
    transaction_2= Transaction(transaction_type= "ingreso",description="T3 ",amount=500,category="C3")
    transaction_3 = Transaction(transaction_type= "gasto",description="T2",amount=750,category="C2")
    budget.add_transaction(transaction_1)
    budget.add_transaction(transaction_2)
    budget.add_transaction(transaction_3)

    all_incomes = budget.get_incomes()
    
    assert len(all_incomes) == 2
    assert all_incomes[0].description == "T1"


def test_get_expenses():
    """Valida que se obtenga una lista de todos los gastos registrados"""

    budget = Budget(name="test obtener lista de gastos")
    transaction_1 = Transaction(transaction_type= "gasto",description="T1",amount=2000,category="C1")
    transaction_2= Transaction(transaction_type= "gasto",description="T2",amount=500,category="C2")
    transaction_3= Transaction(transaction_type= "ingreso",description="T2",amount=500,category="C2")
    budget.add_transaction(transaction_1)
    budget.add_transaction(transaction_2)
    budget.add_transaction(transaction_3)

    all_expenses = budget.get_expenses()
    assert len(all_expenses) == 2
    assert all_expenses[1].category == "C2" 


def test_calculate_incomes():
    """Verifica que se realiza correctamente la suma de los ingresos"""

    budget = Budget(name = "test_ingresos")
    transaction_1 = Transaction(transaction_type= "ingreso",description="T1",amount=2000,category="C1")
    transaction_2= Transaction(transaction_type= "ingreso",description="T2",amount=500,category="C2")
    transaction_3 = Transaction(transaction_type= "gasto",description="T2",amount=750,category="C2")
    budget.add_transaction(transaction_1)
    budget.add_transaction(transaction_2)
    budget.add_transaction(transaction_3)

    total_incomes = budget.calculate_incomes()    

    assert total_incomes == 2500

def test_calculate_expenses():
    """Verifica que se realiza correctamente la suma de los gastos"""

    budget = Budget(name="test_gastos")
    transaction_1 = Transaction(transaction_type= "gasto",description="T1",amount=2000,category="C1")
    transaction_2= Transaction(transaction_type= "gasto",description="T2",amount=500,category="C2")
    transaction_3= Transaction(transaction_type= "ingreso",description="T2",amount=500,category="C2")
    budget.add_transaction(transaction_1)
    budget.add_transaction(transaction_2)
    budget.add_transaction(transaction_3)

    total_expenses = budget.calculate_expenses()

    assert total_expenses == 2500

def test_calculate_negative_balance():
    """Verifica que el balance es negativo, es decir fueron mayores los gastos"""

    budget = Budget(name="balance negativo")
    transaction_1 = Transaction(transaction_type= "ingreso",description="T2",amount=200,category="C2")
    transaction_2= Transaction(transaction_type= "gasto",description="C3",amount=500,category="C3")
    budget.add_transaction(transaction_1)
    budget.add_transaction(transaction_2)

    balance = budget.calculate_balance()

    assert balance == -300

def test_calculate_positive_balance():
    """Verifica que el balance es positivo, es decir fueron mayores los ingresos"""
    
    budget = Budget(name="balance positivo")
    transaction_1 = Transaction(transaction_type= "ingreso",description="T2",amount=700,category="C2")
    transaction_2= Transaction(transaction_type= "gasto",description="C3",amount=500,category="C3")
    budget.add_transaction(transaction_1)
    budget.add_transaction(transaction_2)

    balance = budget.calculate_balance()

    assert balance == 200
