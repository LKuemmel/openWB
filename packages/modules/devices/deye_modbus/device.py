#!/usr/bin/env python3
import logging
from typing import Iterable, Optional, List

from helpermodules.cli import run_using_positional_cli_args
from modules.common.abstract_device import DeviceDescriptor
from modules.common.component_context import SingleComponentUpdateContext
from modules.common.configurable_device import ConfigurableDevice, ComponentFactoryByType, MultiComponentUpdater
from modules.common.modbus import ModbusTcpClient_
from modules.devices.deye_modbus.inverter import DeyeModbusInverter
from modules.devices.deye_modbus import inverter
from modules.devices.deye_modbus.config import DeyeModbus, DeyeModbusConfiguration, DeyeModbusInverterSetup

log = logging.getLogger(__name__)


def create_device(device_config: DeyeModbus):
    def create_inverter_component(component_config: DeyeModbusInverterSetup):
        return DeyeModbusInverter(component_config)

    def update_components(components: Iterable[DeyeModbusInverter]):
        with client as c:
            for component in components:
                with SingleComponentUpdateContext(component.component_info):
                    component.update(c)

    try:
        client = ModbusTcpClient_(device_config.configuration.ip_address, device_config.configuration.port)
    except Exception:
        log.exception("Fehler in create_device")
    return ConfigurableDevice(
        device_config=device_config,
        component_factory=ComponentFactoryByType(
            inverter=create_inverter_component,
        ),
        component_updater=MultiComponentUpdater(update_components)
    )


COMPONENT_TYPE_TO_MODULE = {
    "inverter": inverter
}


def read_legacy(component_type: str, ip_address: str, port: int, modbus_id: int, num: Optional[int] = None) -> None:
    device_config = DeyeModbus(configuration=DeyeModbusConfiguration(
        port=port, ip_address=ip_address))

    dev = create_device(device_config)
    if component_type in COMPONENT_TYPE_TO_MODULE:
        component_config = COMPONENT_TYPE_TO_MODULE[component_type].component_descriptor.configuration_factory()
    else:
        raise Exception(
            "illegal component type " + component_type + ". Allowed values: " +
            ','.join(COMPONENT_TYPE_TO_MODULE.keys())
        )
    component_config.configuration.modbus_id = modbus_id
    component_config.id = num
    dev.add_component(component_config)

    log.debug('Deye Port: ' + str(port))
    log.debug('Deye ID: ' + str(modbus_id))
    log.debug('Deye IP-Adresse: ' + ip_address)

    dev.update()


def main(argv: List[str]):
    run_using_positional_cli_args(read_legacy, argv)


device_descriptor = DeviceDescriptor(configuration_factory=DeyeModbus)
