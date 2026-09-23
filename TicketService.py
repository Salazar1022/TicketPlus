from InventarioStub import InventarioStub
from UsuarioDummy import UsuarioDummy
from RepositorioFake import RepositorioFake

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
Service = TicketService(InventarioStub(), RepositorioFake(), None)
resultado = Service.comprar("Ana", 2)
print(resultado)

