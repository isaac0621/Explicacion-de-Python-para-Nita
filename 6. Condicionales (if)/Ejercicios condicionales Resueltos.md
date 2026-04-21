# ✅ Ejercicios Resueltos — Condicionales en Python

---

## Ejercicio 1 — Mayor de edad

**Enunciado:** Pedile al usuario su edad y mostrá si es mayor o menor de edad.

```python
edad = int(input("Ingresá tu edad: "))
if edad >= 18:
    print("Sos mayor de edad.")
else:
    print("Sos menor de edad.")
```

**Ejemplo de ejecución:**
```
Ingresá tu edad: 20
Sos mayor de edad.
```

---

## Ejercicio 2 — Número mayor a 10

**Enunciado:** Pedile al usuario un número y mostrá si es mayor, menor o igual a `10`.

```python
numero = int(input("Ingresá un número: "))
if numero > 10:
    print("El número es mayor a 10.")
elif numero < 10:
    print("El número es menor a 10.")
else:
    print("El número es igual a 10.")
```

**Ejemplo de ejecución:**
```
Ingresá un número: 7
El número es menor a 10.
```

---

## Ejercicio 3 — Número positivo

**Enunciado:** Pedile al usuario un número y mostrá si es positivo, negativo o cero.

```python
numero = int(input("Ingresá un número: "))
if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")
```

**Ejemplo de ejecución:**
```
Ingresá un número: -5
El número es negativo.
```

---

## Ejercicio 4 — Validar contraseña

**Enunciado:** Pedile al usuario una contraseña y mostrá si es correcta. La correcta es `"python"`.

```python
contrasena = input("Ingresá la contraseña: ")
if contrasena == "python":
    print("✅ Contraseña correcta.")
else:
    print("❌ Contraseña incorrecta.")
```

**Ejemplo de ejecución:**
```
Ingresá la contraseña: hola
❌ Contraseña incorrecta.
```

---

## Ejercicio 5 — Verificar nota

**Enunciado:** Pedile al usuario una nota y mostrá si aprobó (`>= 70`) o reprobó.

```python
nota = int(input("Ingresá tu nota: "))
if nota >= 70:
    print("¡Aprobaste!")
else:
    print("Reprobaste.")
```

**Ejemplo de ejecución:**
```
Ingresá tu nota: 85
¡Aprobaste!
```

---

## Ejercicio 6 — Comparar dos números

**Enunciado:** Pedile al usuario dos números y mostrá si el primero es mayor, menor o igual al segundo.

```python
numero1 = int(input("Ingresá el primer número: "))
numero2 = int(input("Ingresá el segundo número: "))
if numero1 > numero2:
    print("El primer número es mayor.")
elif numero1 < numero2:
    print("El segundo número es mayor.")
else:
    print("Los números son iguales.")
```

**Ejemplo de ejecución:**
```
Ingresá el primer número: 8
Ingresá el segundo número: 12
El segundo número es mayor.
```

---

## Ejercicio 7 — Mostrar el mayor

**Enunciado:** Pedile al usuario dos números y mostrá cuál es el mayor, o si son iguales.

```python
numero1 = int(input("Ingresá el primer número: "))
numero2 = int(input("Ingresá el segundo número: "))
if numero1 > numero2:
    print("El mayor es:", numero1)
elif numero2 > numero1:
    print("El mayor es:", numero2)
else:
    print("Los dos números son iguales.")
```

**Ejemplo de ejecución:**
```
Ingresá el primer número: 15
Ingresá el segundo número: 9
El mayor es: 15
```

---

## Ejercicio 8 — Validar edad

**Enunciado:** Pedile al usuario su edad. Si es menor a `0` o mayor a `120`, mostrá que es inválida.

```python
edad = int(input("Ingresá tu edad: "))
if edad < 0 or edad > 120:
    print("Edad inválida.")
else:
    print("Tu edad es:", edad)
```

**Ejemplo de ejecución:**
```
Ingresá tu edad: 150
Edad inválida.
```

---

## Ejercicio 9 — Mensaje según temperatura

**Enunciado:** Pedile al usuario su temperatura corporal y mostrá si tiene fiebre, está normal o tiene hipotermia.

```python
temperatura = float(input("Ingresá tu temperatura corporal: "))
if temperatura >= 38:
    print("Tenés fiebre.")
elif temperatura >= 36:
    print("Tu temperatura es normal.")
else:
    print("Tenés hipotermia.")
```

**Ejemplo de ejecución:**
```
Ingresá tu temperatura corporal: 38.5
Tenés fiebre.
```

---

## Ejercicio 10 — Validar compra

**Enunciado:** Pedile al usuario el monto de una compra. Si supera `5000`, aplicá un 10% de descuento.

```python
monto = float(input("Ingresá el monto de la compra: "))
if monto > 5000:
    descuento = monto * 0.9
    print("Tenés descuento. Total a pagar:", descuento)
else:
    print("Total a pagar:", monto)
```

**Ejemplo de ejecución:**
```
Ingresá el monto de la compra: 6000
Tenés descuento. Total a pagar: 5400.0
```

---

> 💡 **Recordá:** Estos son solo una forma de resolver cada ejercicio. Los mensajes y valores pueden variar, lo importante es la lógica condicional.
