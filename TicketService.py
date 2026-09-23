from InventarioStub import InventarioStub
from UsuarioDummy import UsuarioDummy
from RepositorioFake import RepositorioFake
from EmailDummy import EmailDummy
from InventarioSpy import InventarioSpy

from unittest.mock import Mock

email_mock = Mock()
inventario_spy = InventarioSpy()

class TicketService:
    def __init__(self, inventario, repositorio, email_service):
        self.inventario = inventario
        self.repositorio = repositorio
        self.email_service = email_service

    def comprar(self, usuario, cantidad):
        disponibles = self.inventario.consultar_disponibilidad()

        if disponibles < cantidad:
            return False

        self.repositorio.guardar(usuario, cantidad)
        self.email_service.enviar_confirmacion(usuario)
        return True

# Service = TicketService(None, None, None)
# Service = TicketService(InventarioStub(), None, None)
# Service = TicketService(InventarioStub(), UsuarioDummy(), None)
# Service = TicketService(InventarioStub(), RepositorioFake(), None)
# resultado = Service.comprar("Ana", 2)
# print(resultado)

# Service = TicketService(InventarioStub(), RepositorioFake(), EmailDummy())

# Service = TicketService(InventarioStub(), RepositorioFake(), email_mock)
# resultado = Service.comprar(UsuarioDummy(), 2)
# print(resultado)
# email_mock.enviar_confirmacion.assert_called_once()

Service = TicketService(inventario_spy, RepositorioFake(), email_mock)
Service.comprar(UsuarioDummy(), 2)
Service.comprar(UsuarioDummy(), 1)
print(inventario_spy.veces_consultado)
