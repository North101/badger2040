POLLIN = 1
POLLHUP = 16
SOL_SOCKET = 0
SO_REUSEADDR = 0


def getaddrinfo(*args, **kwargs) -> list:
  pass


class socket:
  def __init__(self, *args, **kwargs):
    pass

  def accept(self) -> tuple['socket', tuple[str, int]]:
    pass

  def connect(self, *args, **kwargs):
    pass

  def listen(self):
    pass

  def bind(self, *args, **kwargs):
    pass

  def send(self, data: bytes) -> int:
    pass

  def recv(self, length: int = -1):
    pass

  def close(self):
    pass
  
  def fileno(self) -> int:
    pass

  def setsockopt(self, *args, **kwargs):
    pass