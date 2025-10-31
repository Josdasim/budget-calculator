from decimal import Decimal
from typing import Union, Optional
from datetime import datetime
from uuid6 import uuid7
from src.budget_calculator.models.transaction_type import TransactionType

class Transaction():
    """Representa una transaccion financiera (ingreso o gasto)"""
    
    
    def __init__(self, transaction_type:Union[TransactionType,str], description:str, amount:float, category:str, transaction_id: Optional[str] = None, create_at: Optional[datetime] = None):
        self._validate_transaction_type(transaction_type.lower().strip())
        self._validate_amount(amount)
        self.transaction_id = transaction_id or str(uuid7())
        self.transaction_type = transaction_type.lower().strip()
        self.description = description.strip()
        self.amount = Decimal(str(amount))
        self.category = category.strip()
        self.create_at = create_at or datetime.now()
    

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
        
    def to_dict(self) -> dict:
        """
        Convierte la transaccion a un diccionario para serializacion

        Returns:
            dict: Diccionario con todos los atributos de la transaccion
        """

        return {
            "transaction_id": self.transaction_id,
            "transaction_type": self.transaction_type,
            "description": self.description,
            "amount": float(self.amount),
            "category": self.category,
            "create_at": self.create_at.isoformat()
        }
    
    def from_dict(cls, data:dict) -> 'Transaction':
        """
        Crea una transaccion desde un diccionario.

        Args:
            data: Diccionario con los datos de la transaccion

        Returns:
            Transaction: Nueva instancia de Transaction
        """

        return cls(
            transaction_id = data["transaction_id"],
            transaction_type = data["transaction_type"],
            description = data["description"],
            amount = data["amount"],
            category = data["category"],
            create_at = datetime.fromisoformat(data["create_at"])
        )
    
    def __repr__(self)-> str:
        """
        Representacion string del objeto transaccion para debugging.

        Returns: 
            str: Representacion de la transaccion
        """
        return (
            f"Transaction(transaction_id = ${self.transaction_id[:8]}, \n"
            f"transaction_type = ${self.transaction_type}, \n"
            f"description = ${self.description}, \n"
            f"amount = ${self.amount}, \n"
            f"category = ${self.category}, \n"
            f"create_at = ${self.create_at}"
        )