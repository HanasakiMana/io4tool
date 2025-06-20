This tool is designed to perform simple I/O test for SEGA's 837-15257 I/O board (aka IO4).

This tool based on [pyhidapi](https://pypi.org/project/hid/), which uses [hidapi library](https://github.com/libusb/hidapi). However, this package cannot find hidapi correctly, so I copied the source code into `hid.py` and fix this problem by using absolute path (see line 25).