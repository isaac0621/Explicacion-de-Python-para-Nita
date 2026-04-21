# 📝 Examen 1 – Solución completa

# Acumuladores
total_general = 0
cantidad_ventas = 0

while True:
    print("\n--- Nueva venta ---")

    # Entrada de datos
    precio = float(input("Ingrese el precio: "))
    cantidad = int(input("Ingrese la cantidad: "))

    # Validación
    if precio < 0 or cantidad < 0:
        print("❌ Datos inválidos, no se permiten negativos")
        continue  # vuelve a pedir datos

    # Cálculo
    total_venta = precio * cantidad

    # Acumuladores
    total_general += total_venta
    cantidad_ventas += 1

    # Clasificación
    if total_venta > 5000:
        print("💰 Venta alta:", total_venta)
    else:
        print("🧾 Venta normal:", total_venta)

    # Control de salida
    seguir = input("¿Desea continuar? (si/no): ").lower()

    if seguir == "no":
        break

# Evitar división por cero
if cantidad_ventas > 0:
    promedio = total_general / cantidad_ventas
else:
    promedio = 0

# Resultado final
print("\n📊 --- Resumen ---")
print("Total acumulado:", total_general)
print("Cantidad de ventas:", cantidad_ventas)
print("Promedio:", promedio)
