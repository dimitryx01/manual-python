# DATOS INICIALES ---
CATALOGO = {
    "A001": {"nombre": "Teclado Mecánico", "precio": 49.99, "stock": 10, "peso_kg": 0.9},
    "A002": {"nombre": "Ratón Gaming", "precio": 25.50, "stock": 5, "peso_kg": 0.2},
    "A003": {"nombre": "Monitor 24", "precio": 149.00, "stock": 3, "peso_kg": 3.5},
    "A004": {"nombre": "Auriculares", "precio": 35.99, "stock": 0, "peso_kg": 0.4},
    "A005": {"nombre": "Webcam HD", "precio": 39.90, "stock": 7, "peso_kg": 0.3},
}

CODIGOS_PROMO = {
    "ENVIOFREE": {"tipo": "envio", "descuento": 1.0},
    "DESC10": {"tipo": "total", "descuento": 0.10},
}

# FUNCIONES ---

def mostrar_catalogo(catalogo):
    print("\nCATÁLOGO DE PRODUCTOS ---")
    for cod, info in catalogo.items():
        print(f"Código: {cod} | {info['nombre']} | Precio: {info['precio']}€ | Stock: {info['stock']}")

def validar_codigo_producto(catalogo, codigo):
    # Usamos for-else como pide la profe
    for cod in catalogo:
        if cod == codigo:
            return True
    else:
        # Si el bucle termina y no encontró el código, entra aquí
        return False

def agregar_al_carrito(carrito, catalogo, codigo, cantidad):
    if not validar_codigo_producto(catalogo, codigo):
        print("Error: Ese código no existe.")
        return
    
    if catalogo[codigo]["stock"] < cantidad:
        print("Error: No hay suficiente stock.")
        return

    # Si ya está en el carrito, sumamos la cantidad, si no, lo creamos
    if codigo in carrito:
        carrito[codigo] += cantidad
    else:
        carrito[codigo] = cantidad
    print(f"¡{catalogo[codigo]['nombre']} añadido!")

def calcular_totales(carrito, catalogo, iva=0.21):
    subtotal = 0
    peso_total = 0
    for cod, cant in carrito.items():
        subtotal += catalogo[cod]["precio"] * cant
        peso_total += catalogo[cod]["peso_kg"] * cant
    
    total_iva = subtotal * iva
    return {"subtotal": subtotal, "iva": total_iva, "total": subtotal + total_iva, "peso": peso_total}

def calcular_envio(peso_total, zona="PENINSULA"):
    # Un cálculo simple: 2 euros por kilo
    coste = peso_total * 2
    if zona != "PENINSULA":
        coste += 10 # Suplemento fuera de península
    return coste

def aplicar_promos(total, envio, *codigos):
    # *codigos recibe todos los que escribas
    for c in codigos:
        if c in CODIGOS_PROMO:
            promo = CODIGOS_PROMO[c]
            if promo["tipo"] == "envio":
                envio -= envio * promo["descuento"]
            elif promo["tipo"] == "total":
                total -= total * promo["descuento"]
    return total, envio

# PROGRAMA PRINCIPAL ---

def main():
    carrito = {}
    historial_pedidos = [] # Para el informe final

    while True:
        print("\n--- MINI AMAZON MENU ---")
        print("1. Ver catálogo")
        print("2. Añadir producto al carrito")
        print("3. Quitar producto del carrito")
        print("4. Ver carrito")
        print("5. Confirmar pedido")
        print("0. Salir")
        
        opcion = input("Elige una opción: ")

        if opcion == "1":
            mostrar_catalogo(CATALOGO)
        
        elif opcion == "2":
            cod = input("Introduce código del producto: ").upper()
            cant = int(input("¿Cuántos quieres?: "))
            agregar_al_carrito(carrito, CATALOGO, cod, cant)

        elif opcion == "3":
            cod = input("Código a quitar: ").upper()
            if cod in carrito:
                del carrito[cod]
                print("Producto eliminado.")
            else:
                print("No está en el carrito.")

        elif opcion == "4":
            print("\nTu carrito actual:", carrito)

        elif opcion == "5":
            if not carrito:
                print("El carrito está vacío.")
                continue
            
            resumen = calcular_totales(carrito, CATALOGO)
            envio = calcular_envio(resumen["peso"])
            
            print(f"Subtotal: {resumen['total']:.2f}€ | Envio: {envio:.2f}€")
            
            promo = input("¿Tienes código promo? (Sino pulsa Enter): ").upper()
            total_final, envio_final = aplicar_promos(resumen["total"], envio, promo)
            
            print(f"TOTAL A PAGAR: {total_final + envio_final:.2f}€")
            
            confirmar = input("¿Confirmar pedido? (si/no): ").lower()
            if confirmar == "si":
                # Descontar stock
                for cod, cant in carrito.items():
                    CATALOGO[cod]["stock"] -= cant
                historial_pedidos.append("CONFIRMADO")
                carrito = {} # Limpiar carrito
                print("¡Pedido realizado con éxito!")
            else:
                historial_pedidos.append("CANCELADO")
                print("Pedido cancelado.")

        elif opcion == "0":
            # Uso de while-else: se ejecuta al salir normalmente
            break
        else:
            print("Opción no válida.")
    
    else:
        # Este else pertenece al while (se ejecuta si no hubo un break, 
        # pero como usamos break para salir, es solo para cumplir el requisito)
        print("Cerrando sistema...")

  
    print("\n--- INFORME FINAL ---")
    confirmados = historial_pedidos.count("CONFIRMADO")
    cancelados = historial_pedidos.count("CANCELADO")
    print(f"Pedidos Confirmados: {confirmados} | Cancelados: {cancelados}")

    # For-else para ventas
    for p in historial_pedidos:
        if p == "CONFIRMADO":
            print("Hubo ventas en esta sesión.")
            break
    else:
        print("No hubo ventas hoy.")

if __name__ == "__main__":
    main()