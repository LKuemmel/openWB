/**
 * Functions to update graph and gui values via MQTT-messages
 *
 * @author Kevin Wieland
 * @author Michael Ortenstein
 */

function handlevar(mqttmsg, mqttpayload) {
	// receives all messages and calls respective function to process them
 	processPreloader(mqttmsg);
	switch(mqttmsg){
		case "openWB/evu/ASchieflast": directShow(mqttpayload, '#schieflastdiv'); visibilityValue('#schieflastEvuStatusId', '#schieflastdiv'); break;
		case "openWB/evu/APhase1": directShow(mqttpayload, '#bezuga1div'); visibilityRow('#stromstaerkeEvuStatusId', '#bezuga1div', '#bezuga2div', '#bezuga3div'); break;
		case "openWB/evu/APhase2": directShow(mqttpayload, '#bezuga2div'); visibilityRow('#stromstaerkeEvuStatusId', '#bezuga1div', '#bezuga2div', '#bezuga3div'); break;
		case "openWB/evu/APhase3": directShow(mqttpayload, '#bezuga3div'); visibilityRow('#stromstaerkeEvuStatusId', '#bezuga1div', '#bezuga2div', '#bezuga3div'); break;
		case "openWB/evu/WPhase1": impExpShow(mqttpayload, '#bezugw1div'); visibilityRow('#leistungEvuStatusId', '#bezugw1div', '#bezugw2div', '#bezugw3div'); break;
		case "openWB/evu/WPhase2": impExpShow(mqttpayload, '#bezugw2div'); visibilityRow('#leistungEvuStatusId', '#bezugw1div', '#bezugw2div', '#bezugw3div'); break;
		case "openWB/evu/WPhase3": impExpShow(mqttpayload, '#bezugw3div'); visibilityRow('#leistungEvuStatusId', '#bezugw1div', '#bezugw2div', '#bezugw3div'); break;
		case "openWB/lp/1/AConfigured": directShow(mqttpayload, '#llsolldiv'); break;
		case "openWB/lp/2/AConfigured": directShow(mqttpayload, '#llsolls1div'); break;
		case "openWB/lp/3/AConfigured": directShow(mqttpayload, '#llsolls2div'); break;
		case "openWB/lp/2/APhase1": directShow(mqttpayload, '#llas11div'); break;
		case "openWB/lp/2/APhase2": directShow(mqttpayload, '#llas12div'); break;
		case "openWB/lp/2/APhase3": directShow(mqttpayload, '#llas13div'); break;
		case "openWB/lp/3/APhase1": directShow(mqttpayload, '#llas21div'); break;
		case "openWB/lp/3/APhase2": directShow(mqttpayload, '#llas22div'); break;
		case "openWB/lp/3/APhase3": directShow(mqttpayload, '#llas23div'); break;
		case "openWB/lp/1/APhase1": directShow(mqttpayload, '#lla1div'); break;
		case "openWB/lp/1/APhase2": directShow(mqttpayload, '#lla2div'); break;
		case "openWB/lp/1/APhase3": directShow(mqttpayload, '#lla3div'); break;
		case "openWB/lp/1/kWhCounter": directShow(mqttpayload, '#llkwhdiv'); break;
		case "openWB/lp/2/kWhCounter": directShow(mqttpayload, '#llkwhs1div'); break;
		case "openWB/lp/3/kWhCounter": directShow(mqttpayload, '#llkwhs2div'); break;
		case "openWB/Verbraucher/1/Watt": directShow(mqttpayload, '#verbraucher1wattdiv'); break;
		case "openWB/Verbraucher/1/WhImported": kShow(mqttpayload, "#verbraucher1whdiv"); break;
		case "openWB/Verbraucher/1/WhExported": kShow(mqttpayload, "#verbraucher1whediv"); break;
		case "openWB/Verbraucher/2/Watt": directShow(mqttpayload, '#verbraucher2wattdiv'); break;
		case "openWB/Verbraucher/2/WhImported": kShow(mqttpayload, "#verbraucher2whdiv"); break;
		case "openWB/Verbraucher/2/WhExported": kShow(mqttpayload, "#verbraucher2whediv"); break;
		case "openWB/evu/WhExported": kShow(mqttpayload, "#einspeisungkwhdiv"); visibilityValue('#einspeisungEvuStatusId', "#einspeisungkwhdiv"); break;
		case "openWB/evu/WhImported": kShow(mqttpayload, "#bezugkwhdiv"); visibilityValue('#bezugEvuStatusId', "#bezugkwhdiv"); break;
		case "openWB/housebattery/WhImported": kShow(mqttpayload, "#speicherikwhdiv"); break;
		case "openWB/housebattery/WhExported": kShow(mqttpayload, "#speicherekwhdiv"); break;
		case "openWB/pv/CounterTillStartPvCharging": directShow(mqttpayload, '#pvcounterdiv'); break;
		case "openWB/pv/DailyYieldKwh": directShow(mqttpayload, '#daily_pvkwhdiv'); break;
		case "openWB/lp/1/VPhase1": directShow(mqttpayload, '#llv1div'); break;
		case "openWB/lp/1/VPhase2": directShow(mqttpayload, '#llv2div'); break;
		case "openWB/lp/1/VPhase3": directShow(mqttpayload, '#llv3div'); break;
		case "openWB/lp/2/VPhase1": directShow(mqttpayload, '#llv1s1div'); break;
		case "openWB/lp/3/VPhase1": directShow(mqttpayload, '#llv1s2div'); break;
		case "openWB/lp/2/VPhase2": directShow(mqttpayload, '#llv2s1div'); break;
		case "openWB/lp/3/VPhase2": directShow(mqttpayload, '#llv2s2div'); break;
		case "openWB/lp/2/VPhase3": directShow(mqttpayload, '#llv3s1div'); break;
		case "openWB/lp/3/VPhase3": directShow(mqttpayload, '#llv3s2div'); break;
		case "openWB/lp/1/PfPhase1": directShow(mqttpayload, '#llpf1div'); break;
		case "openWB/lp/1/PfPhase2": directShow(mqttpayload, '#llpf2div'); break;
		case "openWB/lp/1/PfPhase3": directShow(mqttpayload, '#llpf3div'); break;
		case "openWB/evu/VPhase1": directShow(mqttpayload, '#evuv1div'); visibilityRow('#spannungEvuStatusId', '#evuv1div', '#evuv2div', '#evuv3div'); break;
		case "openWB/evu/VPhase2": directShow(mqttpayload, '#evuv2div'); visibilityRow('#spannungEvuStatusId', '#evuv1div', '#evuv2div', '#evuv3div'); break;
		case "openWB/evu/VPhase3": directShow(mqttpayload, '#evuv3div'); visibilityRow('#spannungEvuStatusId', '#evuv1div', '#evuv2div', '#evuv3div'); break;
		case "openWB/evu/Hz": directShow(mqttpayload, '#evuhzdiv'); visibilityValue('#frequenzEvuStatusId', '#evuhzdiv'); break;
		case "openWB/evu/PfPhase1": directShow(mqttpayload, '#evupf1div'); visibilityRow('#powerfaktorEvuStatusId', '#evupf1div', '#evupf2div', '#evupf3div'); break;
		case "openWB/evu/PfPhase2": directShow(mqttpayload, '#evupf2div'); visibilityRow('#powerfaktorEvuStatusId', '#evupf1div', '#evupf2div', '#evupf3div'); break;
		case "openWB/evu/PfPhase3": directShow(mqttpayload, '#evupf3div'); visibilityRow('#powerfaktorEvuStatusId', '#evupf1div', '#evupf2div', '#evupf3div'); break;
		default: break;}
}  // end handlevar


// don't parse value
function directShow(mqttpayload, variable) {
		var value = parseFloat(mqttpayload);
		if ( isNaN(value) ) {
			value = 0;
		}
		var valueStr = value.toLocaleString(undefined) ;
		$(variable).text(valueStr);
}

//show with imp/exp
function impExpShow(mqttpayload, variable) {
	// zur Anzeige Wert um "Bezug"/"Einspeisung" ergänzen
	var value = parseInt(mqttpayload);
	var valueStr = "";
	if(value<0) {
		value = value * -1;
		valueStr = valueStr+value+" (E)"
	} else if (value>0) {
		valueStr = valueStr+value+" (B)"
	} else  {
		// Bezug = 0
		valueStr = valueStr+value
	}
	$(variable).text(valueStr);
}

// show value as kilo
function kShow(mqttpayload, variable) {
	var value = parseFloat(mqttpayload);
	value = (value / 1000).toFixed(3);
	var valueStr = value.toLocaleString(undefined) ;
	$(variable).text(valueStr);
}

//show/hide row with only one value
function visibilityValue(row, variable){
	if (( $(variable).text() != "0") && ( $(variable).text() != "")) {
		showSection($(row));
	}
	else {
		hideSection($(row));
	}
}

//show/hide complete row, if all three values are zero or empty
function visibilityRow(row, var1, var2, var3) {
	if ( ( ($(var1).text() == "0") || ($(var1).text() == "") ) &&
		 ( ($(var2).text() == "0") || ($(var2).text() == "") ) &&
		 ( ($(var3).text() == "0") || ($(var3).text() == "") ) ) {
		hideSection($(row));
	}
	else {
		showSection($(row));
	}
}