import sys
import serial
import time


def send_command(ser, cmd):
    ser.write(cmd)
    ser.flush()
    time.sleep(0.01)


def draw_cube(ser):
    send_command(ser, b'\x18\x00\x03\x33')
    send_command(ser, b'\x19\x00\x00\x00')
    send_command(ser, b'\x00\x00\x40\x00')
    send_command(ser, b'\x00\x01\x00\x4e')
    send_command(ser, b'\x01\x00\xc0\x00')
    send_command(ser, b'\x01\x01\x00\x15')
    send_command(ser, b'\x02\x00\x96\xa8')
    send_command(ser, b'\x02\x01\x00\x00')
    send_command(ser, b'\x03\x00\x40\x00')
    send_command(ser, b'\x03\x01\x00\x1d')
    send_command(ser, b'\x04\x00\xc0\x00')
    send_command(ser, b'\x04\x01\x00\x28')
    send_command(ser, b'\x05\x00\x78\x78')
    send_command(ser, b'\x05\x01\x00\x00')
    send_command(ser, b'\x06\x00\x40\x00')
    send_command(ser, b'\x06\x01\x00\x13')
    send_command(ser, b'\x07\x00\x80\x00')
    send_command(ser, b'\x07\x01\x00\x5d')
    send_command(ser, b'\x08\x00\x98\xc3')
    send_command(ser, b'\x08\x01\x00\x00')
    send_command(ser, b'\x12\x00\x00\x00')
    send_command(ser, b'\x12\x01\x00\x00')
    send_command(ser, b'\x13\x00\x96\xa8')
    send_command(ser, b'\x13\x01\x00\x00')
    send_command(ser, b'\x14\x00\x00\x00')
    send_command(ser, b'\x14\x01\x00\x00')
    send_command(ser, b'\x15\x00\x00\x00')
    send_command(ser, b'\x15\x01\x00\x00')
    send_command(ser, b'\x16\x00\x98\xc3')
    send_command(ser, b'\x16\x01\x00\x00')
    send_command(ser, b'\x17\x00\x00\x00')
    send_command(ser, b'\x17\x01\x00\x00')
    send_command(ser, b'\x1a\x00\x00\x01')
    send_command(ser, b'\x00\x00\xc0\x00')
    send_command(ser, b'\x00\x01\x00\x5e')
    send_command(ser, b'\x01\x00\x00\x00')
    send_command(ser, b'\x01\x01\x00\x35')
    send_command(ser, b'\x02\x00\x67\x34')
    send_command(ser, b'\x02\x01\x00\x00')
    send_command(ser, b'\x03\x00\x40\x00')
    send_command(ser, b'\x03\x01\x00\x52')
    send_command(ser, b'\x04\x00\x00\x00')
    send_command(ser, b'\x04\x01\x00\x56')
    send_command(ser, b'\x05\x00\xcc\xcc')
    send_command(ser, b'\x05\x01\x00\x00')
    send_command(ser, b'\x06\x00\x00\x00')
    send_command(ser, b'\x06\x01\x00\x65')
    send_command(ser, b'\x07\x00\x40\x00')
    send_command(ser, b'\x07\x01\x00\x63')
    send_command(ser, b'\x08\x00\x7e\x07')
    send_command(ser, b'\x08\x01\x00\x00')
    send_command(ser, b'\x12\x00\x00\x00')
    send_command(ser, b'\x12\x01\x00\x00')
    send_command(ser, b'\x13\x00\x67\x34')
    send_command(ser, b'\x13\x01\x00\x00')
    send_command(ser, b'\x14\x00\xcc\xcc')
    send_command(ser, b'\x14\x01\x00\x00')
    send_command(ser, b'\x15\x00\x00\x00')
    send_command(ser, b'\x15\x01\x00\x00')
    send_command(ser, b'\x16\x00\x7e\x07')
    send_command(ser, b'\x16\x01\x00\x00')
    send_command(ser, b'\x17\x00\x7e\x07')
    send_command(ser, b'\x17\x01\x00\x00')
    send_command(ser, b'\x1a\x00\x00\x01')
    send_command(ser, b'\x00\x00\x40\x00')
    send_command(ser, b'\x00\x01\x00\x52')
    send_command(ser, b'\x01\x00\x00\x00')
    send_command(ser, b'\x01\x01\x00\x56')
    send_command(ser, b'\x02\x00\xcc\xcc')
    send_command(ser, b'\x02\x01\x00\x00')
    send_command(ser, b'\x03\x00\xc0\x00')
    send_command(ser, b'\x03\x01\x00\x36')
    send_command(ser, b'\x04\x00\x40\x00')
    send_command(ser, b'\x04\x01\x00\x66')
    send_command(ser, b'\x05\x00\x68\x5b')
    send_command(ser, b'\x05\x01\x00\x00')
    send_command(ser, b'\x06\x00\x00\x00')
    send_command(ser, b'\x06\x01\x00\x65')
    send_command(ser, b'\x07\x00\x40\x00')
    send_command(ser, b'\x07\x01\x00\x63')
    send_command(ser, b'\x08\x00\x7e\x07')
    send_command(ser, b'\x08\x01\x00\x00')
    send_command(ser, b'\x12\x00\x00\x00')
    send_command(ser, b'\x12\x01\x00\x00')
    send_command(ser, b'\x13\x00\xcc\xcc')
    send_command(ser, b'\x13\x01\x00\x00')
    send_command(ser, b'\x14\x00\x68\x5b')
    send_command(ser, b'\x14\x01\x00\x00')
    send_command(ser, b'\x15\x00\x00\x00')
    send_command(ser, b'\x15\x01\x00\x00')
    send_command(ser, b'\x16\x00\x7e\x07')
    send_command(ser, b'\x16\x01\x00\x00')
    send_command(ser, b'\x17\x00\x7e\x07')
    send_command(ser, b'\x17\x01\x00\x00')
    send_command(ser, b'\x1a\x00\x00\x01')
    send_command(ser, b'\x00\x00\xc0\x00')
    send_command(ser, b'\x00\x01\x00\x5e')
    send_command(ser, b'\x01\x00\x00\x00')
    send_command(ser, b'\x01\x01\x00\x35')
    send_command(ser, b'\x02\x00\x67\x34')
    send_command(ser, b'\x02\x01\x00\x00')
    send_command(ser, b'\x03\x00\x40\x00')
    send_command(ser, b'\x03\x01\x00\x4e')
    send_command(ser, b'\x04\x00\xc0\x00')
    send_command(ser, b'\x04\x01\x00\x15')
    send_command(ser, b'\x05\x00\x96\xa8')
    send_command(ser, b'\x05\x01\x00\x00')
    send_command(ser, b'\x06\x00\x40\x00')
    send_command(ser, b'\x06\x01\x00\x52')
    send_command(ser, b'\x07\x00\x00\x00')
    send_command(ser, b'\x07\x01\x00\x56')
    send_command(ser, b'\x08\x00\xcc\xcc')
    send_command(ser, b'\x08\x01\x00\x00')
    send_command(ser, b'\x12\x00\x00\x00')
    send_command(ser, b'\x12\x01\x00\x00')
    send_command(ser, b'\x13\x00\x67\x34')
    send_command(ser, b'\x13\x01\x00\x00')
    send_command(ser, b'\x14\x00\x00\x00')
    send_command(ser, b'\x14\x01\x00\x00')
    send_command(ser, b'\x15\x00\x00\x00')
    send_command(ser, b'\x15\x01\x00\x00')
    send_command(ser, b'\x16\x00\xcc\xcc')
    send_command(ser, b'\x16\x01\x00\x00')
    send_command(ser, b'\x17\x00\x00\x00')
    send_command(ser, b'\x17\x01\x00\x00')
    send_command(ser, b'\x1a\x00\x00\x01')
    send_command(ser, b'\x00\x00\x40\x00')
    send_command(ser, b'\x00\x01\x00\x52')
    send_command(ser, b'\x01\x00\x00\x00')
    send_command(ser, b'\x01\x01\x00\x56')
    send_command(ser, b'\x02\x00\xcc\xcc')
    send_command(ser, b'\x02\x01\x00\x00')
    send_command(ser, b'\x03\x00\x40\x00')
    send_command(ser, b'\x03\x01\x00\x13')
    send_command(ser, b'\x04\x00\x80\x00')
    send_command(ser, b'\x04\x01\x00\x5d')
    send_command(ser, b'\x05\x00\x98\xc3')
    send_command(ser, b'\x05\x01\x00\x00')
    send_command(ser, b'\x06\x00\xc0\x00')
    send_command(ser, b'\x06\x01\x00\x36')
    send_command(ser, b'\x07\x00\x40\x00')
    send_command(ser, b'\x07\x01\x00\x66')
    send_command(ser, b'\x08\x00\x68\x5b')
    send_command(ser, b'\x08\x01\x00\x00')
    send_command(ser, b'\x12\x00\x00\x00')
    send_command(ser, b'\x12\x01\x00\x00')
    send_command(ser, b'\x13\x00\xcc\xcc')
    send_command(ser, b'\x13\x01\x00\x00')
    send_command(ser, b'\x14\x00\x00\x00')
    send_command(ser, b'\x14\x01\x00\x00')
    send_command(ser, b'\x15\x00\x00\x00')
    send_command(ser, b'\x15\x01\x00\x00')
    send_command(ser, b'\x16\x00\x68\x5b')
    send_command(ser, b'\x16\x01\x00\x00')
    send_command(ser, b'\x17\x00\x00\x00')
    send_command(ser, b'\x17\x01\x00\x00')
    send_command(ser, b'\x1a\x00\x00\x01')
    send_command(ser, b'\x00\x00\x40\x00')
    send_command(ser, b'\x00\x01\x00\x4e')
    send_command(ser, b'\x01\x00\xc0\x00')
    send_command(ser, b'\x01\x01\x00\x15')
    send_command(ser, b'\x02\x00\x96\xa8')
    send_command(ser, b'\x02\x01\x00\x00')
    send_command(ser, b'\x03\x00\x40\x00')
    send_command(ser, b'\x03\x01\x00\x13')
    send_command(ser, b'\x04\x00\x80\x00')
    send_command(ser, b'\x04\x01\x00\x5d')
    send_command(ser, b'\x05\x00\x98\xc3')
    send_command(ser, b'\x05\x01\x00\x00')
    send_command(ser, b'\x06\x00\x40\x00')
    send_command(ser, b'\x06\x01\x00\x52')
    send_command(ser, b'\x07\x00\x00\x00')
    send_command(ser, b'\x07\x01\x00\x56')
    send_command(ser, b'\x08\x00\xcc\xcc')
    send_command(ser, b'\x08\x01\x00\x00')
    send_command(ser, b'\x12\x00\x00\x00')
    send_command(ser, b'\x12\x01\x00\x00')
    send_command(ser, b'\x13\x00\x96\xa8')
    send_command(ser, b'\x13\x01\x00\x00')
    send_command(ser, b'\x14\x00\x98\xc3')
    send_command(ser, b'\x14\x01\x00\x00')
    send_command(ser, b'\x15\x00\x00\x00')
    send_command(ser, b'\x15\x01\x00\x00')
    send_command(ser, b'\x16\x00\xcc\xcc')
    send_command(ser, b'\x16\x01\x00\x00')
    send_command(ser, b'\x17\x00\xcc\xcc')
    send_command(ser, b'\x17\x01\x00\x00')
    send_command(ser, b'\x1a\x00\x00\x01')
    send_command(ser, b'\x1b\x00\x00\x00')


def main(argv):
    if (len(argv) == 0):
        print("Usage: client.py <serial device>")
        exit(0)
    else:
        ser = serial.Serial(argv[0], baudrate=115200)
        draw_cube(ser)
        ser.close()
    exit(0)


if __name__ == "__main__":
    main(sys.argv[1:])
