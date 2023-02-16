#!/usr/bin/env python3
import logging
from typing import Optional, List

from helpermodules.cli import run_using_positional_cli_args
from modules.common.abstract_device import DeviceDescriptor
from modules.common.configurable_device import ConfigurableDevice, ComponentFactoryByType, IndependentComponentUpdater
from modules.devices.deye import inverter
from modules.devices.deye.config import Deye, DeyeConfiguration, DeyeInverterSetup

log = logging.getLogger(__name__)


def create_device(device_config: Deye):
    def create_inverter_component(component_config: DeyeInverterSetup):
        return inverter.DeyeInverter(component_config,
                                     device_config.configuration.username,
                                     device_config.configuration.password,
                                     device_config.configuration.ip_address)

    return ConfigurableDevice(
        device_config=device_config,
        component_factory=ComponentFactoryByType(
            inverter=create_inverter_component,
        ),
        component_updater=IndependentComponentUpdater(lambda component: component.update())
    )


COMPONENT_TYPE_TO_MODULE = {
    "inverter": inverter
}


def read_legacy(component_type: str, ip_address: str, username: str, password: str, num: Optional[int] = None) -> None:
    device_config = Deye(configuration=DeyeConfiguration(username=username, password=password, ip_address=ip_address))

    dev = create_device(device_config)
    if component_type in COMPONENT_TYPE_TO_MODULE:
        component_config = COMPONENT_TYPE_TO_MODULE[component_type].component_descriptor.configuration_factory()
    else:
        raise Exception(
            "illegal component type " + component_type + ". Allowed values: " +
            ','.join(COMPONENT_TYPE_TO_MODULE.keys())
        )
    component_config.id = num
    dev.add_component(component_config)

    log.debug('Deye Username: ' + username)
    log.debug('Deye Passwort: ' + password)
    log.debug('Deye IP-Adresse: ' + ip_address)

    dev.update()


def main(argv: List[str]):
    run_using_positional_cli_args(read_legacy, argv)


device_descriptor = DeviceDescriptor(configuration_factory=Deye)
