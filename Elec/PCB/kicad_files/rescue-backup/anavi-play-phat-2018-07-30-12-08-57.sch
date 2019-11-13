EESchema Schematic File Version 2
LIBS:power
LIBS:device
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
LIBS:mylibrary
LIBS:w_connectors
LIBS:switches
LIBS:anavi-play-phat-cache
EELAYER 25 0
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
L CAT24C32WI-GT3 U1
U 1 1 56FB5761
P 1500 3300
F 0 "U1" H 1250 3250 60  0000 C CNN
F 1 "CAT24C32WI-GT3" H 1500 2650 60  0000 C CNN
F 2 "Housings_DIP:DIP-8_W7.62mm" H 1500 2550 60  0001 C CNN
F 3 "" H 1500 3300 60  0000 C CNN
	1    1500 3300
	1    0    0    -1  
$EndComp
$Comp
L R R1
U 1 1 56FB57DD
P 2650 3350
F 0 "R1" H 2600 3500 50  0000 C CNN
F 1 "1K" V 2650 3350 50  0000 C CNN
F 2 "Resistors_SMD:R_0603_HandSoldering" V 2580 3350 50  0001 C CNN
F 3 "" H 2650 3350 50  0000 C CNN
	1    2650 3350
	1    0    0    -1  
$EndComp
$Comp
L R R2
U 1 1 56FB589D
P 2800 3350
F 0 "R2" H 2750 3500 50  0000 C CNN
F 1 "4.7K" V 2800 3350 50  0000 C CNN
F 2 "Resistors_SMD:R_0603_HandSoldering" V 2730 3350 50  0001 C CNN
F 3 "" H 2800 3350 50  0000 C CNN
	1    2800 3350
	1    0    0    -1  
$EndComp
$Comp
L R R3
U 1 1 56FB5912
P 2950 3350
F 0 "R3" H 2900 3500 50  0000 C CNN
F 1 "4.7K" V 2950 3350 50  0000 C CNN
F 2 "Resistors_SMD:R_0603_HandSoldering" V 2880 3350 50  0001 C CNN
F 3 "" H 2950 3350 50  0000 C CNN
	1    2950 3350
	1    0    0    -1  
$EndComp
$Comp
L C C1
U 1 1 56FB5967
P 2050 3050
F 0 "C1" V 2200 3000 50  0000 L CNN
F 1 "0.1" V 1900 3000 50  0000 L CNN
F 2 "Capacitors_SMD:C_0603_HandSoldering" H 2088 2900 50  0001 C CNN
F 3 "" H 2050 3050 50  0000 C CNN
	1    2050 3050
	0    1    1    0   
$EndComp
$Comp
L GND #PWR01
U 1 1 56FB5AA8
P 800 3950
F 0 "#PWR01" H 800 3700 50  0001 C CNN
F 1 "GND" H 800 3800 50  0000 C CNN
F 2 "" H 800 3950 50  0000 C CNN
F 3 "" H 800 3950 50  0000 C CNN
	1    800  3950
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR02
U 1 1 56FB5B93
P 1900 3050
F 0 "#PWR02" H 1900 2800 50  0001 C CNN
F 1 "GND" H 1900 2900 50  0000 C CNN
F 2 "" H 1900 3050 50  0000 C CNN
F 3 "" H 1900 3050 50  0000 C CNN
	1    1900 3050
	0    1    1    0   
$EndComp
$Comp
L +3.3V #PWR03
U 1 1 56FB5F37
P 2200 2700
F 0 "#PWR03" H 2200 2550 50  0001 C CNN
F 1 "+3.3V" H 2200 2840 50  0000 C CNN
F 2 "" H 2200 2700 50  0000 C CNN
F 3 "" H 2200 2700 50  0000 C CNN
	1    2200 2700
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR04
U 1 1 56FB60BD
P 2650 4650
F 0 "#PWR04" H 2650 4400 50  0001 C CNN
F 1 "GND" H 2650 4500 50  0000 C CNN
F 2 "" H 2650 4650 50  0000 C CNN
F 3 "" H 2650 4650 50  0000 C CNN
	1    2650 4650
	1    0    0    -1  
$EndComp
$Comp
L Raspberry_PI RASP_CONN1
U 1 1 56FB7C7A
P 4400 1700
F 0 "RASP_CONN1" H 3900 1750 60  0001 C CNN
F 1 "Raspberry_PI" H 4800 1750 60  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_2x20" H 4350 -1800 60  0001 C CNN
F 3 "" H 4400 1700 60  0000 C CNN
	1    4400 1700
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR05
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
L +3.3V #PWR06
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
L +5V #PWR07
U 1 1 56FF1D94
P 3450 1800
F 0 "#PWR07" H 3450 1650 50  0001 C CNN
F 1 "+5V" H 3450 1940 50  0000 C CNN
F 2 "" H 3450 1800 50  0000 C CNN
F 3 "" H 3450 1800 50  0000 C CNN
	1    3450 1800
	1    0    0    -1  
$EndComp
$Comp
L I2C_SENS_1 SENS1
U 1 1 5704A9C3
P 7200 1700
F 0 "SENS1" H 7300 1800 60  0000 C CNN
F 1 "I2C_SENS_1" H 7450 1700 60  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_1x04" H 7200 1700 60  0001 C CNN
F 3 "" H 7200 1700 60  0000 C CNN
	1    7200 1700
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR08
U 1 1 5704B80C
P 8050 2100
F 0 "#PWR08" H 8050 1850 50  0001 C CNN
F 1 "GND" H 8050 1950 50  0000 C CNN
F 2 "" H 8050 2100 50  0000 C CNN
F 3 "" H 8050 2100 50  0000 C CNN
	1    8050 2100
	1    0    0    -1  
$EndComp
$Comp
L +3.3V #PWR09
U 1 1 5704BA43
P 7900 700
F 0 "#PWR09" H 7900 550 50  0001 C CNN
F 1 "+3.3V" H 7900 840 50  0000 C CNN
F 2 "" H 7900 700 50  0000 C CNN
F 3 "" H 7900 700 50  0000 C CNN
	1    7900 700 
	1    0    0    -1  
$EndComp
$Comp
L R R4
U 1 1 570C0762
P 6200 900
F 0 "R4" H 6150 750 50  0000 C CNN
F 1 "4.7K" V 6200 900 50  0000 C CNN
F 2 "Resistors_SMD:R_0603_HandSoldering" V 6130 900 50  0001 C CNN
F 3 "" H 6200 900 50  0000 C CNN
	1    6200 900 
	1    0    0    -1  
$EndComp
$Comp
L R R5
U 1 1 570C0BD5
P 6350 900
F 0 "R5" H 6450 750 50  0000 C CNN
F 1 "4.7K" V 6350 900 50  0000 C CNN
F 2 "Resistors_SMD:R_0603_HandSoldering" V 6280 900 50  0001 C CNN
F 3 "" H 6350 900 50  0000 C CNN
	1    6350 900 
	1    0    0    -1  
$EndComp
$Comp
L JUMPER JP1
U 1 1 570C5478
P 2650 4350
F 0 "JP1" V 2650 4550 50  0000 C CNN
F 1 "JUMPER" V 2650 4200 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_1x02" H 2650 4350 50  0001 C CNN
F 3 "" H 2650 4350 50  0000 C CNN
	1    2650 4350
	0    1    1    0   
$EndComp
$Comp
L I2C_SENS_1 SENS2
U 1 1 5752A123
P 7200 1100
F 0 "SENS2" H 7300 1200 60  0000 C CNN
F 1 "I2C_SENS_1" H 7450 1100 60  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_1x04" H 7200 1100 60  0001 C CNN
F 3 "" H 7200 1100 60  0000 C CNN
	1    7200 1100
	1    0    0    -1  
$EndComp
$Comp
L I2C_SENS_1 SENS3
U 1 1 5752A2F7
P 7200 700
F 0 "SENS3" H 7300 800 60  0000 C CNN
F 1 "I2C_SENS_1" H 7450 700 60  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_1x04" H 7200 700 60  0001 C CNN
F 3 "" H 7200 700 60  0000 C CNN
	1    7200 700 
	1    0    0    -1  
$EndComp
$Comp
L +3.3V #PWR012
U 1 1 5752AF07
P 6050 750
F 0 "#PWR012" H 6050 600 50  0001 C CNN
F 1 "+3.3V" H 6050 890 50  0000 C CNN
F 2 "" H 6050 750 50  0000 C CNN
F 3 "" H 6050 750 50  0000 C CNN
	1    6050 750 
	0    -1   -1   0   
$EndComp
NoConn ~ 5350 4950
NoConn ~ 5350 4850
NoConn ~ 5350 4750
NoConn ~ 5350 4650
NoConn ~ 5350 4450
NoConn ~ 5350 3750
NoConn ~ 5350 3950
NoConn ~ 5350 2900
NoConn ~ 5350 3000
NoConn ~ 5350 4150
NoConn ~ 5350 3850
$Comp
L SW_DIP_x01 SW3
U 1 1 5B2D06D5
P 6450 4550
F 0 "SW3" H 6450 4700 50  0000 C CNN
F 1 "SW_DIP_x01" H 6450 4400 50  0000 C CNN
F 2 "Buttons_Switches_ThroughHole:SW_PUSH_6mm_h4.3mm" H 6450 4550 50  0001 C CNN
F 3 "" H 6450 4550 50  0001 C CNN
	1    6450 4550
	1    0    0    -1  
$EndComp
$Comp
L SW_DIP_x01 SW4
U 1 1 5B2D074E
P 6450 5050
F 0 "SW4" H 6450 5200 50  0000 C CNN
F 1 "SW_DIP_x01" H 6450 4900 50  0000 C CNN
F 2 "Buttons_Switches_ThroughHole:SW_PUSH_6mm_h4.3mm" H 6450 5050 50  0001 C CNN
F 3 "" H 6450 5050 50  0001 C CNN
	1    6450 5050
	1    0    0    -1  
$EndComp
$Comp
L SW_DIP_x01 SW2
U 1 1 5B2D07DD
P 6450 4050
F 0 "SW2" H 6450 4200 50  0000 C CNN
F 1 "SW_DIP_x01" H 6450 3900 50  0000 C CNN
F 2 "Buttons_Switches_ThroughHole:SW_PUSH_6mm_h4.3mm" H 6450 4050 50  0001 C CNN
F 3 "" H 6450 4050 50  0001 C CNN
	1    6450 4050
	1    0    0    -1  
$EndComp
$Comp
L SW_DIP_x01 SW1
U 1 1 5B2D0866
P 6450 3150
F 0 "SW1" H 6450 3300 50  0000 C CNN
F 1 "SW_DIP_x01" H 6450 3000 50  0000 C CNN
F 2 "Buttons_Switches_ThroughHole:SW_PUSH_6mm_h4.3mm" H 6450 3150 50  0001 C CNN
F 3 "" H 6450 3150 50  0001 C CNN
	1    6450 3150
	1    0    0    -1  
$EndComp
$Comp
L SW_DIP_x01 SW5
U 1 1 5B2D08D5
P 7900 4250
F 0 "SW5" H 7900 4400 50  0000 C CNN
F 1 "SW_DIP_x01" H 7900 4100 50  0000 C CNN
F 2 "Buttons_Switches_ThroughHole:SW_PUSH_6mm_h4.3mm" H 7900 4250 50  0001 C CNN
F 3 "" H 7900 4250 50  0001 C CNN
	1    7900 4250
	1    0    0    -1  
$EndComp
$Comp
L SW_DIP_x01 SW6
U 1 1 5B2D093A
P 7900 4850
F 0 "SW6" H 7900 5000 50  0000 C CNN
F 1 "SW_DIP_x01" H 7900 4700 50  0000 C CNN
F 2 "Buttons_Switches_ThroughHole:SW_PUSH_6mm_h4.3mm" H 7900 4850 50  0001 C CNN
F 3 "" H 7900 4850 50  0001 C CNN
	1    7900 4850
	1    0    0    -1  
$EndComp
$Comp
L SW_DIP_x01 SW7
U 1 1 5B2D09C5
P 9050 3550
F 0 "SW7" H 9050 3700 50  0000 C CNN
F 1 "SW_DIP_x01" H 9050 3400 50  0000 C CNN
F 2 "switches:SW_PUSH_6mm_h4.3mm" H 9050 3550 50  0001 C CNN
F 3 "" H 9050 3550 50  0001 C CNN
	1    9050 3550
	1    0    0    -1  
$EndComp
$Comp
L SW_DIP_x01 SW8
U 1 1 5B2D0A20
P 9050 4000
F 0 "SW8" H 9050 4150 50  0000 C CNN
F 1 "SW_DIP_x01" H 9050 3850 50  0000 C CNN
F 2 "switches:SW_PUSH_6mm_h4.3mm" H 9050 4000 50  0001 C CNN
F 3 "" H 9050 4000 50  0001 C CNN
	1    9050 4000
	1    0    0    -1  
$EndComp
NoConn ~ 5350 2600
NoConn ~ 5350 2700
$Comp
L GND #PWR013
U 1 1 5B2D114F
P 6750 4550
F 0 "#PWR013" H 6750 4300 50  0001 C CNN
F 1 "GND" H 6750 4400 50  0000 C CNN
F 2 "" H 6750 4550 50  0001 C CNN
F 3 "" H 6750 4550 50  0001 C CNN
	1    6750 4550
	0    -1   -1   0   
$EndComp
$Comp
L GND #PWR014
U 1 1 5B2D13B3
P 6750 3150
F 0 "#PWR014" H 6750 2900 50  0001 C CNN
F 1 "GND" H 6750 3000 50  0000 C CNN
F 2 "" H 6750 3150 50  0001 C CNN
F 3 "" H 6750 3150 50  0001 C CNN
	1    6750 3150
	0    -1   -1   0   
$EndComp
$Comp
L GND #PWR015
U 1 1 5B2D1516
P 6750 4050
F 0 "#PWR015" H 6750 3800 50  0001 C CNN
F 1 "GND" H 6750 3900 50  0000 C CNN
F 2 "" H 6750 4050 50  0001 C CNN
F 3 "" H 6750 4050 50  0001 C CNN
	1    6750 4050
	0    -1   -1   0   
$EndComp
$Comp
L GND #PWR016
U 1 1 5B2D1552
P 6750 5050
F 0 "#PWR016" H 6750 4800 50  0001 C CNN
F 1 "GND" H 6750 4900 50  0000 C CNN
F 2 "" H 6750 5050 50  0001 C CNN
F 3 "" H 6750 5050 50  0001 C CNN
	1    6750 5050
	0    -1   -1   0   
$EndComp
$Comp
L GND #PWR017
U 1 1 5B2D271F
P 8200 4850
F 0 "#PWR017" H 8200 4600 50  0001 C CNN
F 1 "GND" H 8200 4700 50  0000 C CNN
F 2 "" H 8200 4850 50  0001 C CNN
F 3 "" H 8200 4850 50  0001 C CNN
	1    8200 4850
	0    -1   -1   0   
$EndComp
$Comp
L GND #PWR018
U 1 1 5B2D275B
P 9350 3550
F 0 "#PWR018" H 9350 3300 50  0001 C CNN
F 1 "GND" H 9350 3400 50  0000 C CNN
F 2 "" H 9350 3550 50  0001 C CNN
F 3 "" H 9350 3550 50  0001 C CNN
	1    9350 3550
	0    -1   -1   0   
$EndComp
$Comp
L GND #PWR019
U 1 1 5B2D27DC
P 9350 4000
F 0 "#PWR019" H 9350 3750 50  0001 C CNN
F 1 "GND" H 9350 3850 50  0000 C CNN
F 2 "" H 9350 4000 50  0001 C CNN
F 3 "" H 9350 4000 50  0001 C CNN
	1    9350 4000
	0    -1   -1   0   
$EndComp
NoConn ~ 5350 2800
Wire Wire Line
	950  3500 800  3500
Wire Wire Line
	800  3500 800  3950
Wire Wire Line
	950  3600 800  3600
Connection ~ 800  3600
Wire Wire Line
	950  3700 800  3700
Connection ~ 800  3700
Wire Wire Line
	950  3800 800  3800
Connection ~ 800  3800
Wire Wire Line
	2200 3500 2050 3500
Connection ~ 2200 3050
Wire Wire Line
	2950 3050 2950 3200
Wire Wire Line
	2800 3050 2800 3200
Connection ~ 2800 3050
Wire Wire Line
	2650 3200 2650 3050
Connection ~ 2650 3050
Wire Wire Line
	2200 3050 2950 3050
Wire Wire Line
	2050 3600 2650 3600
Wire Wire Line
	2650 3500 2650 4050
Wire Wire Line
	2800 3700 2800 3500
Wire Wire Line
	2950 3800 2950 3500
Connection ~ 2950 3800
Connection ~ 2800 3700
Wire Wire Line
	2200 2700 2200 3500
Connection ~ 2650 3600
Wire Wire Line
	3450 2150 3450 2250
Connection ~ 3450 2150
Connection ~ 3450 1800
Wire Wire Line
	3450 1800 3450 1900
Wire Wire Line
	5350 1800 7000 1800
Wire Wire Line
	5350 1900 7000 1900
Connection ~ 6650 1800
Connection ~ 6800 1900
Wire Wire Line
	8050 900  8050 2100
Wire Wire Line
	8050 1900 7900 1900
Connection ~ 7900 1800
Wire Wire Line
	2050 3700 3450 3700
Wire Wire Line
	2050 3800 3450 3800
Connection ~ 7900 1200
Connection ~ 7900 800 
Wire Wire Line
	7900 900  8050 900 
Wire Wire Line
	8050 1300 7900 1300
Connection ~ 8050 1900
Connection ~ 8050 1300
Wire Wire Line
	7000 800  6650 800 
Wire Wire Line
	6200 1200 7000 1200
Connection ~ 6650 1200
Wire Wire Line
	7000 900  6800 900 
Wire Wire Line
	6350 1300 7000 1300
Connection ~ 6800 1300
Wire Wire Line
	6350 1050 6350 1300
Wire Wire Line
	6200 1050 6200 1200
Wire Wire Line
	6050 750  6350 750 
Connection ~ 6200 750 
Wire Wire Line
	6800 900  6800 1900
Wire Wire Line
	6650 800  6650 1800
Wire Wire Line
	7900 700  7900 1800
Wire Wire Line
	3450 2650 3450 3450
Connection ~ 3450 2750
Connection ~ 3450 2850
Connection ~ 3450 2950
Connection ~ 3450 3050
Connection ~ 3450 3150
Connection ~ 3450 3350
Connection ~ 3450 3250
Wire Wire Line
	5350 4050 6150 4050
Wire Wire Line
	5350 5050 6150 5050
Wire Wire Line
	5350 4350 7600 4350
Wire Wire Line
	7600 4350 7600 4850
Wire Wire Line
	5350 3650 8750 3650
Wire Wire Line
	8750 3650 8750 4000
Wire Wire Line
	8750 3550 5350 3550
Wire Wire Line
	6150 4550 5350 4550
Wire Wire Line
	5350 3450 6150 3450
Wire Wire Line
	6150 3450 6150 3150
Wire Wire Line
	5350 4250 7600 4250
$Comp
L GND #PWR020
U 1 1 5B2D2E88
P 8200 4250
F 0 "#PWR020" H 8200 4000 50  0001 C CNN
F 1 "GND" H 8200 4100 50  0000 C CNN
F 2 "" H 8200 4250 50  0001 C CNN
F 3 "" H 8200 4250 50  0001 C CNN
	1    8200 4250
	0    -1   -1   0   
$EndComp
NoConn ~ 5350 2200
NoConn ~ 5350 2300
$EndSCHEMATC