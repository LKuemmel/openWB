from typing import Optional

from modules.common.component_setup import ComponentSetup


class DeyeConfiguration:
    def __init__(self,
                 username: Optional[str] = None,
                 password: Optional[str] = None,
                 ip_address: Optional[str] = None):
        self.username = username
        self.password = password
        self.ip_address = ip_address


class Deye:
    def __init__(self,
                 name: str = "Deye",
                 type: str = "deye",
                 id: int = 0,
                 configuration: DeyeConfiguration = None) -> None:
        self.name = name
        self.type = type
        self.id = id
        self.configuration = configuration or DeyeConfiguration()


class DeyeInverterConfiguration:
    def __init__(self):
        pass


class DeyeInverterSetup(ComponentSetup[DeyeInverterConfiguration]):
    def __init__(self,
                 name: str = "Deye Wechselrichter",
                 type: str = "inverter",
                 id: int = 0,
                 configuration: DeyeInverterConfiguration = None) -> None:
        super().__init__(name, type, id, configuration or DeyeInverterConfiguration())
