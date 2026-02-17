class ProcesadorPago:
    def __init__(self, numero_tarjeta, cvv):
        # Atributos PRIVADOS (doble guion bajo __)
        # NO se pueden acceder directamente desde fuera de la clase
        self.__numero_tarjeta = numero_tarjeta  # PRIVADO: Protege el número completo
        self.__cvv = cvv  # PRIVADO: Protege el código de seguridad
        self.__saldo_disponible = 5000  # PRIVADO: Evita manipulación del saldo
        
    # Método PÚBLICO (sin guiones bajos)
    # Puede ser llamado desde fuera de la clase
    def procesar_pago(self, monto):
        """Método público para procesar pagos de forma segura"""
        
        # 1. Validar CVV usando método privado
        if not self.__validar_cvv():  # Llama a método PRIVADO
            return "❌ CVV inválido"
        
        # 2. Verificar saldo (accede a atributo PRIVADO internamente)
        if monto > self.__saldo_disponible:
            return "❌ Saldo insuficiente"
        
        # 3. Procesar pago (modifica atributo PRIVADO de forma controlada)
        self.__saldo_disponible -= monto
        return f"✅ Pago aprobado: {monto}€"
    
    # Método PRIVADO (doble guion bajo __)
    # Solo puede ser llamado DENTRO de la clase
    def __validar_cvv(self):
        """Método privado - Validación interna de seguridad"""
        return len(self.__cvv) == 3
    
    # Método PÚBLICO
    # Proporciona acceso controlado a datos sensibles
    def ver_tarjeta(self):
        """Solo muestra últimos 4 dígitos (enmascarado)"""
        return f"**** **** **** {self.__numero_tarjeta[-4:]}"
    
    
    
       
    # 1. Cliente ingresa datos (se guardan como PRIVADOS)
pago = ProcesadorPago("4532123456789012", "123")

# 2. Mostrar tarjeta enmascarada (método PÚBLICO)
print(f"Accediendo a metodo publico --> Tarjeta: {pago.ver_tarjeta()}")  # ✅ Funciona

# 3. Procesar pagos (método PÚBLICO)
print("Pagando con 150 --> "+pago.procesar_pago(150))  # ✅ Pago aprobado: 150€
print("Pagando con 6000 --> "+pago.procesar_pago(6000)) # ❌ Saldo insuficiente




# ❌ Intento de acceder al número completo (FALLA)
# Los atributos con __ NO son accesibles desde fuera
try:
    print(pago.__numero_tarjeta)  # Intento de acceso directo
except AttributeError:
    print("Accediendo al numero de tarjeta --> ❌ Número de tarjeta protegido (atributo PRIVADO)")

# ❌ Intento de acceder al CVV (FALLA)
try:
    print(pago.__cvv)  # Intento de acceso directo
except AttributeError:
    print("accediendo al CVV --> ❌ CVV protegido (atributo PRIVADO)")

# ❌ Intento de modificar saldo directamente (NO AFECTA el saldo real)
# Esto crea un NUEVO atributo, pero NO modifica el PRIVADO
pago.__saldo_disponible = 999999  # Parece que funciona, pero NO
print(pago.procesar_pago(100))  # ✅ Sigue usando el saldo PRIVADO real (4850€)

# ❌ Intento de llamar método privado (FALLA)
try:
    pago.__validar_cvv()  # Los métodos __ tampoco son accesibles
except AttributeError:
    print("Accediendo al Metodo privado --> ❌ Método de validación protegido (método PRIVADO)")