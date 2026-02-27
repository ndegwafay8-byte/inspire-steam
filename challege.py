from machine import Pin, I2C
import utime

# ================= LCD DRIVER =================
class I2cLcd:
    def __init__(self, i2c, addr, rows, cols):
        self.i2c = i2c
        self.addr = addr
        self.rows = rows
        self.cols = cols

        utime.sleep_ms(20)
        self._write_cmd(0x33)
        self._write_cmd(0x32)
        self._write_cmd(0x28)
        self._write_cmd(0x0C)
        self._write_cmd(0x06)
        self.clear()

    def _write_cmd(self, cmd):
        self._write4(cmd & 0xF0)
        self._write4((cmd << 4) & 0xF0)

    def _write_data(self, data):
        self._write4(data & 0xF0, True)
        self._write4((data << 4) & 0xF0, True)

    def _write4(self, data, char_mode=False):
        control = 0x01 if char_mode else 0x00
        self.i2c.writeto(self.addr, bytes([data | control | 0x04]))
        self.i2c.writeto(self.addr, bytes([data | control]))

    def clear(self):
        self._write_cmd(0x01)
        utime.sleep_ms(2)

    def move_to(self, col, row):
        addr = col + (0x40 if row else 0x00)
        self._write_cmd(0x80 | addr)

    def putstr(self, string):
        for char in string:
            self._write_data(ord(char))

# ================= HARDWARE SETUP =================
# LCD I2C (GP0 SDA, GP1 SCL)
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
lcd = I2cLcd(i2c, 0x27, 2, 16)

# Buzzer (GP15)
buzzer = Pin(15, Pin.OUT)

# Keypad Pins
rows = [Pin(2, Pin.OUT), Pin(3, Pin.OUT), Pin(4, Pin.OUT), Pin(5, Pin.OUT)]
cols = [
    Pin(6, Pin.IN, Pin.PULL_DOWN),
    Pin(7, Pin.IN, Pin.PULL_DOWN),
    Pin(8, Pin.IN, Pin.PULL_DOWN),
    Pin(9, Pin.IN, Pin.PULL_DOWN)
]

keys = [
    ["1","2","3","A"],
    ["4","5","6","B"],
    ["7","8","9","C"],
    ["*","0","#","D"]
]

PASSWORD = "2424"
entered = ""

# ================= FUNCTIONS =================
def beep(duration=0.1):
    buzzer.high()
    utime.sleep(duration)
    buzzer.low()

def read_key():
    for i, row in enumerate(rows):
        row.high()
        for j, col in enumerate(cols):
            if col.value():
                utime.sleep(0.2)  # debounce
                row.low()
                return keys[i][j]
        row.low()
    return None

# ================= MAIN PROGRAM =================
lcd.putstr("Enter Password:")
lcd.move_to(0, 1)

while True:
    key = read_key()
    if key:
        beep(0.05)
        entered += key
        lcd.putstr("*")

        if len(entered) == len(PASSWORD):
            utime.sleep(0.5)
            lcd.clear()

            if entered == PASSWORD:
                lcd.putstr("Access Granted")
                beep(0.3)
            else:
                lcd.putstr("Wrong Password")
                for _ in range(3):
                    beep(0.2)
                    utime.sleep(0.1)

            utime.sleep(2)
            lcd.clear()
            lcd.putstr("Enter Password:")
            lcd.move_to(0, 1)
            entered = ""