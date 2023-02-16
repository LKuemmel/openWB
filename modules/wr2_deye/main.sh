#!/bin/bash
OPENWBBASEDIR=$(cd "$(dirname "$0")/../../" && pwd)

bash "$OPENWBBASEDIR/packages/legacy_run.sh" "modules.devices.deye.device" "inverter" "$wr2deyehost" "$wr2deyeusername" "$wr2deyepassword" "2" &>>"$OPENWBBASEDIR/ramdisk/openWB.log"

cat "$OPENWBBASEDIR/ramdisk/pvwatt"
