
# ==================================================
# REGISTRO DE EVENTOS Y ERRORES - SOFTWARE FJ
# ==================================================

import logging

# Configuración del archivo de registros
logging.basicConfig(
    filename="software_fj.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8
    "
)


def registrar_evento(mensaje):
    """Registra los eventos importantes del sistema."""
    logging.info(mensaje)


def registrar_error(mensaje):
    """Registra los errores que ocurren en el sistema."""
    logging.error(mensaje)


def registrar_excepcion(mensaje):
    """Registra información detallada de una excepción."""
    logging.exception(mensaje)
