class ResourceNotFoundException(Exception):
    """Exceção para quando um recurso não é encontrado."""
    
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class BadRequestException(Exception):
    """Exceção para quando uma requisição é inválida."""
    
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)