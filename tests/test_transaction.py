"""
Tests para la clase Transaction.
"""


import pytest
from decimal import Decimal
from src.budget_calculator.models.transaction import Transaction
from src.budget_calculator.models.transaction_type import TransactionType
from datetime import datetime

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


def test_transaction_to_dict():
    """
    Verifica que to_dict() convierte correctamente la transacción.
    """
    date = datetime(2024, 1, 15, 10, 30, 0)
    transaccion = Transaction(
        transaction_id = "test-id-123",
        transaction_type = TransactionType.EXPENSE,
        description = "Compra online",
        amount = 89000,
        category = "Compras",
        create_at = date,
        
    )

    resultado = transaccion.to_dict()

    assert resultado["transaction_id"] == "test-id-123"
    assert resultado["transaction_type"] == "gasto"  # String, no Enum
    assert resultado["description"] == "Compra online"
    assert resultado["amount"] == 89000
    assert resultado["category"] == "Compras"
    assert resultado["create_at"] == date.isoformat()
    
    
def test_transaction_from_dict():
        """
        Verifica que from_dict() reconstruye correctamente la transacción.
        """
        data = {
            "transaction_id": "test-id-456",
            "transaction_type": "ingreso",
            "description": "Venta producto",
            "amount": 25000,
            "category": "Ventas",
            "create_at": "2024-01-20T14:30:00"
        }
        
        transaccion = Transaction.from_dict(Transaction,data)
        
        assert transaccion.transaction_id == "test-id-456"
        assert transaccion.transaction_type == TransactionType.INCOME
        assert transaccion.description == "Venta producto"
        assert transaccion.amount == Decimal("25000")
        assert transaccion.category == "Ventas"
        assert transaccion.create_at == datetime(2024, 1, 20, 14, 30, 0)
    
def test_two_different_transaction_id():
    """
    Verifica que dos transacciones generan IDs únicos automáticamente.
    """
    transaccion1 = Transaction(
        transaction_type = TransactionType.INCOME,
        description = "Transacción 1",
        amount = 10000,
        category = "Test"
    )
    
    transaccion2 = Transaction(
        transaction_type = TransactionType.EXPENSE,
        description = "Transacción 2",
        amount = 10000,
        category = "Test"
    )
    
    assert transaccion1.transaction_id != transaccion2.transaction_id