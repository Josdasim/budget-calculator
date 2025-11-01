from decimal import Decimal
from datetime import datetime
from uuid6 import uuid7
from typing import List, Optional, Dict

from src.budget_calculator.models import Transaction, TransactionType



class Budget:
    """Representa el presupuesto personal"""

    def __init__(self, name:str):
        """Inicializa el presupuesto"""

        self.budget_id = str(uuid7())
        self.name = name
        self.created_at = datetime.now()
        self.transactions = []


    def add_transaction(self, transaction:Transaction)-> None:
        """
        Permite agregar una nueva transaccion al presupuesto

        Args:
            transaction: Transaccion a registrar
        """

        self.transactions.append(transaction)


    def get_all_transactions(self)-> List[Transaction]:
        """
        Obtiene todas las transacciones registradas en el presupuesto

        Returns:
            List[Transaction]: Lista de todas las transacciones
        """
        return self.transactions.copy()
    
    
    def get_incomes(self)-> List[Transaction]:
        """
        Obtiene todas las transacciones de tipo 'ingreso'

        Returns:
            List[Transaction]: Lista de todas las transacciones de ingresos
        """

        return [transaccion for transaccion in self.transactions if transaccion.transaction_type==TransactionType.INCOME]
    

    def get_expenses(self)-> List[Transaction]:
        """
        Obtiene todas las transacciones de tipo 'gasto'

        Returns:
            List[Transaction]: Lista de todas las transacciones de gastos
        """

        return [transaccion for transaccion in self.transactions if transaccion.transaction_type==TransactionType.EXPENSE]
    

    def calculate_incomes(self)-> Decimal:
        """
        Calcula el total de ingresos

        Returns:
            Decimal: Suma de todos los ingresos
        """

        total_incomes = 0
        all_incomes = self.get_incomes()
        print(len(all_incomes))
        for transaction in all_incomes:
            total_incomes += transaction.amount

        return Decimal(str(total_incomes))
    

    def calculate_expenses(self)-> Decimal:
        """
        Calcula el total de gastos

        Returns:
            Decimal: Suma de todos los gastos
        """

        total_expenses = 0
        all_expenses = self.get_expenses()
        print(len(all_expenses))
        for transaction in all_expenses:
            total_expenses += transaction.amount

        return Decimal(str(total_expenses))
    

    def calculate_balance(self)-> Decimal:
        """
        Calcula el total de ingresos

        Returns:
            Decimal: Suma de todos los ingresos
        """

        total_incomes = self.calculate_incomes()
        total_expenses = self.calculate_expenses()

        return (total_incomes - total_expenses)

    


    
