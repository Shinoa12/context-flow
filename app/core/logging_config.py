import logging

def setup_logging():

    # Crear un logger base
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)  # Mostrar todos los niveles de log

    # Crear un handler para imprimir en consola
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # Definir el formato de los logs
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    console_handler.setFormatter(formatter)

    # Agregar el handler al logger base
    if not logger.hasHandlers():
        logger.addHandler(console_handler)
