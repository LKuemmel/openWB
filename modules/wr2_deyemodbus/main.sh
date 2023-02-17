#!/bin/bash
OPENWBBASEDIR=$(cd "$(dirname "$0")/../../" && pwd)

bash "$OPENWBBASEDIR/packages/legacy_run.sh" "modules.devices.deye_modbus.device" "inverter" "$pv2deyemodbusip" "$pv2deyemodbusport" "$pv2deyemodbusid" "2" &>>"$OPENWBBASEDIR/ramdisk/openWB.log"

cat "$OPENWBBASEDIR/ramdisk/pvwatt"
