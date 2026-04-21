# 🔥 Ejercicios Resueltos — `True` en Python

---

## Ejercicio 1 — Mensaje con `if True`

**Enunciado:** Escribí un bloque `if` que siempre se ejecute e imprima un mensaje de bienvenida.

```python
if True:
    print("¡Bienvenido al programa!")
```

**Salida:**
```
¡Bienvenido al programa!
```

---

## Ejercicio 2 — Bucle que imprime una sola vez

**Enunciado:** Creá un bucle infinito que imprima `"Hola"` una única vez y luego se detenga.

```python
while True:
    print("Hola")
    break
```

**Salida:**
```
Hola
```

---

## Ejercicio 3 — Bucle con palabra de salida

**Enunciado:** Pedile texto al usuario repetidamente. Cuando escriba `"fin"`, el programa debe terminar.

```python
while True:
    texto = input("Escribí algo (o 'fin' para terminar): ")
    if texto == "fin":
        print("¡Hasta luego!")
        break
    print("Ingresaste:", texto)
```

**Ejemplo de ejecución:**
```
Escribí algo (o 'fin' para terminar): hola
Ingresaste: hola
Escribí algo (o 'fin' para terminar): python
Ingresaste: python
Escribí algo (o 'fin' para terminar): fin
¡Hasta luego!
```

---

## Ejercicio 4 — Números hasta el cero

**Enunciado:** Pedí números al usuario uno por uno. Cuando ingrese `0`, el programa debe detenerse.

```python
while True:
    numero = int(input("Ingresá un número (0 para salir): "))
    if numero == 0:
        print("Saliendo...")
        break
    print("Número ingresado:", numero)
```

**Ejemplo de ejecución:**
```
Ingresá un número (0 para salir): 5
Número ingresado: 5
Ingresá un número (0 para salir): 12
Número ingresado: 12
Ingresá un número (0 para salir): 0
Saliendo...
```

---

## Ejercicio 5 — Menú repetible

**Enunciado:** Mostrá un menú con opciones numeradas. El menú debe volver a aparecer después de cada elección hasta que el usuario elija la opción de salir.

```python
while True:
    print("\n--- MENÚ ---")
    print("1. Saludar")
    print("2. Mostrar la fecha")
    print("3. Salir")

    opcion = input("Elegí una opción: ")

    if opcion == "1":
        print("¡Hola!")
    elif opcion == "2":
        print("Hoy es un gran día para aprender Python.")
    elif opcion == "3":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida, intentá de nuevo.")
```

**Ejemplo de ejecución:**
```
--- MENÚ ---
1. Saludar
2. Mostrar la fecha
3. Salir
Elegí una opción: 1
¡Hola!

--- MENÚ ---
1. Saludar
2. Mostrar la fecha
3. Salir
Elegí una opción: 3
¡Hasta luego!
```

---

## Ejercicio 6 — Nombre obligatorio

**Enunciado:** Pedí el nombre del usuario. Si deja el campo vacío, volvé a pedirlo hasta que escriba algo.

```python
while True:
    nombre = input("Ingresá tu nombre: ")
    if nombre:
        print("Hola,", nombre)
        break
    print("El nombre no puede estar vacío. Intentá de nuevo.")
```

**Ejemplo de ejecución:**
```
Ingresá tu nombre: 
El nombre no puede estar vacío. Intentá de nuevo.
Ingresá tu nombre: 
El nombre no puede estar vacío. Intentá de nuevo.
Ingresá tu nombre: Ana
Hola, Ana
```

---

## Ejercicio 7 — Edad válida

**Enunciado:** Pedí la edad del usuario. Si ingresa `0` o un número negativo, volvé a pedirla hasta obtener un valor mayor a `0`.

```python
while True:
    edad = int(input("Ingresá tu edad: "))
    if edad > 0:
        print("Tu edad es:", edad)
        break
    print("La edad debe ser mayor a 0. Intentá de nuevo.")
```

**Ejemplo de ejecución:**
```
Ingresá tu edad: -3
La edad debe ser mayor a 0. Intentá de nuevo.
Ingresá tu edad: 0
La edad debe ser mayor a 0. Intentá de nuevo.
Ingresá tu edad: 25
Tu edad es: 25
```

---

## Ejercicio 8 — Repetidor de mensajes

**Enunciado:** Pedí un mensaje al usuario e imprimilo. Repetí esto hasta que el usuario escriba `"no"`.

```python
while True:
    mensaje = input("Escribí un mensaje: ")
    print("Tu mensaje:", mensaje)
    continuar = input("¿Querés escribir otro? (no para salir): ")
    if continuar == "no":
        print("¡Listo!")
        break
```

**Ejemplo de ejecución:**
```
Escribí un mensaje: Python es genial
Tu mensaje: Python es genial
¿Querés escribir otro? (no para salir): sí
Escribí un mensaje: Me gusta programar
Tu mensaje: Me gusta programar
¿Querés escribir otro? (no para salir): no
¡Listo!
```

---

## Ejercicio 9 — Sistema de login

**Enunciado:** Simulá un login. Pedí la contraseña hasta que el usuario ingrese la correcta (`"python123"`). Al lograrse, mostrá un mensaje de acceso concedido.

```python
contrasena_correcta = "python123"

while True:
    intento = input("Ingresá la contraseña: ")
    if intento == contrasena_correcta:
        print("✅ Acceso concedido. ¡Bienvenido!")
        break
    print("❌ Contraseña incorrecta. Intentá de nuevo.")
```

**Ejemplo de ejecución:**
```
Ingresá la contraseña: hola
❌ Contraseña incorrecta. Intentá de nuevo.
Ingresá la contraseña: 1234
❌ Contraseña incorrecta. Intentá de nuevo.
Ingresá la contraseña: python123
✅ Acceso concedido. ¡Bienvenido!
```

---

## Ejercicio 10 — Suma acumulada

**Enunciado:** Pedí números al usuario y sumalos. Cuando escriba `"stop"`, mostrá el total acumulado y terminá el programa.

```python
total = 0

while True:
    entrada = input("Ingresá un número (o 'stop' para terminar): ")
    if entrada == "stop":
        print("Total acumulado:", total)
        break
    total = total + int(entrada)
    print("Total hasta ahora:", total)
```

**Ejemplo de ejecución:**
```
Ingresá un número (o 'stop' para terminar): 10
Total hasta ahora: 10
Ingresá un número (o 'stop' para terminar): 25
Total hasta ahora: 35
Ingresá un número (o 'stop' para terminar): 5
Total hasta ahora: 40
Ingresá un número (o 'stop' para terminar): stop
Total acumulado: 40
```

---

> 💡 **Recordá:** Estos son solo una forma de resolver cada ejercicio. Puede haber otras soluciones igualmente válidas.
