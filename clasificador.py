import difflib
import re
import argparse

def palabras_clave_similares(texto, palabras_clave, umbral=0.7):
    palabras_texto = re.findall(r'\b\w+\b', texto.lower())
    contador = 0
    for palabra_texto in palabras_texto:
        for palabra_clave in palabras_clave:
            ratio = difflib.SequenceMatcher(None, palabra_texto, palabra_clave).ratio()
            if ratio >= umbral:
                contador += 1
                break
    return contador

def contar_iaas(texto):
    iaas_keywords = [
        'infraestructura', 'infraestructura como servicio', 'servidor virtual', 'vm', 'máquina virtual',
        'almacenamiento', 'red', 'hardware', 'computación', 'servidores físicos', 'data center',
        'infraestructura física', 'infraestructura escalable', 'recursos computacionales',
        'cpu', 'procesador', 'memoria ram', 'ram', 'disco duro', 'ssd', 'almacenamiento en bloque',
        'ancho de banda', 'tarjeta de red', 'gpu', 'firewall', 'balanceador de carga', 'ip pública', 'ip privada',
        'virtualización', 'hypervisor', 'escalado vertical', 'escalado horizontal'
    ]
    return palabras_clave_similares(texto, iaas_keywords)

def contar_paas(texto):
    paas_keywords = [
        'plataforma', 'plataforma como servicio', 'desarrollo', 'entorno', 'middleware',
        'base de datos gestionada', 'deploy', 'automatización', 'api', 'framework', 'runtime',
        'entorno de ejecución', 'integración continua', 'entrega continua', 'servicio gestionado',
        'herramientas de desarrollo', 'orquestación', 'backend como servicio',
        'python', 'java', 'node.js', 'ruby', 'php', 'dotnet', '.net', 'golang', 'scala', 'runtime environment',
        'sdk', 'paquete', 'compilación', 'contenedor', 'docker', 'kubernetes', 'microservicios', 'automatización de despliegue',
        'pipeline', 'testing automatizado', 'entorno de prueba'
    ]
    return palabras_clave_similares(texto, paas_keywords)

def contar_saas(texto):
    saas_keywords = [
        'software', 'software como servicio', 'aplicación', 'aplicaciones', 'acceso web',
        'servicio', 'usuario final', 'app', 'cliente', 'correo electrónico', 'erp', 'crm',
        'ofimática', 'suscripción', 'portal web', 'multitenencia', 'interfaz web', 'producto terminado',
        'colaboración', 'gestión de proyectos', 'office 365', 'google workspace', 'dropbox',
        'salesforce', 'slack', 'zoom', 'servicios gestionados', 'software empaquetado',
        'acceso desde navegador', 'interfaz gráfica', 'usuario final'
    ]
    return palabras_clave_similares(texto, saas_keywords)

def contar_faas(texto):
    faas_keywords = [
        'función', 'serverless', 'funciones', 'sin servidor', 'eventos', 'trigger', 'microservicios',
        'ejecución bajo demanda', 'event-driven', 'función como servicio', 'lambda', 'event handler',
        'escalado automático', 'funciones pequeñas', 'backend sin servidor',
        'az functions', 'google cloud functions', 'aws lambda', 'orquestación de funciones',
        'automatización basada en eventos', 'ejecución en la nube', 'facturación por ejecución'
    ]
    return palabras_clave_similares(texto, faas_keywords)

def clasificar_servicio_cloud(texto):
    if not texto or texto.strip() == '':
        return "Error: La entrada está vacía. Por favor ingresa un texto válido."
    
    iaas_count = contar_iaas(texto)
    paas_count = contar_paas(texto)
    saas_count = contar_saas(texto)
    faas_count = contar_faas(texto)

    conteos = {
        'IaaS': iaas_count,
        'PaaS': paas_count,
        'SaaS': saas_count,
        'FaaS': faas_count
    }

    categoria = max(conteos, key=conteos.get)
    return categoria

# -------------------------------
# ARGPARSE: permite usar el script por consola
# -------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clasificador de modelos de servicio en la nube (IaaS, PaaS, SaaS, FaaS).")
    parser.add_argument('--texto', type=str, required=True, help='Texto a clasificar')
    args = parser.parse_args()

    resultado = clasificar_servicio_cloud(args.texto)
    print(f"Clasificación: {resultado}")
