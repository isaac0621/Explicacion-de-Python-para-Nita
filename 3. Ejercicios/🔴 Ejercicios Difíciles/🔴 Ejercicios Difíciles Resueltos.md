# 🔴 20 Ejercicios Difíciles – Python (Resueltos)

---

## 1. ➕ Suma hasta 0

```python
total = 0

while True:
    num = int(input("Número: "))
    if num == 0:
        break
    total += num

print("Total:", total)
```

---

## 2. 🔢 Contador de números

```python
contador = 0

while True:
    num = int(input("Número (0 para salir): "))
    if num == 0:
        break
    contador += 1

print("Cantidad:", contador)
```

---

## 3. 💰 Total de precios

```python
total = 0

while True:
    precio = float(input("Precio (0 para salir): "))
    if precio == 0:
        break
    total += precio

print("Total:", total)
```

---

## 4. 🛒 Caja registradora

```python
total = 0

while True:
    precio = float(input("Precio: "))
    total += precio

    seguir = input("¿Seguir? (si/no): ")
    if seguir == "no":
        break

print("Total:", total)
```

---

## 5. 🎂 Validar edad

```python
while True:
    edad = int(input("Edad: "))
    if edad > 0:
        break

print("Edad válida")
```

---

## 6. 🔁 Contar hasta N

```python
n = int(input("Número: "))
i = 1

while i <= n:
    print(i)
    i += 1
```

---

## 7. 📊 Tabla del 5

```python
i = 1

while i <= 10:
    print(5 * i)
    i += 1
```

---

## 8. ⏳ Cuenta regresiva

```python
i = 10

while i >= 1:
    print(i)
    i -= 1
```

---

## 9. 📈 Número mayor

```python
mayor = None

while True:
    num = int(input("Número (0 para salir): "))
    if num == 0:
        break
    if mayor is None or num > mayor:
        mayor = num

print("Mayor:", mayor)
```

---

## 10. 📉 Número menor

```python
menor = None

while True:
    num = int(input("Número (0 para salir): "))
    if num == 0:
        break
    if menor is None or num < menor:
        menor = num

print("Menor:", menor)
```

---

## 11. 📊 Promedio

```python
total = 0
contador = 0

while True:
    num = int(input("Número (0 para salir): "))
    if num == 0:
        break
    total += num
    contador += 1

print("Promedio:", total / contador)
```

---

## 12. 🔐 Login simple

```python
intentos = 3

while intentos > 0:
    clave = input("Clave: ")

    if clave == "1234":
        print("Acceso correcto")
        break

    intentos -= 1

print("Fin")
```

---

## 13. 💵 Meta de ahorro

```python
total = 0
meta = 1000

while total < meta:
    ahorro = float(input("Aporte: "))
    total += ahorro

print("Meta alcanzada")
```

---

## 14. 🛍️ Productos hasta "no"

```python
total = 0

while True:
    precio = float(input("Precio: "))
    total += precio

    seguir = input("¿Seguir? (si/no): ")
    if seguir == "no":
        break

print("Total:", total)
```

---

## 15. ✅ Validación de entrada

```python
while True:
    num = input("Número: ")
    if num.isdigit():
        break

print("Número válido")
```

---

## 16. 🔢 Contar pares

```python
contador = 0

while True:
    num = int(input("Número (0 salir): "))
    if num == 0:
        break
    if num % 2 == 0:
        contador += 1

print("Pares:", contador)
```

---

## 17. ➕ Sumar > 10

```python
total = 0

while True:
    num = int(input("Número (0 salir): "))
    if num == 0:
        break
    if num > 10:
        total += num

print("Total:", total)
```

---

## 18. 💸 Presupuesto

```python
total = 0
limite = 5000

while True:
    precio = float(input("Precio: "))

    if total + precio > limite:
        print("Límite superado")
        break

    total += precio

print("Total:", total)
```

---

## 19. 📋 Menú interactivo

```python
while True:
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Salir")

    op = input("Elegí: ")

    if op == "3":
        break
```

---

## 20. 🛒 Carrito completo

```python
total = 0

while True:
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))

    total += precio * cantidad

    if total > 5000:
        print("Cuidado: superando presupuesto")

    seguir = input("¿Seguir? (si/no): ")
    if seguir == "no":
```
