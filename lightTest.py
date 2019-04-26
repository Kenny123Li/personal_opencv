import time
import board
import neopixel


pixel_pin = board.D18
num_pixels = 15
ORDER = neopixel.RGBW
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)
blue=(0,0,255,0)

pass_found=True
x=0
for x in range(15):
    pixels[x]=blue
    pixels.show()
    time.sleep(1)
    
pixels.fill((0,0,0,0))
pixels.show()
##if pass_found == True:
##    pixels.fill((255,0,0,0))
##    pixels.show()
##
##time.sleep(1)
##pass_found=False
##
##elif pass_found==False:
##    pixels.fill((0,255,0,0))
##    pixels.show()
