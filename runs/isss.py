#!/usr/bin/python
import logging
import os
import re
import threading
import time
from typing import Dict, List, Optional
import RPi.GPIO as GPIO

from helpermodules.pub import pub_single
from helpermodules import compatibility
from modules.common.store import ramdisk_read
from modules.common.store._util import get_rounding_function_by_digits
from modules.common.fault_state import FaultState
from modules.common.component_state import ChargepointState
from modules.common.modbus import ModbusSerialClient_
from modules.internal_openwb import chargepoint_module, socket
from modules.internal_openwb.chargepoint_module import InternalOpenWB

basePath = "/var/www/html/openWB"
ramdiskPath = basePath + "/ramdisk"
logFilename = ramdiskPath + "/isss.log"
MAP_LOG_LEVEL = [logging.ERROR, logging.WARNING, logging.DEBUG]


logging.basicConfig(filename=ramdiskPath+'/isss.log',
                    format='%(asctime)s - {%(name)s:%(lineno)s} - %(levelname)s - %(message)s',
                    level=MAP_LOG_LEVEL[int(os.environ.get('debug'))])
log = logging.getLogger()
log.error("Loglevel: "+str(int(os.environ.get('debug'))))

pymodbus_logger = logging.getLogger("pymodbus")
pymodbus_logger.setLevel(logging.WARNING)

   if heartbeat > 80:
        set_current = 0
        log.error("Heartbeat Fehler seit " + str(heartbeat) + "Sekunden keine Verbindung, Stoppe Ladung.")

# handling of all logging statements

    if cp_interruption_duration > 0:
        self.__thread_cp_interruption(cp_interruption_duration)


class UpdateValues:
    MAP_KEY_TO_OLD_TOPIC = {
        "imported": "kWhCounter",
        "exported": None,
        "power": "W",
        "voltages": ["VPhase1", "VPhase2", "VPhase3"],
        "currents": ["APhase1", "APhase2", "APhase3"],
        "power_factors": None,
        "phases_in_use": "countPhasesInUse",
        "charge_state": "boolChargeStat",
        "plug_state": "boolPlugStat",
        "rfid": "LastScannedRfidTag",
    }

    def __init__(self, local_charge_point_num: int) -> None:
        self.cp_num = str(Isss.get_cp_num(local_charge_point_num))
        self.parent_wb = Isss.get_parent_wb()
        self.old_counter_state = None

    def update_values(self, counter_state: ChargepointState) -> None:
        if self.old_counter_state:
            # iterate over counterstate
            vars_old_counter_state = vars(self.old_counter_state)
            for key, value in vars(counter_state).items():
                if value != vars_old_counter_state[key]:
                    # pub to 1.9
                    topic = self.MAP_KEY_TO_OLD_TOPIC[key]
                    if topic is not None:
                        if isinstance(topic, List):
                            for i in range(0, 3):
                                self.pub_values_to_1_9(topic[i], value[i])
                        else:
                            self.pub_values_to_1_9(self.MAP_KEY_TO_OLD_TOPIC[key], value)
                    # pub to 2.0
                    self.pub_values_to_2(key, value)
            self.old_counter_state = counter_state
        else:
            # Bei Neustart alles publishen
            for key, value in vars(counter_state).items():
                # pub to 1.9
                topic = self.MAP_KEY_TO_OLD_TOPIC[key]
                if topic is not None:
                    if isinstance(topic, List):
                        for i in range(0, 3):
                            self.pub_values_to_1_9(topic[i], value[i])
                    else:
                        self.pub_values_to_1_9(self.MAP_KEY_TO_OLD_TOPIC[key], value)
                # pub to 2.0
                self.pub_values_to_2(key, value)

        try:
            if lp1lla1 > 3:
                lp1countphasesinuse = 1
            if lp1lla2 > 3:
                lp1countphasesinuse = 2
            if lp1lla3 > 3:
                lp1countphasesinuse = 3
        except Exception:
            FaultState.warning("Es konnte keine Ladepunkt-Nummer ermittelt werden. Auf Default-Wert 0 gesetzt.")
            return 0

    @staticmethod
    def get_parent_wb() -> str:
        # check for parent openWB
        try:
            return ramdisk_read("parentWB").replace('\\n', '').replace('\"', '')
        except Exception:
            FaultState.warning("Für den Betrieb im Nur-Ladepunkt-Modus ist zwingend eine Master-openWB erforderlich.")
            return ""


class IsssChargepoint:
    def __init__(self, serial_client, local_charge_point_num) -> None:
        self.local_charge_point_num = local_charge_point_num
        if local_charge_point_num == 1:
            try:
                with open('/home/pi/ppbuchse', 'r') as f:
                    max_current = int(f.read())
                self.module = socket.Socket(max_current, InternalOpenWB(1, serial_client))
            except (FileNotFoundError, ValueError):
                self.module = chargepoint_module.ChargepointModule(InternalOpenWB(1, serial_client))
        else:
            self.module = chargepoint_module.ChargepointModule(InternalOpenWB(2, serial_client))
        self.update_values = UpdateValues(local_charge_point_num)
        self.update_state = UpdateState(self.module)
        self.old_plug_state = False

    def update(self):
        def __thread_active(thread: Optional[threading.Thread]):
            if thread:
                return thread.is_alive()
        try:
            if self.local_charge_point_num == 2:
                time.sleep(0.1)
            phase_switch_cp_active = __thread_active(self.update_state.cp_interruption_thread) or __thread_active(self.update_state.phase_switch_thread)
            state, _ = self.module.get_values(phase_switch_cp_active)
            log.debug("Published plug state "+str(state.plug_state))
            self.update_values.update_values(state)
            self.update_state.update_state()
        except Exception:
            log.exception("Fehler bei Ladepunkt "+str(self.local_charge_point_num))


Isss().loop()
