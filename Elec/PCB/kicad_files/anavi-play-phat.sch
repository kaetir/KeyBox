EESchema Schematic File Version 4
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
NoConn ~ 5350 3750
NoConn ~ 5350 2900
NoConn ~ 5350 3000
NoConn ~ 5350 3850
NoConn ~ 5350 2600
NoConn ~ 5350 2700
$Comp
L anavi-play-phat-rescue:GND-power #PWR016
U 1 1 5B2D1552
P 6350 3700
F 0 "#PWR016" H 6350 3450 50  0001 C CNN
F 1 "GND" H 6350 3550 50  0000 C CNN
F 2 "" H 6350 3700 50  0001 C CNN
F 3 "" H 6350 3700 50  0001 C CNN
	1    6350 3700
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
NoConn ~ 5350 3550
NoConn ~ 5350 3650
NoConn ~ 3450 3700
NoConn ~ 3450 3800
Wire Wire Line
	6350 3450 6350 3700
$Comp
L boutton:boutton_6mx6m UP1
U 1 1 5DE76847
P 6350 4050
F 0 "UP1" H 6225 4223 50  0000 C CNN
F 1 "boutton_6mx6m" H 6200 3900 50  0001 C CNN
F 2 "boutton:boutton__6mx6m" H 6350 3950 50  0001 C CNN
F 3 "" H 6350 3950 50  0001 C CNN
	1    6350 4050
	1    0    0    -1  
$EndComp
$Comp
L boutton:boutton_6mx6m L1
U 1 1 5DE77762
P 6350 5050
F 0 "L1" H 6225 5223 50  0000 C CNN
F 1 "boutton_6mx6m" H 6200 4900 50  0001 C CNN
F 2 "boutton:boutton__6mx6m" H 6350 4950 50  0001 C CNN
F 3 "" H 6350 4950 50  0001 C CNN
	1    6350 5050
	1    0    0    -1  
$EndComp
$Comp
L boutton:boutton_6mx6m OK1
U 1 1 5DE79BAE
P 6350 4550
F 0 "OK1" H 6225 4723 50  0000 C CNN
F 1 "boutton_6mx6m" H 6200 4400 50  0001 C CNN
F 2 "boutton:boutton__6mx6m" H 6350 4450 50  0001 C CNN
F 3 "" H 6350 4450 50  0001 C CNN
	1    6350 4550
	1    0    0    -1  
$EndComp
$Comp
L boutton:boutton_6mx6m R1
U 1 1 5DE7B850
P 6350 3450
F 0 "R1" H 6225 3623 50  0000 C CNN
F 1 "boutton_6mx6m" H 6200 3300 50  0001 C CNN
F 2 "boutton:boutton__6mx6m" H 6350 3350 50  0001 C CNN
F 3 "" H 6350 3350 50  0001 C CNN
	1    6350 3450
	1    0    0    -1  
$EndComp
$Comp
L boutton:boutton_6mx6m DWN1
U 1 1 5DE7C4F2
P 6350 4300
F 0 "DWN1" H 6225 4473 50  0000 C CNN
F 1 "boutton_6mx6m" H 6200 4150 50  0001 C CNN
F 2 "boutton:boutton__6mx6m" H 6350 4200 50  0001 C CNN
F 3 "" H 6350 4200 50  0001 C CNN
	1    6350 4300
	1    0    0    -1  
$EndComp
$Comp
L boutton:boutton_6mx6m BCK1
U 1 1 5DE7DEC3
P 6350 4800
F 0 "BCK1" H 6225 4973 50  0000 C CNN
F 1 "boutton_6mx6m" H 6200 4650 50  0001 C CNN
F 2 "boutton:boutton__6mx6m" H 6350 4700 50  0001 C CNN
F 3 "" H 6350 4700 50  0001 C CNN
	1    6350 4800
	1    0    0    -1  
$EndComp
Wire Wire Line
	5350 3450 6100 3450
Wire Wire Line
	5350 4050 6100 4050
Wire Wire Line
	5350 4150 5700 4150
Wire Wire Line
	5700 4150 5700 4300
Wire Wire Line
	5700 4300 6100 4300
Wire Wire Line
	5350 4550 6100 4550
Wire Wire Line
	5350 4650 5650 4650
Wire Wire Line
	5650 4650 5650 4800
Wire Wire Line
	5650 4800 6100 4800
Wire Wire Line
	5350 5050 6100 5050
Connection ~ 6350 4050
Wire Wire Line
	6350 4050 6350 4300
Connection ~ 6350 4300
Wire Wire Line
	6350 4300 6350 4550
Connection ~ 6350 4550
Wire Wire Line
	6350 4550 6350 4800
Connection ~ 6350 4800
Wire Wire Line
	6350 4800 6350 5050
Connection ~ 6350 3700
Wire Wire Line
	6350 3700 6350 4050
$Comp
L w_connectors:HEADER_2 J1
U 1 1 5DF274FA
P 8450 2650
F 0 "J1" H 8578 2756 60  0000 L CNN
F 1 "USB Data" H 8578 2650 60  0000 L CNN
F 2 "w_conn_misc:header 2m spaced" H 8578 2544 60  0000 L CNN
F 3 "" H 8450 2650 60  0000 C CNN
	1    8450 2650
	1    0    0    -1  
$EndComp
$Comp
L w_connectors:HEADER_2 J2
U 1 1 5DF290D8
P 8450 3000
F 0 "J2" H 8578 3106 60  0000 L CNN
F 1 "USB power" H 8578 3000 60  0000 L CNN
F 2 "w_conn_misc:header 2m spaced" H 8578 2894 60  0000 L CNN
F 3 "" H 8450 3000 60  0000 C CNN
	1    8450 3000
	1    0    0    -1  
$EndComp
$EndSCHEMATC
