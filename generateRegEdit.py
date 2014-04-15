import json

codes = open("scancodes.json")
codes = json.load(codes)

prefs = open("preferences.json")
prefs = json.load(prefs)

out = open("generatedRegEdit.reg", mode="w")
out.write("Windows Registry Editor Version 5.00\n\n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Keyboard Layout]\n\"Scancode Map\"=hex:00,00,00,00,00,00,00,00,")

def twoCharHexString(x_int):
	x_int = hex(x_int)[2:]
	if len(x_int) == 1: x_int = "0"+x_int
	elif len(x_int) > 2: raise ValueError("Value too large for 2 digit hex. Value > 0xFF.")
	return x_int.upper()

out.write(twoCharHexString(len(prefs)+1)+",00,00,00,")

for p in prefs.keys():
	out.write(codes[prefs[p]]+",00,"+codes[p]+",00,")

out.write("00,00,00,00")