## HU-001: Registrar un Ingreso
**Como** usuario,  
**Quiero** poder registrar mis ingresos,  
**Para** tener control de cuánto dinero entra.

### ✅ Criterios de Aceptación
- [ ] Puedo ingresar una descripción (Ej: “Salario de noviembre”).
- [ ] Puedo ingresar un monto positivo (Ej: 15000).
- [ ] Puedo especificar una categoría (Ej: “Salario”, “Freelance”).
- [ ] El sistema registra la fecha automáticamente.
- [ ] El registro se guarda y persiste entre sesiones.

---

## HU-002: Registrar un Gasto
**Como** usuario,  
**Quiero** poder registrar mis gastos diarios,  
**Para** saber en qué estoy gastando mi dinero.

### ✅ Criterios de Aceptación
- [ ] Puedo ingresar una descripción (Ej: “Compra en supermercado”).
- [ ] Puedo ingresar un monto positivo (Ej: 10000).
- [ ] Puedo especificar una categoría (Ej: “Comida”, “Transporte”).
- [ ] El sistema registra la fecha automáticamente.
- [ ] El registro se guarda y persiste entre sesiones.

---

## HU-003: Ver Balance Actual
**Como** usuario,  
**Quiero** ver mi balance actual (Ingresos - Gastos),  
**Para** saber cuánto dinero me queda disponible.

### ✅ Criterios de Aceptación
- [ ] El sistema muestra: Total de Ingresos, Total de Gastos y Balance.
- [ ] El balance se calcula correctamente (Ingresos - Gastos).
- [ ] Se muestra en formato monetario legible.

---

## HU-004: Ver Historial de Transacciones
**Como** usuario,  
**Quiero** ver todas mis transacciones (ingresos y gastos),  
**Para** revisar mi historial financiero.

### ✅ Criterios de Aceptación
- [ ] Veo todas las transacciones ordenadas por fecha (la más reciente primero).
- [ ] Cada transacción muestra: fecha, tipo, descripción, categoría, monto.
- [ ] Puedo distinguir visualmente ingresos (+) de gastos (-).

---

## HU-005: Ver Resumen por Categoría
**Como** usuario,  
**Quiero** ver un resumen agrupado por categoría,  
**Para** identificar en qué estoy gastando más.

### ✅ Criterios de Aceptación
- [ ] Veo un resumen agrupado por categoría.
- [ ] Cada categoría muestra el total ingresado/gastado.
- [ ] Las categorías están ordenadas de mayor a menor monto.

---

## HU-006: Eliminar una Transacción
**Como** usuario,  
**Quiero** poder eliminar una transacción que registré por error,  
**Para** mantener mis datos correctos.

### ✅ Criterios de Aceptación
- [ ] Puedo seleccionar una transacción de la lista.
- [ ] El sistema me pide confirmación antes de eliminar.
- [ ] La transacción se elimina permanentemente.
- [ ] El balance se actualiza automáticamente.

---

## HU-007: Modificar una Transacción
***Como*** usuario,  
***Quiero*** poder editar una transacción existente,  
**Para*** corregir errores sin tener que borrarla y crear una nueva.

### ✅ Criterios de Aceptación
- [ ] Puedo seleccionar una transacción de la lista.
- [ ] Puedo modificar: descripción, monto, categoría.
- [ ] No puedo cambiar el tipo (ingreso ↔ gasto).
- [ ] Los cambios se guardan y el balance se recalcula automáticamente.

---

## 🧭 Orden de Prioridad (Implementación)
1. **HU-001**, **HU-002** → Funcionalidad básica  
2. **HU-003** → Valor inmediato  
3. **HU-004** → Transparencia  
4. **HU-006** → Corrección de errores  
5. **HU-007** → Edición conveniente  
6. **HU-005** → Análisis