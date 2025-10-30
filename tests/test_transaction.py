"""
Tests para la clase Transaction.
"""


import pytest
from decimal import Decimal
from src.budget_calculator.models.transaction import Transaction


# =========================================
#            TESTS DE CREACION            #
# =========================================

def test_create_transaction_income_success():
    """Verifica que se puede crear un ingreso valido"""
    transaction_type = "ingreso"
    description = "Proyecto web"
    amount = Decimal("500000")
    category = "Paypal"

    transaction = Transaction(transaction_type,description,amount,category)

    assert transaction.transaction_type == "ingreso"
    assert transaction.description == "Proyecto web"
    assert transaction.amount == Decimal("500000")
    assert transaction.category == "Paypal"
    assert isinstance(transaction, Transaction)
    assert transaction.transaction_id is not None
    assert transaction.create_at is not None

def test_create_transaction_expense_success():
    """Verifica que se puede crear un gasto valido"""
    transaction_type = "gasto"
    description = "Mercado"
    amount = Decimal("150000")
    category = "Comida"

    transaction = Transaction(transaction_type,description,amount,category)

    assert transaction.transaction_type == "gasto"
    assert transaction.description == "Mercado"
    assert transaction.amount == Decimal("150000")
    assert transaction.category == "Comida"
    assert isinstance(transaction, Transaction)
    assert transaction.transaction_id is not None
    assert transaction.create_at is not None

def test_create_transaction_with_negative_amount():
    """verificar que no se puede crear una transaccion con monto negativo"""
    transaction_type = "ingreso"
    description = "Proyecto web"
    amount = Decimal("-500000")
    category = "Paypal"

    with pytest.raises(ValueError):
        transaction = Transaction(transaction_type,description,amount,category)

def test_create_transaction_invalid_type():
    """Verifica que no se puede crear una transaccion con tipo invalido"""
    transaction_type = "compra"
    description = "random"
    amount = Decimal("5000")
    category = "Varios"

    with pytest.raises(TypeError):
        transaction = Transaction(transaction_type,description,amount,category)

def test_create_transaction_with_amount_zero():
    """verificar que no se puede crear una transaccion con monto cero"""
    transaction_type = "ingreso"
    description = "Transaccion invalida"
    amount = Decimal("0")
    category = "Varios"

    with pytest.raises(ValueError):
        transaction = Transaction(transaction_type,description,amount,category)