# Savings-Bonds

Use this program to make analyzing savings bonds easier. 
Save your bonds in a .dat file, comma separated,
in the following format:

Bond type, denomination, serial number, experation month/experation year


example:


EE, 500, D12345678EE, 12/2000

I, 200, R12345689I, 11/2005

.

.

.

currently supports EE or I bonds, change number of bonds at top of file before running,
make sure files 
are in the same directory, and change name of file accordingly 
(default is bonds.data). Requires Selenium for python, 
and Chrome Web Driver.