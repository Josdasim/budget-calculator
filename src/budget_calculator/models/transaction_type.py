from enum import Enum


class TransactionType(str, Enum):
    """Enumeracion de tipos de transacciones financieras
    Atributos: 
        INCOME: Representa una entrada de dinero
        EXPENSE: Representa una salida de dinero
    """
    INCOME = "ingreso"
    EXPENSE = "gasto"

    @classmethod
    def list(cls):
        return [transaction_type.value for transaction_type in cls]

