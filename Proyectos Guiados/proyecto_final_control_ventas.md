# 🏢 Proyecto Final – Control de Ventas (Grupo Purdy)

## 🎯 Objetivo
Simular un sistema básico de control de ventas, aplicando variables, input, conversión, condicionales y bucles.

---

## 🧾 Enunciado

La empresa **Grup-Cart** necesita un sistema simple para registrar ventas diarias.

El programa debe permitir:

- Ingresar múltiples ventas
- Calcular el total acumulado
- Aplicar validaciones básicas
- Mostrar un resumen final

---

## 📊 Contexto real

Cada venta tiene:
- Precio del producto
- Cantidad vendida

La empresa tiene una regla:
- Si una venta supera ₡5000 → marcar como “venta alta”

---

## 📌 Requisitos

### Entrada de datos
- Pedir precio del producto
- Pedir cantidad
- Calcular total por venta

### Lógica del sistema
- Acumular total general
- Contar número de ventas
- Detectar ventas mayores a ₡5000

### Control de flujo
- Repetir proceso hasta que el usuario decida salir
- Usar `while`

### Validaciones
- No permitir precios negativos
- No permitir cantidades negativas

---

## ⚙️ Reglas del negocio

- total_venta = precio * cantidad
- Si total_venta > 5000 → mostrar: "Venta alta"
- Si no → "Venta normal"

---

## 📤 Salida esperada

Al finalizar el programa mostrar:

- Total de ventas acumuladas
- Cantidad de ventas realizadas
- Promedio por venta

---

## 🧠 Pistas (sin código)

- Usar acumulador para total
- Usar contador para ventas
- Usar conversión (`float`, `int`)
- Usar `if` para validaciones
- Usar `while` para repetir

---

## 🚧 Nivel extra (opcional)

- Agregar presupuesto diario (ej: meta de ventas ₡20000)
- Mostrar si se cumplió o no la meta

---

## ✅ Criterio de éxito

- El sistema no se rompe con datos inválidos
- Calcula correctamente los totales
- Permite múltiples ventas sin errores
- Muestra un resumen claro al final
