# hUGEGBS
This is a very hacked up version of hUGEDriver/hUGETracker's .gbs export code mixed with ISSO's GB-Boilerplate, I made it to make my life easier when ripping my music for oscilloscope views, being able to control which channels play on every export.

## Usage
To compile, export your song to RGBDS asm through hUGETracker and place it under `src`, replacing the `song.asm` file in there, afterwards just use `make` as normally, although mind you, a Python script (rempad.py) is called during the compiling process so make sure you have Python 3, it's only been tested on Linux but it should work on any platform RGBDS supports with some changes to the Python call.

To change the channel flags, go to `hardware.inc` and change the flags at the beginning:
```
	; Used for GBS ripping
	; Set these to 0 or 1 for each channel
	DEF CH1 EQU 1
	DEF CH2 EQU 1
	DEF CH3 EQU 1
	DEF CH4 EQU 1
```
After this, you can rip each channel with tools such as foobar2000's game music emu plugin (Doesn't seem to work on other .gbs players such as Nezplug or GBSPlay).