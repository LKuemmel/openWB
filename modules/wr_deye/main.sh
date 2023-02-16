#!/bin/bash
OPENWBBASEDIR=$(cd "$(dirname "$0")/../../" && pwd)

bash "$OPENWBBASEDIR/packages/legacy_run.sh" "modules.devices.deye.device" "inverter" "$wrdeyehost" "$wrdeyeusername" "$wrdeyepassword" "1" &>>"$OPENWBBASEDIR/ramdisk/openWB.log"

cat "$OPENWBBASEDIR/ramdisk/pvwatt"
