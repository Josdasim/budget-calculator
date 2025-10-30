from decimal import Decimal
from typing import Union
from datetime import datetime
from uuid6 import uuid7
from src.budget_calculator.models.transaction_type import TransactionType

class Transaction():
    """Representa una transaccion financiera (ingreso o gasto)"""
    
    
    def __init__(self, transaction_type:Union[TransactionType,str], description:str, amount:float, category:str):
        self._validate_transaction_type(transaction_type.lower().strip())
        self._validate_amount(amount)
        self.transaction_id = str(uuid7())
        self.transaction_type = transaction_type.lower().strip()
        self.description = description.strip()
        self.amount = Decimal(str(amount))
        self.category = category.strip()
        self.create_at = datetime.now()
    

    def _validate_amount(self, amount:float) -> None:
        """Confirma que se ingresa un monto valido

            Args: 
                amount: Monto de la transaccion (debe ser mayor a Cero (0))

            Raises: 
                ValueError: Si el monto es menor o igual a cero, si es un tipo invalido o vacio
        """
        #Crear Excepciones y mensajes personalizados
        if amount <= 0:
            raise ValueError("Valor no valido, debe ingresar un valor mayor a cero")
        elif not amount:
            raise ValueError("El campo no puede estar vacio")
        

    def _validate_transaction_type(self, transaction_type:str) -> None:
        """Confirma que se ingresa un tipo de transaccion valido

            Args: 
                transaction_type: Tipo de transaccion (debe ser 'ingreso' o 'gasto')

            Raises: 
                ValueError: Si campo tipo de transaccion es vacio
                TypeError: Si el tipo de transaccion es diferente a 'ingreso' o 'gasto'
        """
        #Crear Excepciones y mensajes personalizados
        if not transaction_type:
            raise ValueError("Campo no puede estar vacio")
        elif transaction_type not in TransactionType.list():
            raise TypeError("Tipo de transaccion no valida")