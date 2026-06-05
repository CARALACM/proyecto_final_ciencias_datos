import time
from faker import Faker

# Registrar tiempo de inicio
inicio = time.perf_counter()

# Inicializas Faker configurando la localización (por ejemplo, México 'es_MX' o España 'es_ES')
fake = Faker('es_MX')

# Generas una lista con nombres y correos aleatorios
cantidad = 1000000
nombres_falsos = [fake.name() for _ in range(cantidad)]
correos_falsos = [fake.email() for _ in range(cantidad)]

# Registrar tiempo final
fin = time.perf_counter()

# Mostrar los primeros 5 nombres generados
print(nombres_falsos[:5])
print(correos_falsos[:5])

# Mostrar el tiempo requerido para la generación
print(f"Tiempo de ejecución: {fin - inicio:.4f} segundos")