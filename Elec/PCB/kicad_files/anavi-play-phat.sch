EESchema Schematic File Version 4
LIBS:anavi-play-phat-cache
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L anavi-play-phat-rescue:GND-power #PWR05
U 1 1 56FD1B71
P 3450 3450
F 0 "#PWR05" H 3450 3200 50  0001 C CNN
F 1 "GND" H 3450 3300 50  0000 C CNN
F 2 "" H 3450 3450 50  0000 C CNN
F 3 "" H 3450 3450 50  0000 C CNN
	1    3450 3450
	1    0    0    -1  
$EndComp
$Comp
L anavi-play-phat-rescue:+3.3V-power #PWR06
U 1 1 56FD2267
P 3450 2150
F 0 "#PWR06" H 3450 2000 50  0001 C CNN
F 1 "+3.3V" H 3450 2290 50  0000 C CNN
F 2 "" H 3450 2150 50  0000 C CNN
F 3 "" H 3450 2150 50  0000 C CNN
	1    3450 2150
	1    0    0    -1  
$EndComp
$Comp
L anavi-play-phat-rescue:+5V-power #PWR07
U 1 1 56FF1D94
P 3450 1800
F 0 "#PWR07" H 3450 1650 50  0001 C CNN
F 1 "+5V" H 3450 1940 50  0000 C CNN
F 2 "" H 3450 1800 50  0000 C CNN
F 3 "" H 3450 1800 50  0000 C CNN
	1    3450 1800
	1    0    0    -1  
$EndComp
NoConn ~ 5350 4850
NoConn ~ 5350 4750
NoConn ~ 5350 4650
NoConn ~ 5350 3750
NoConn ~ 5350 2900
NoConn ~ 5350 3000
NoConn ~ 5350 4150
NoConn ~ 5350 3850
NoConn ~ 5350 2600
NoConn ~ 5350 2700
$Comp
L anavi-play-phat-rescue:GND-power #PWR016
U 1 1 5B2D1552
P 7600 5300
F 0 "#PWR016" H 7600 5050 50  0001 C CNN
F 1 "GND" H 7600 5150 50  0000 C CNN
F 2 "" H 7600 5300 50  0001 C CNN
F 3 "" H 7600 5300 50  0001 C CNN
	1    7600 5300
	0    -1   -1   0   
$EndComp
NoConn ~ 5350 2800
Wire Wire Line
	3450 2150 3450 2250
Wire Wire Line
	3450 1800 3450 1900
NoConn ~ 5350 2200
NoConn ~ 5350 2300
$Comp
L anavi-play-phat-rescue:+3.3V-power #PWR0101
U 1 1 5DCF6D0C
P 6250 2000
F 0 "#PWR0101" H 6250 1850 50  0001 C CNN
F 1 "+3.3V" H 6250 2140 50  0000 C CNN
F 2 "" H 6250 2000 50  0000 C CNN
F 3 "" H 6250 2000 50  0000 C CNN
	1    6250 2000
	0    -1   -1   0   
$EndComp
$Comp
L anavi-play-phat-rescue:GND-power #PWR0102
U 1 1 5DCF6D1A
P 6250 2100
F 0 "#PWR0102" H 6250 1850 50  0001 C CNN
F 1 "GND-power" H 6255 1927 50  0000 C CNN
F 2 "" H 6250 2100 50  0001 C CNN
F 3 "" H 6250 2100 50  0001 C CNN
	1    6250 2100
	1    0    0    -1  
$EndComp
Wire Wire Line
	6250 2000 6550 2000
Wire Wire Line
	6250 2100 6550 2100
Wire Wire Line
	5350 1800 6550 1800
Wire Wire Line
	5350 1900 6550 1900
$Comp
L screen:i2c_screen i2c_scr1
U 1 1 5DCC6113
P 6500 2200
F 0 "i2c_scr1" H 7129 2865 50  0000 C CNN
F 1 "i2c_screen" H 7129 2774 50  0000 C CNN
F 2 "i2c_screen:i2c_screen" H 6900 2500 50  0001 C CNN
F 3 "" H 6900 2500 50  0001 C CNN
	1    6500 2200
	1    0    0    -1  
$EndComp
$Comp
L boutton:boutton_5mx6m SW_L1
U 1 1 5DCB9911
P 7150 4150
F 0 "SW_L1" H 7025 4323 50  0000 C CNN
F 1 "boutton_5mx6m" H 7025 4324 50  0001 C CNN
F 2 "boutton:boutton" H 7025 4323 50  0001 C CNN
F 3 "" H 7150 4050 50  0001 C CNN
	1    7150 4150
	1    0    0    -1  
$EndComp
$Comp
L boutton:boutton_5mx6m SW_UP1
U 1 1 5DCBCA4E
P 7150 3800
F 0 "SW_UP1" H 7025 3973 50  0000 C CNN
F 1 "boutton_5mx6m" H 7025 3974 50  0001 C CNN
F 2 "boutton:boutton" H 7025 3973 50  0001 C CNN
F 3 "" H 7150 3700 50  0001 C CNN
	1    7150 3800
	1    0    0    -1  
$EndComp
$Comp
L boutton:boutton_5mx6m SW_OK1
U 1 1 5DCD09F9
P 7150 5300
F 0 "SW_OK1" H 7025 5473 50  0000 C CNN
F 1 "boutton_5mx6m" H 7025 5474 50  0001 C CNN
F 2 "boutton:boutton" H 7025 5473 50  0001 C CNN
F 3 "" H 7150 5200 50  0001 C CNN
	1    7150 5300
	1    0    0    -1  
$EndComp
$Comp
L boutton:boutton_5mx6m SW_DNW1
U 1 1 5DCD1F59
P 7150 4550
F 0 "SW_DNW1" H 7025 4723 50  0000 C CNN
F 1 "boutton_5mx6m" H 7025 4724 50  0001 C CNN
F 2 "boutton:boutton" H 7025 4723 50  0001 C CNN
F 3 "" H 7150 4450 50  0001 C CNN
	1    7150 4550
	1    0    0    -1  
$EndComp
$Comp
L boutton:boutton_5mx6m SW_R1
U 1 1 5DCD6AE5
P 7150 4900
F 0 "SW_R1" H 7025 5073 50  0000 C CNN
F 1 "boutton_5mx6m" H 7025 5074 50  0001 C CNN
F 2 "boutton:boutton" H 7025 5073 50  0001 C CNN
F 3 "" H 7150 4800 50  0001 C CNN
	1    7150 4900
	1    0    0    -1  
$EndComp
Wire Wire Line
	3450 3350 3450 3450
Connection ~ 3450 3350
Connection ~ 3450 3050
Wire Wire Line
	3450 3250 3450 3350
Connection ~ 3450 3250
Connection ~ 3450 2850
Wire Wire Line
	3450 3150 3450 3250
Wire Wire Line
	3450 3050 3450 3150
Connection ~ 3450 3150
Wire Wire Line
	3450 2950 3450 3050
Wire Wire Line
	3450 2850 3450 2950
Connection ~ 3450 2950
Wire Wire Line
	3450 2750 3450 2850
Wire Wire Line
	3450 2650 3450 2750
Connection ~ 3450 2750
Connection ~ 3450 1800
Connection ~ 3450 2150
$Comp
L mylibrary:Raspberry_PI RASP_CONN1
U 1 1 56FB7C7A
P 4400 1700
F 0 "RASP_CONN1" H 3900 1750 60  0001 C CNN
F 1 "Raspberry_PI" H 4800 1750 60  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_2x20" H 4350 -1800 60  0001 C CNN
F 3 "" H 4400 1700 60  0000 C CNN
	1    4400 1700
	1    0    0    -1  
$EndComp
Wire Wire Line
	5350 3950 5950 3950
Wire Wire Line
	5950 3950 5950 3800
Wire Wire Line
	5950 3800 6900 3800
Wire Wire Line
	5350 4250 6100 4250
Wire Wire Line
	6100 4250 6100 4150
Wire Wire Line
	6100 4150 6900 4150
Wire Wire Line
	5350 4950 5850 4950
Wire Wire Line
	5850 4950 5850 5300
Wire Wire Line
	5850 5300 6900 5300
Wire Wire Line
	5350 4350 6250 4350
Wire Wire Line
	6250 4350 6250 4550
Wire Wire Line
	6250 4550 6900 4550
Wire Wire Line
	5350 4450 6000 4450
Wire Wire Line
	6000 4450 6000 4900
Wire Wire Line
	6000 4900 6900 4900
Wire Wire Line
	7150 3800 7350 3800
Wire Wire Line
	7350 3800 7350 4150
Wire Wire Line
	7350 5300 7600 5300
Wire Wire Line
	7150 5300 7350 5300
Connection ~ 7350 5300
Wire Wire Line
	7150 4900 7350 4900
Connection ~ 7350 4900
Wire Wire Line
	7350 4900 7350 5300
Wire Wire Line
	7150 4550 7350 4550
Connection ~ 7350 4550
Wire Wire Line
	7350 4550 7350 4900
Wire Wire Line
	7150 4150 7350 4150
Connection ~ 7350 4150
Wire Wire Line
	7350 4150 7350 4550
NoConn ~ 5350 4050
NoConn ~ 5350 4550
NoConn ~ 5350 3450
NoConn ~ 5350 3550
NoConn ~ 5350 3650
NoConn ~ 3450 3700
NoConn ~ 3450 3800
$Comp
L boutton:boutton_5mx6m SW_BCK1
U 1 1 5DCC3420
P 7150 5650
F 0 "SW_BCK1" H 7025 5823 50  0000 C CNN
F 1 "boutton_5mx6m" H 7025 5824 50  0001 C CNN
F 2 "boutton:boutton" H 7025 5823 50  0001 C CNN
F 3 "" H 7150 5550 50  0001 C CNN
	1    7150 5650
	1    0    0    -1  
$EndComp
Wire Wire Line
	7150 5650 7350 5650
Wire Wire Line
	7350 5650 7350 5300
Wire Wire Line
	5350 5050 5700 5050
Wire Wire Line
	5700 5050 5700 5650
Wire Wire Line
	5700 5650 6900 5650
$EndSCHEMATC
