
# ==================================================
# GESTION DE RESERVAS - SOFTWARE FJ
# ==================================================

from excepciones import (
    ReservaInvalidaError,
    OperacionNoPermitidaError
)


class Reserva:
    """Representa una reserva realizada por un cliente."""

    contador = 0

    def __init__(self, cliente, servicio, duracion):
        if cliente is None or servicio is None:
            raise ReservaInvalidaError(
                "El cliente y el servicio son obligatorios."
            )

        servicio.validar_parametros(duracion)

        Reserva.contador += 1
        self.identificador = Reserva.contador
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def calcular_total(self, descuento=0, impuesto=0):
        """Calcula el costo con descuento e impuesto."""

        if not isinstance(descuento, (int, float)) or isinstance(descuento, bool):
            raise ReservaInvalidaError("Descuento inválido.")

        if not isinstance(impuesto, (int, float)) or isinstance(impuesto, bool):
            raise ReservaInvalidaError("Impuesto inválido.")

        if not 0 <= descuento <= 100:
            raise ReservaInvalidaError("Descuento fuera de rango.")

        if not 0 <= impuesto <= 100:
            raise ReservaInvalidaError("Impuesto fuera de rango.")

        subtotal = self.servicio.calcular_costo(
            self.duracion, descuento
        )

        return subtotal + (subtotal * impuesto / 100)

    def confirmar(self):
        if self.estado != "Pendiente":
            raise OperacionNoPermitidaError(
                "Solo se pueden confirmar reservas pendientes."
            )

        self.estado = "Confirmada"
        return "Reserva confirmada correctamente."

    def cancelar(self):
        if self.estado == "Cancelada":
            raise OperacionNoPermitidaError(
                "La reserva ya está cancelada."
            )

        self.estado = "Cancelada"
        return "Reserva cancelada correctamente."

    def mostrar_reserva(self):
        return (
            f"Reserva: {self.identificador} | "
            f"Cliente: {self.cliente.nombre} | "
            f"Servicio: {self.servicio.nombre} | "
            f"Duración: {self.duracion} | "
            f"Estado: {self.estado}"
        )
