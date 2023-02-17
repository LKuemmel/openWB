#!/usr/bin/env python3
from typing import Dict, Union

from dataclass_utils import dataclass_from_dict
from modules.common.component_state import InverterState
from modules.common.component_type import ComponentDescriptor
from modules.common.fault_state import ComponentInfo
from modules.common.modbus import ModbusDataType, ModbusTcpClient_
from modules.common.store import get_inverter_value_store
from modules.devices.deye_modbus.config import DeyeModbusInverterSetup


class DeyeModbusInverter:
    def __init__(self, component_config: Union[Dict, DeyeModbusInverterSetup]) -> None:
        self.component_config = dataclass_from_dict(DeyeModbusInverterSetup, component_config)
        self.store = get_inverter_value_store(self.component_config.id)
        self.component_info = ComponentInfo.from_component_config(self.component_config)

    def update(self, client: ModbusTcpClient_) -> None:
        unit = self.component_config.configuration.modbus_id
        power = client.read_holding_registers(0x3F, ModbusDataType.INT_32, unit=unit)
        dc_power = client.read_holding_registers(0x52, ModbusDataType.INT_16, unit=unit)
        exported = client.read_holding_registers(0x56, ModbusDataType.INT_32, unit=unit)
        currents = client.read_holding_registers(0x4C, [ModbusDataType.INT_16]*3, unit=unit)

        inverter_state = InverterState(
            currents=currents,
            power=power,
            exported=exported,
            dc_power=dc_power
        )
        self.store.set(inverter_state)


component_descriptor = ComponentDescriptor(configuration_factory=DeyeModbusInverterSetup)
