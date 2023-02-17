from typing import Optional

from modules.common.component_setup import ComponentSetup


class DeyeModbusConfiguration:
    def __init__(self,
                 ip_address: Optional[str] = None,
                 port: int = 8899):
        self.ip_address = ip_address
        self.port = port


class DeyeModbus:
    def __init__(self,
                 name: str = "Deye (Anbindung per Modbus)",
                 type: str = "deye",
                 id: int = 0,
                 configuration: DeyeModbusConfiguration = None) -> None:
        self.name = name
        self.type = type
        self.id = id
        self.configuration = configuration or DeyeModbusConfiguration()


class DeyeModbusInverterConfiguration:
    def __init__(self, modbus_id: int = 1):
        self.modbus_id = modbus_id


class DeyeModbusInverterSetup(ComponentSetup[DeyeModbusInverterConfiguration]):
    def __init__(self,
                 name: str = "Deye Wechselrichter",
                 type: str = "inverter",
                 id: int = 0,
                 configuration: DeyeModbusInverterConfiguration = None) -> None:
        super().__init__(name, type, id, configuration or DeyeModbusInverterConfiguration())
