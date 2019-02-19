<?php

$lines = file('/var/www/html/openWB/openwb.conf');
foreach($lines as $line) {
	if(strpos($line, "minimalstromstaerke=") !== false) {
		list(, $minimalstromstaerkeold) = explode("=", $line);
	}
	if(strpos($line, "maximalstromstaerke=") !== false) {
		list(, $maximalstromstaerkeold) = explode("=", $line);
	}
}

$minimalstromstaerkeold = intval($minimalstromstaerkeold);
$maximalstromstaerkeold = intval($maximalstromstaerkeold);

if(isset($_GET["lademodus"])) {
	if($_GET["lademodus"] == "jetzt") {
	file_put_contents('/var/www/html/openWB/ramdisk/lademodus', 0);
	}

	if($_GET["lademodus"] == "minundpv") {
	file_put_contents('/var/www/html/openWB/ramdisk/lademodus', 1);
	}
	if($_GET["lademodus"] == "pvuberschuss") {
	file_put_contents('/var/www/html/openWB/ramdisk/lademodus', 2);
	}
	if($_GET["lademodus"] == "stop") {
	file_put_contents('/var/www/html/openWB/ramdisk/lademodus', 3);
	}
}
if(isset($_GET["sofortlllp1"])) {
	if($_GET["sofortlllp1"] >= $minimalstromstaerkeold && $_GET["sofortlllp1"] <= $maximalstromstaerkeold) {
		$result = '';
		$lines = file('/var/www/html/openWB/openwb.conf');
		foreach($lines as $line) {
			if(strpos($line, "sofortll=") !== false) {
			    $result .= 'sofortll='.$_GET[sofortlllp1]."\n";
			}
			else {
			    $result .= $line;
			}
		}
		file_put_contents('/var/www/html/openWB/openwb.conf', $result);

	}
}
if(isset($_GET["sofortlllp2"])) {

	if($_GET["sofortlllp2"] >= $minimalstromstaerkeold && $_GET["sofortlllp2"] <= $maximalstromstaerkeold) {

		$result = '';
		$lines = file('/var/www/html/openWB/openwb.conf');
		foreach($lines as $line) {
			if(strpos($line, "sofortlls1=") !== false) {
			    $result .= 'sofortlls1='.$_GET[sofortlllp2]."\n";
			}
			else {
			    $result .= $line;
			}
		}
		file_put_contents('/var/www/html/openWB/openwb.conf', $result);

	}
}
if(isset($_GET["sofortlllp3"])) {

	if($_GET["sofortlllp3"] >= $minimalstromstaerkeold && $_GET["sofortlllp3"] <= $maximalstromstaerkeold) {

		$result = '';
		$lines = file('/var/www/html/openWB/openwb.conf');
		foreach($lines as $line) {
			if(strpos($line, "sofortlls2=") !== false) {
			    $result .= 'sofortlls2='.$_GET[sofortlllp3]."\n";
			}
			else {
			    $result .= $line;
			}
		}
		file_put_contents('/var/www/html/openWB/openwb.conf', $result);

	}
}

if(isset($_GET["speicher"])) {
	if($_GET["speicher"]) {
		file_put_contents('/var/www/html/openWB/ramdisk/speicher', $_GET['speicher']);
	}
}
if(isset($_GET["get"])) {

	if($_GET["get"] == "all") {
		$json = array(
			"date"	=>	date('Y:m:d-H:i:s'),
			"lademodus"	=>	explode(PHP_EOL, file_get_contents('/var/www/html/openWB/ramdisk/lademodus'))[0],
			"minimalstromstaerke" => explode(PHP_EOL, $minimalstromstaerkeold)[0],
			"maximalstromstaerke" => explode(PHP_EOL, $maximalstromstaerkeold)[0],
			"llsoll"	=>	explode(PHP_EOL, file_get_contents('/var/www/html/openWB/ramdisk/llsoll'))[0],
			"restzeitlp1"	=>	explode(PHP_EOL, file_get_contents('/var/www/html/openWB/ramdisk/restzeitlp1'))[0],
			"restzeitlp2"	=>	explode(PHP_EOL, file_get_contents('/var/www/html/openWB/ramdisk/restzeitlp2'))[0],
			"restzeitlp3"	=>	explode(PHP_EOL, file_get_contents('/var/www/html/openWB/ramdisk/restzeitlp3'))[0],
			"gelkwhlp1"	=>      explode(PHP_EOL, file_get_contents('/var/www/html/openWB/ramdisk/aktgeladen'))[0],
			"gelkwhlp2"	=>	explode(PHP_EOL, file_get_contents('/var/www/html/openWB/ramdisk/aktgeladens1'))[0],
			"gelkwhlp3"	=>      explode(PHP_EOL, file_get_contents('/var/www/html/openWB/ramdisk/aktgeladens2'))[0],
			"gelrlp1"	=>      explode(PHP_EOL, file_get_contents('/var/www/html/openWB/ramdisk/gelrlp1'))[0],
			"gelrlp2"	=>	explode(PHP_EOL, file_get_contents('/var/www/html/openWB/ramdisk/gelrlp2'))[0],
			"gelrlp3"	=>      explode(PHP_EOL, file_get_contents('/var/www/html/openWB/ramdisk/gelrlp3'))[0],
			"llgesamt"	=>	explode(PHP_EOL, file_get_contents('/var/www/html/openWB/ramdisk/llkombiniert'))[0],
			"evua1"	=>	explode(PHP_EOL, file_get_contents('/var/www/html/openWB/ramdisk/bezuga1'))[0],
			"evua2"	=>	explode(PHP_EOL, file_get_contents('/var/www/html/openWB/ramdisk/bezuga2'))[0],
			"evua3"	=>	explode(PHP_EOL, file_get_contents('/var/www/html/openWB/ramdisk/bezuga3'))[0],
			"lllp1"	=>	explode(PHP_EOL, file_get_contents('/var/www/html/openWB/ramdisk/llaktuell'))[0],
			"lllp2"	=>	explode(PHP_EOL, file_get_contents('/var/www/html/openWB/ramdisk/llaktuells1'))[0],
			"lllp3"	=>	explode(PHP_EOL, file_get_contents('/var/www/html/openWB/ramdisk/llaktuells2'))[0],
			"evuw"	=>	explode(PHP_EOL, file_get_contents('/var/www/html/openWB/ramdisk/wattbezug'))[0],
			"pvw"	=>	explode(PHP_EOL, file_get_contents('/var/www/html/openWB/ramdisk/pvwatt'))[0],
			"evuv1"	=>	explode(PHP_EOL, file_get_contents('/var/www/html/openWB/ramdisk/evuv1'))[0],
			"evuv2"	=>	explode(PHP_EOL, file_get_contents('/var/www/html/openWB/ramdisk/evuv2'))[0],
			"evuv3"	=>	explode(PHP_EOL, file_get_contents('/var/www/html/openWB/ramdisk/evuv3'))[0],
			"ladestatusLP1"	=>	explode(PHP_EOL, file_get_contents('/var/www/html/openWB/ramdisk/ladestatus'))[0],
			"ladestatusLP2"	=>	explode(PHP_EOL, file_get_contents('/var/www/html/openWB/ramdisk/ladestatuss1'))[0],
			"ladestatusLP3"	=>	explode(PHP_EOL, file_get_contents('/var/www/html/openWB/ramdisk/ladestatuss2'))[0],
			"ladestartzeitLP1"	=>	explode(PHP_EOL, file_get_contents('/var/www/html/openWB/ramdisk/ladestart'))[0],
			"ladestartzeitLP2"	=>	explode(PHP_EOL, file_get_contents('/var/www/html/openWB/ramdisk/ladestarts1'))[0],
			"ladestartzeitLP3"	=>	explode(PHP_EOL, file_get_contents('/var/www/html/openWB/ramdisk/ladestarts2'))[0],
			"zielladungaktiv"	=>	explode(PHP_EOL, file_get_contents('/var/www/html/openWB/ramdisk/ladungdurchziel'))[0],
			"lla1LP1"	=>	explode(PHP_EOL, file_get_contents('/var/www/html/openWB/ramdisk/lla1'))[0],
			"lla2LP1"	=>	explode(PHP_EOL, file_get_contents('/var/www/html/openWB/ramdisk/lla2'))[0],
			"lla3LP1"	=>	explode(PHP_EOL, file_get_contents('/var/www/html/openWB/ramdisk/lla3'))[0],
			"lla1LP2"	=>	explode(PHP_EOL, file_get_contents('/var/www/html/openWB/ramdisk/llas11'))[0],
			"lla2LP2"	=>	explode(PHP_EOL, file_get_contents('/var/www/html/openWB/ramdisk/llas12'))[0],
			"lla3LP2"	=>	explode(PHP_EOL, file_get_contents('/var/www/html/openWB/ramdisk/llas13'))[0],
			"llkwhLP1"	=>	explode(PHP_EOL, file_get_contents('/var/www/html/openWB/ramdisk/llkwh'))[0],
			"llkwhLP2"	=>	explode(PHP_EOL, file_get_contents('/var/www/html/openWB/ramdisk/llkwhs1'))[0],
			"llkwhLP3"	=>	explode(PHP_EOL, file_get_contents('/var/www/html/openWB/ramdisk/llkwhs2'))[0],
			"evubezugWh"	=>	explode(PHP_EOL, file_get_contents('/var/www/html/openWB/ramdisk/bezugkwh'))[0],
			"evueinspeisungWh"	=>	explode(PHP_EOL, file_get_contents('/var/www/html/openWB/ramdisk/einspeisungkwh'))[0],
			"pvWh"	=>	explode(PHP_EOL, file_get_contents('/var/www/html/openWB/ramdisk/pvkwh'))[0],
			"speichersoc"	=>	explode(PHP_EOL, file_get_contents('/var/www/html/openWB/ramdisk/speichersoc'))[0],
			"socLP1"	=>	explode(PHP_EOL, file_get_contents('/var/www/html/openWB/ramdisk/soc'))[0],
			"socLP2"	=>	explode(PHP_EOL, file_get_contents('/var/www/html/openWB/ramdisk/soc1'))[0],
			"speicherleistung"	=>	explode(PHP_EOL, file_get_contents('/var/www/html/openWB/ramdisk/speicherleistung'))[0]
		);
		echo json_encode($json);
	}
}



?>
