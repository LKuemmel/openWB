#!/usr/bin/env python3
import re
from typing import Dict, Union
from requests.auth import HTTPDigestAuth

from dataclass_utils import dataclass_from_dict
from modules.common import req
from modules.common.component_state import InverterState
from modules.common.component_type import ComponentDescriptor
from modules.common.fault_state import ComponentInfo
from modules.common.store import get_inverter_value_store
from modules.devices.deye.config import DeyeInverterSetup


class DeyeInverter:
    def __init__(self,
                 component_config: Union[Dict, DeyeInverterSetup],
                 username: str,
                 password: str,
                 ip_address: str) -> None:
        self.component_config = dataclass_from_dict(DeyeInverterSetup, component_config)
        self.username = username
        self.password = password
        self.ip_address = ip_address
        self.store = get_inverter_value_store(self.component_config.id)
        self.component_info = ComponentInfo.from_component_config(self.component_config)

    def update(self) -> None:
        response = req.get_http_session().get("http://" + self.ip_address + "/status.html",
                                              auth=HTTPDigestAuth(self.username, self.password))
        text = response.text

        now_p = re.search('webdata_now_p = (\d*)', text)
        now_p_value = int(now_p.group())
        # now_p_value = int(re.search('(/d*)'"'. now_p.group()))

        total_e = re.search('webdata_total_e = (\d*)', text)
        total_e_value = int(total_e.group())
        # total_e_value = int(re.search('(/d*)', total_e.group()))

        # Hint:
        # exported: total energy in Wh
        # power: actual power in W

        inverter_state = InverterState(
            power=now_p_value,
            exported=total_e_value
        )
        self.store.set(inverter_state)


component_descriptor = ComponentDescriptor(configuration_factory=DeyeInverterSetup)
