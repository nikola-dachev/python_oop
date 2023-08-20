from abc import ABC , abstractmethod

class Cable(ABC):
  @abstractmethod
  def connect(self, d1, d2):
    pass

class HDMICable(Cable):
  def connect(self, device1, device2):
    return f"Connect {device1} with {device2} via HDMI cable"

class RCACable(Cable):
  def connect(self, device1, device2):
    return f"Connect {device1} with {device2} via RCA cable"

class EthernetCable(Cable):
  def connect(self, device1, device2):
    return f"Connect {device1} with {device2} via Ethernet cable"

class PowerCable(Cable):
  def connect(self, device, ):
    return f"Connect {device} to power"


class DVDPlayer:
  pass

class Television:
  pass

class GameConsole:
  pass

class Router:
  pass

hdmi = HDMICable()
tv = Television()
gc = GameConsole()
hdmi.connect(tv,gc)

