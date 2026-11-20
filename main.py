

# ==========================================================
# SOFTWARE FJ
# SISTEMA INTEGRAL DE CLIENTES, SERVICIOS Y RESERVAS
# Curso: Programacion - UNAD
# ==========================================================

from entidades import Cliente
from servicios import (
    ReservaSala,
    AlquilerEquipos,
    AsesoriaEspecializada
)
from reservas import Reserva
from excepciones import (
    DatosInvalidosError,
    ReservaInvalidaError,
    OperacionNoPermitidaError
)
from logs import (
    registrar_evento,
    registrar_error,
    registrar_excepcion
)


def ejecutar_pruebas():
    print("=" * 55)
    print(" SISTEMA INTEGRAL DE GESTION - SOFTWARE FJ")
    print("=" * 55)

    clientes = []
    servicios = []
    reservas = []

    # OPERACION 1: Registrar un cliente valido
    print("\nOPERACION 1: Registro de cliente")
    try:
        cliente1 = Cliente(
            "C001",
            "Carlos Perez",
            "carlos@gmail.com",
            "3001234567"
        )
        clientes.append(cliente1)
        print(cliente1.mostrar_informacion())
        registrar_evento("Cliente registrado correctamente.")
    except DatosInvalidosError as error:
        print("Error:", error)
        registrar_excepcion("Error al registrar cliente.")

    # OPERACION 2: Intentar registrar un cliente invalido
    print("\nOPERACION 2: Registro de cliente invalido")
    try:
        cliente2 = Cliente(
            "C002",
            "",
            "correo incorrecto",
            "3004567890"
        )
        clientes.append(cliente2)
    except DatosInvalidosError as error:
        print("Error controlado:", error)
        registrar_error("Intento de registro de cliente invalido.")

    # OPERACION 3: Crear servicio de salas
    print("\nOPERACION 3: Crear servicio de salas")
    sala = ReservaSala("Reserva de sala", 50000)
    servicios.append(sala)
    print(sala.describir_servicio())
    registrar_evento("Servicio de salas creado.")

    # OPERACION 4: Crear servicio de alquiler de equipos
    print("\nOPERACION 4: Crear servicio de equipos")
    equipo = AlquilerEquipos("Alquiler de computadores", 30000)
    servicios.append(equipo)
    print(equipo.describir_servicio())
    registrar_evento("Servicio de equipos creado.")

    # OPERACION 5: Crear servicio de asesorias
    print("\nOPERACION 5: Crear servicio de asesorias")
    asesoria = AsesoriaEspecializada("Asesoria profesional", 80000)
    servicios.append(asesoria)
    print(asesoria.describir_servicio())
    registrar_evento("Servicio de asesorias creado.")

    # OPERACION 6: Intentar crear un servicio invalido
    print("\nOPERACION 6: Crear servicio invalido")
    try:
        servicio_invalido = ReservaSala("Sala", -5000)
    except DatosInvalidosError as error:
        print("Error controlado:", error)
        registrar_error("Intento de crear servicio con precio invalido.")

    # OPERACION 7: Crear una reserva correctamente
    print("\nOPERACION 7: Crear reserva")
    try:
        reserva1 = Reserva(cliente1, sala, 2)
        reservas.append(reserva1)
        print(reserva1.mostrar_reserva())
        registrar_evento("Reserva creada correctamente.")
    except (ReservaInvalidaError, DatosInvalidosError) as error:
        print("Error:", error)
        registrar_excepcion("Error al crear reserva.")

    # OPERACION 8: Confirmar la reserva
    print("\nOPERACION 8: Confirmar reserva")
    try:
        mensaje = reserva1.confirmar()
        print(mensaje)
        registrar_evento("Reserva confirmada.")
    except OperacionNoPermitidaError as error:
        print("Error:", error)
        registrar_excepcion("Error al confirmar reserva.")

    # OPERACION 9: Calcular el costo con descuento e impuesto
    print("\nOPERACION 9: Calcular costo")
    try:
        total = reserva1.calcular_total(
            descuento=10,
            impuesto=19
        )
        print(f"Total de la reserva: ${total:,.2f}")
        registrar_evento("Costo de reserva calculado.")
    except (ReservaInvalidaError, DatosInvalidosError) as error:
        print("Error:", error)
        registrar_excepcion("Error al calcular costo.")

    # OPERACION 10: Cancelar la reserva
    print("\nOPERACION 10: Cancelar reserva")
    try:
        print(reserva1.cancelar())
        registrar_evento("Reserva cancelada.")
    except OperacionNoPermitidaError as error:
        print("Error:", error)
        registrar_excepcion("Error al cancelar reserva.")

    # OPERACION 11: Intentar confirmar una reserva cancelada
    print("\nOPERACION 11: Operacion no permitida")
    try:
        reserva1.confirmar()
    except OperacionNoPermitidaError as error:
        print("Error controlado:", error)
        registrar_error("Intento de confirmar una reserva cancelada.")

    # OPERACION 12: Intentar crear reserva con duracion incorrecta
    print("\nOPERACION 12: Reserva con duracion invalida")
    try:
        reserva_invalida = Reserva(cliente1, sala, -3)
    except DatosInvalidosError as error:
        print("Error controlado:", error)
        registrar_error("Intento de reserva con duracion negativa.")

    # OPERACION 13: Demostrar encadenamiento de excepciones
    print("\nOPERACION 13: Encadenamiento de excepciones")
    try:
        try:
            Cliente("C003", "Ana", "correo_invalido", "3001111111")
        except DatosInvalidosError as error:
            raise RuntimeError(
                "No fue posible completar el registro del cliente."
            ) from error
    except RuntimeError as error:
        print("Error encadenado:", error)
        registrar_excepcion("Error encadenado durante el registro.")

    # OPERACION 14: Demostrar try, except, else y finally
    print("\nOPERACION 14: Manejo avanzado de excepciones")
    try:
        resultado = sala.calcular_costo(2)
    except DatosInvalidosError as error:
        print("Error:", error)
        registrar_excepcion("Error en calculo del servicio.")
    else:
        print("Calculo realizado correctamente:", resultado)
        registrar_evento("Prueba de calculo exitosa.")
    finally:
        print("Finalizo la prueba de manejo de excepciones.")

    print("\n" + "=" * 55)
    print("RESUMEN DEL SISTEMA")
    print("Clientes registrados:", len(clientes))
    print("Servicios creados:", len(servicios))
    print("Reservas creadas:", len(reservas))
    print("El sistema finalizo las pruebas.")
    print("=" * 55)

    registrar_evento("Ejecucion de pruebas finalizada.")


if __name__ == "__main__":
    ejecutar_pruebas()
