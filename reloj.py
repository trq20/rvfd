from machine import Pin, SPI
import st7789

tft = st7789.ST7789(
    SPI(2, baudrate=30000000, polarity=1, phase=1, sck=Pin(18), mosi=Pin(19)),
    240,
    240,
    reset=Pin(23, Pin.OUT),
    dc=Pin(22, Pin.OUT)
) # Contructor del display

tft.init()  # Inicializacion del display

# TODO
