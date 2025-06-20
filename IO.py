import hid
from const import *

class IO4(object):

    boardInfo = ''

    reportId = bytearray(1)
    adcs = bytearray(16)
    spinners = bytearray(8)
    chutes = bytearray(4)
    buttons = bytearray(4)
    sysStat = bytearray(1)
    usbStat = bytearray(1)

    outputPayload = bytearray(62)


    def __init__(self):
        devices = hid.enumerate(vid=0x0ca3, pid=0x0021)
        # assert device connection
        if len(devices) == 0:
            raise ConnectionError("No devices found, please check the connection!")
        elif len(devices) > 1:
            raise ConnectionError(f"Found {len(devices)} devices, please make sure connect only 1 device at a time!")

        # get device info
        device = devices[0]
        prodDesc = device.get('product_string').split(';')
        funcDesc = prodDesc[7].split('_')

        self.boardInfo = f'''Path:         {device.get('path').decode('utf-8')}
Vendor Id:    {device.get('vendor_id')}
Product Id:   {device.get('product_id')}
Serial Num:   {device.get('serial_number')}
Release Num:  {device.get('release_number')}
Manufacturer: {device.get('manufacturer_string')}
Product Description:
Board Type:          {prodDesc[0]}
Board Number:        {prodDesc[1]}
Board Sub Number:    {prodDesc[2]}
Firmware Revision:   {prodDesc[3]}
Firmware CheckSum:   {prodDesc[4]}
Output MOSFET Model: {prodDesc[5]}
Configuration:       {prodDesc[6]}
Functions:
General-purpose Outputs: 0x{list(filter(lambda x: 'GOUT' in x, funcDesc))[0].split('=')[-1]}
ADC Inputs:              0x{list(filter(lambda x: 'ADIN' in x, funcDesc))[0].split('=')[-1]}
Rotary Inputs:           0x{list(filter(lambda x: 'ROTIN' in x, funcDesc))[0].split('=')[-1]}
Switch Inputs:           0x{list(filter(lambda x: 'SWIN' in x, funcDesc))[0].split('=')[-1]}
Unique Function:         0x{list(filter(lambda x: 'UQ' in x, funcDesc))[0].split('=')[-1]}
'''

        # create hid object
        self.device = hid.Device(path=device.get('path'))

    def readReport(self):
        report = self.device.read(64)
        self.reportId = report[0]
        self.adcs = report[1:17]
        self.spinners = report[17:25]
        self.chutes = report[25:29]
        self.buttons = report[29:33]
        self.sysStat = report[33]
        self.usbStat = report[34]
        uqInput = report[35:]
        assert len(uqInput) == 29

    def changeOutput(self, output: OUTPUT, status: bool):
        # 15257 uses 3 bytes to describe all outputs, and other 59 bytes are just padding
        if status:
            self.outputPayload[output.byte] = self.outputPayload[output.byte] | (1 << output.shift)
        else:
            self.outputPayload[output.byte] = self.outputPayload[output.byte] & ~(1 << output.shift)


    def changeAllOutputs(self, status: bool):
        for output in outputs:
            self.changeOutput(output, status)

    def sendReport(self):
        output = bytearray(2)
        # report id
        output[0] = 0x10
        # cmd
        output[1] = 0x04 # set general output
        # payload
        output = bytes(output + self.outputPayload)
        self.device.write(output)