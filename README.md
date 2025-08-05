# FuerzaBrutaPy-AR

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

Un potente generador de diccionarios de contraseñas escrito en Python, enfocado en crear listas de palabras altamente personalizadas y efectivas para auditorías de seguridad y pruebas de penetración.

Este script toma listas de palabras comunes y aplica múltiples capas de mutación para generar un diccionario extenso y robusto, incluyendo reglas específicas adaptadas a la cultura y modismos de Argentina.

## Características Principales

- **Múltiples Capas de Mutación**: Aplica una serie de transformaciones para maximizar la cobertura.
- **Sustitución Leetspeak**: Reemplaza letras por símbolos comunes (ej: `a` por `@`, `e` por `3`).
- **Combinaciones Numéricas**: Añade secuencias numéricas, años y fechas de nacimiento comunes.
- **Patrones de Teclado**: Genera secuencias basadas en la disposición de teclados QWERTY y de teléfono.
- **Contexto Argentino**: Incorpora nombres, apellidos, lugares, equipos de fútbol y modismos de Argentina.
- **Tendencias Actuales**: Utiliza temas populares y nombres de personajes de la cultura pop.
- **Generación para Wi-Fi**: Crea variaciones específicas a partir del nombre de una red (SSID).
- **Fácil de Usar**: Interfaz de línea de comandos simple e intuitiva.

## Requisitos

- Python 3.x

No se requieren bibliotecas externas.

## Instrucciones de Uso

1.  Clona o descarga este repositorio.
2.  Abre una terminal en el directorio del proyecto.
3.  Ejecuta el script con el siguiente comando:

    ```bash
    python generador_avanzado_contraseñas.py [OPCIONES]
    ```

### Opciones

-   `-o, --output`: Especifica el nombre del archivo de salida.
    -   *Valor por defecto*: `super_diccionario_avanzado.txt`
-   `--wifi`: Genera variaciones para un SSID de Wi-Fi específico.
-   `--help`: Muestra el menú de ayuda.

### Ejemplos

**Generar un diccionario estándar:**

```bash
python generador_avanzado_contraseñas.py -o mi_diccionario.txt
```

**Generar un diccionario para una red Wi-Fi llamada "MiRedWifi":**

```bash
python generador_avanzado_contraseñas.py --wifi "MiRedWifi" -o claves_para_mi_red.txt
```

## Advertencia de Uso Ético

Esta herramienta fue creada con fines educativos y para ser utilizada en auditorías de seguridad autorizadas. El uso de este software para atacar sistemas sin el consentimiento previo de sus propietarios es ilegal. El autor no se hace responsable del mal uso de esta herramienta.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
