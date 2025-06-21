# IO4Tool

This tool is designed to perform simple I/O tests for SEGA's 837-15257 I/O board (also known as IO4).

## Before running
This tool is based on [pyhidapi](https://pypi.org/project/hid/), which itself relies on the [hidapi library](https://github.com/libusb/hidapi). However, Python refuses to load DLL files from untrusted path since Python 3.8(see [here](https://docs.python.org/3.8/library/ctypes.html#ctypes.CDLL)), which prevents this package from correctly locating the hidapi library, so I copied the source code into `hid.py` and fix this problem by adding a path prefix to the filename(see line 25).

To use this tool, you need to make sure that there is a hidapi dynamic link file for your system (e.g. `*.so`, `*.dll` or `*.dylib` files) in the `lib` folder. Then the program will automatically detect them and choose the suitable one. The `lib` folder is already contains dynamic link files for windows and macOS.

Please note that the `hidapi.dylib` file alreadly existed in the `lib` folder is compiled for Apple M-series chips. If you are using a Intel-based mac, you can use `homebrew` to install hidapi and extract the dylib file from where you install it.

## Packing

To pack this project into a exectuable file, please install `pyinstaller` by running `pip install pyinstaller`, and choose the corresponding `*.spec` file for your system.

For example, to compile `IO4Tool.exe` for Windows, you can run the command `pyinstaller win.spec`.

If you are using Linux, you need to create your own `*.spec` file. Just copy all contents from `win.spec` and modify the path of dynamic link files at line 15. This file must be the same as the one you prepared for your system in the `lib` folder.