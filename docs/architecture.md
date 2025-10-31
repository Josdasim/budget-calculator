# 🏗️ Diseño de Arquitectura

## Visión General
Arquitectura de 3 capas basada en los principios de **Arquitectura Limpia (Clean Architecture)**.

## Capa 1: Presentación (CLI)
**Responsabilidad:** Interacción con el usuario  
- Mostrar menús  
- Capturar entradas del usuario  
- Formatear la salida  
- Manejar errores del usuario  

**Archivos:** cli.py

## Capa 2: Lógica de Negocio (Modelos)
**Responsabilidad:** Lógica central del dominio  
- Validación de transacciones  
- Cálculo de presupuesto  
- Aplicación de reglas de negocio  

**Archivos:**
- models/transaction.py - Entidad *Transaction*
- models/budget.py - Agregado *Budget*

### Modelo de Transacción

    Transaction:
      - transaction_id: str (UUID)
      - transaction_type: str ("ingreso" | "gasto")
      - description: str
      - amount: Decimal
      - category: str
      - create_at: datetime

### Modelo de Presupuesto

    Budget:
      - transactions: List[Transaction]
      
      Métodos:
      - add_income()                # HU-001
      - add_expense()               # HU-002
      - get_balance()               # HU-003
      - get_transactions()          # HU-004
      - get_summary_by_category()   # HU-005
      - delete_transaction()        # HU-006
      - update_transaction()        # HU-007

## Capa 3: Persistencia (Storage)
**Responsabilidad:** Almacenamiento y recuperación de datos  
- Guardar en formato JSON  
- Cargar desde JSON  
- Manejar errores de lectura/escritura de archivos  

*Archivos:*
- storage/base.py - Interfaz de almacenamiento (ABC)
- storage/json_storage.py - Implementación en JSON

## Principios de Diseño Aplicados

### SOLID
- **S**ingle Responsibility (Responsabilidad Única): Cada clase tiene una sola función.  
- **O**pen/Closed (Abierto/Cerrado): Se pueden extender funcionalidades sin modificar el código existente.  
- **L**iskov Substitution (Sustitución de Liskov): Cualquier implementación de Storage debe funcionar sin romper el sistema.  
- **I**nterface Segregation (Segregación de Interfaces): Interfaces pequeñas y específicas.  
- **D**ependency Inversion (Inversión de Dependencias): Budget depende de una interfaz, no de una implementación concreta.  

### TDD (Desarrollo Guiado por Pruebas)

- Escribir las pruebas primero  
- Ciclo *Rojo → Verde → Refactorizar*  
- Alta cobertura de pruebas (>80%)

## Flujo de Datos

Usuario → CLI → Budget → Transaction
                  ↓
                Storage → JSON


### Ejemplo: Registrar Ingreso (HU-001)
1. Usuario ingresa datos en CLI
2. CLI llama budget.add_income(desc, monto, cat)
3. Budget crea Transaction con validaciones
4. Budget agrega a self.transactions
5. Budget llama storage.save(transactions)
6. Storage serializa a JSON