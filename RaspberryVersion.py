#!/usr/bin/python3

# Version 0.11 by TF tommy@binbash.de

import subprocess

getdata = subprocess.run(["cat /proc/cpuinfo | grep Revision"], shell=True, stdout=subprocess.PIPE)
tempdata = str(getdata.stdout).split(': ')
revcode = tempdata[1].split('\\n\'')[0]

if revcode == '0002':
	print('Raspberry Pi B - 256MB RAM - 100MBit LAN - Rev 1.0 Manufactured by Egoman')
elif revcode == '0003':
	print('Raspberry Pi B - 256MB RAM - 100MBit LAN - Rev 1.0 Manufactured by Egoman')
elif revcode == '0004':
	print('Raspberry Pi B - 256MB RAM - 100MBit LAN - Rev 1.0 Manufactured by Sony UK')
elif revcode == '0005':
        print('Raspberry Pi B - 256MB RAM - 100MBit LAN - Rev 2.0 Manufactured by Qisda')
elif revcode == '0006':
        print('Raspberry Pi B - 256MB RAM - 100MBit LAN -  Rev 2.0 Manufactured by Egoman')
elif revcode == '0007':
        print('Raspberry Pi A - 256MB RAM - Rev 2.0 Manufactured by Egoman')
elif revcode == '0008':
        print('Raspberry Pi A - 256MB RAM - Rev 2.0 Manufactured by Sony UK')
elif revcode == '0009':
        print('Raspberry Pi A - 256MB RAM - Rev 2.0 Manufactured by Qisda')
elif revcode == '000d':
        print('Raspberry Pi B - 512MB RAM - 100MBit LAN - Rev 2.0 Manufactured by Egoman')
elif revcode == '000e':
        print('Raspberry Pi B - 512MB RAM - 100MBit LAN - Rev 2.0 Manufactured by Sony UK')
elif revcode == '000f':
        print('Raspberry Pi B - 512MB RAM - 100MBit LAN - Rev 2.0 Manufactured by Egoman')
elif revcode == '0010':
        print('Raspberry Pi B+ - 512MB RAM - 100MBit LAN - Rev 1.2 Manufactured by Sony UK')
elif revcode == '0011':
        print('Raspberry Pi CM1 - 512MB RAM - Rev 1.0 Manufactured by Sony UK')
elif revcode == '0012':
        print('Raspberry Pi A+ - 256MB RAM - Rev 1.1 Manufactured by Sony UK')
elif revcode == '0013':
        print('Raspberry Pi B+ - 512MB RAM - 100MBit LAN - Rev 1.2 Manufactured by Embest')
elif revcode == '0014':
        print('Raspberry Pi CM1 - 512MB RAM - Rev 1.0 Manufactured by Embest')
elif revcode == '0015':
        print('Raspberry Pi A+ - 256MB/512MB RAM - Rev 1.1 Manufactured by Embest')
elif revcode == '900021':
        print('Raspberry Pi A+ - 512MB RAM - Rev 1.1 Manufactured by Sony UK')
elif revcode == '900032':
        print('Raspberry Pi B+ - 512MB RAM - 100MBit LAN - Rev 1.2 Manufactured by Sony UK')
elif revcode == '900092':
        print('Raspberry Pi Zero - 512MB RAM - Rev 1.2 Manufactured by Sony UK')
elif revcode == '900093':
        print('Raspberry Pi Zero - 512MB RAM - Rev 1.3 Manufactured by Sony UK')
elif revcode == '9000c1':
        print('Raspberry Pi Zero W - 512MB RAM - 2,4GHz WLAN - Rev 1.1 Manufactured by Sony UK')
elif revcode == '9020e0':
        print('Raspberry Pi 3A+ - 512MB RAM - Rev 1.0 Manufactured by Sony UK')
elif revcode == '920092':
        print('Raspberry Pi Zero - 512MB RAM - Rev 1.2 Manufactured by Embast')
elif revcode == '920093':
        print('Raspberry Pi Zero - 512MB RAM - Rev 1.3 Manufactured by Embast')
elif revcode == '900061':
        print('Raspberry Pi CM - 512MB RAM - Rev 1.1 Manufactured by Sony UK')
elif revcode == 'a01040':
        print('Raspberry Pi 2 B - 1GB RAM - 100MBit LAN - Rev 1.0 Manufactured by Sony UK')
elif revcode == 'a01041':
        print('Raspberry Pi 2 B - 1GB RAM - 100MBit LAN - Rev 1.1 Manufactured by Sony UK')
elif revcode == 'a02082':
        print('Raspberry Pi 3 B - 1GB RAM - 100MBit LAN - 2,4GHz WLAN - Rev 1.2 Manufactured by Sony UK')
elif revcode == 'a020a0':
        print('Raspberry Pi CM3 - 1GB RAM - Rev 1.0 Manufactured by Sony UK')
elif revcode == 'a020d3':
        print('Raspberry Pi 3 B+ - 1GB RAM - 1GBit LAN - 2,4GHz/5GHz WLAN - Rev 1.3 Manufactured by Sony UK')
elif revcode == 'a02042':
        print('Raspberry Pi 2 B (with BCM2837) - 1GB RAM - 100MBit LAN - Rev 1.2 Manufactured by Sony UK')
elif revcode == 'a021041':
        print('Raspberry Pi 2 B - 1GB RAM - 100MBit LAN - Rev 1.1 Manufactured by Embest')
elif revcode == 'a22042':
        print('Raspberry Pi 2 B (with BCM2837) - 1GB RAM - 100MBit LAN - Rev 1.2 Manufactured by Embest')
elif revcode == 'a22082':
        print('Raspberry Pi 3 B - 1GB RAM - 100MBit LAN - 2,4GHz WLAN - Rev 1.2 Manufactured by Embest')
elif revcode == 'a220a0':
        print('Raspberry Pi CM3 - 1GB RAM - Rev 1.0 Manufactured by Embest')
elif revcode == 'a32082':
        print('Raspberry Pi 3 B - 1GB RAM - 100MBit LAN - 2,4GHz WLAN - Rev 1.2 Manufactured by Sony Japan')
elif revcode == 'a52082':
        print('Raspberry Pi 3 B - 1GB RAM - 100MBit LAN - 2,4GHz WLAN - Rev 1.2 Manufactured by Stadium')
elif revcode == 'a22083':
        print('Raspberry Pi 3 B - 1GB RAM - 100MBit LAN - 2,4GHz WLAN - Rev 1.3 Manufactured by Embest')
elif revcode == 'a02100':
        print('Raspberry Pi CM3+ - 1GB RAM - Rev 1.0 Manufactured by Sony UK')
elif revcode == 'a03111':
        print('Raspberry Pi 4 B - 1GB RAM - 1GBit LAN - 2,4GHz/5GHz WLAN - Rev 1.1 Manufactured by Sony UK')
elif revcode == 'b03111':
        print('Raspberry Pi 4 B - 2GB RAM - 1GBit LAN - 2,4GHz/5GHz WLAN - Rev 1.1 Manufactured by Sony UK')
elif revcode == 'b03112':
        print('Raspberry Pi 4 B - 2GB RAM - 1GBit LAN - 2,4GHz/5GHz WLAN - Rev 1.2 Manufactured by Sony UK')
elif revcode == 'c03111':
        print('Raspberry Pi 4 B - 4GB RAM - 1GBit LAN - 2,4GHz/5GHz WLAN - Rev 1.1 Manufactured by Sony UK')
elif revcode == 'a03112':
        print('Raspberry Pi 4 B - 4GB RAM - 1GBit LAN - 2,4GHz/5GHz WLAN - Rev 1.2 Manufactured by Sony UK')
elif revcode == 'd03114':
        print('Raspberry Pi 4 B - 8GB RAM - 1GBit LAN - 2,4GHz/5GHz WLAN - Rev 1.4 Manufactured by Sony UK')
else:
	print('Unknown')
