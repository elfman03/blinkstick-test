import sys
import time

sys.path.append("blinkstick-python")
from blinkstick import blinkstick

def show_status(bstick):
    print ("    Current Color: " + bstick.get_color(color_format="hex"))
    #print ("    Info Block 1:  " + bstick.get_info_block1())
    #print ("    Info Block 2:  " + bstick.get_info_block2())

def blink_get_color(bstick):
  try:
    hex=bstick.get_color(color_format="hex")
    time.sleep(0.1)
  except Exception as e:
    print("BlinkStick Exception Fetching Color: {0}".format(e))
    hex="error"

  #print(hex)
  if hex=="#000000":
    return "black"
  elif hex=="#ffffff":
    return "white"
  elif hex=="#ff0000":
    return "red"
  elif hex=="#ffff00":
    return "yellow"
  elif hex=="#008000":
    return "green"
  elif hex=="#0000ff":
    return "blue"
  return "error"

def blink_set_color_safe(bstick,color):
  cur=blink_get_color(bstick)   # sometimes errors out
  #
  if(cur==color):
    return cur
  #
  bstick.set_color(name=color)
  time.sleep(0.1)
  #
  cur=blink_get_color(bstick)  # should not error out
  return cur

def get_bstick():
  bs=blinkstick.find_first()
  print ("Found device:")
  print ("    Manufacturer:  " + bs.get_manufacturer())
  print ("    Description:   " + bs.get_description())
  print ("    Serial:        " + bs.get_serial())
#  show_status(bs)
  return bs

bstick=get_bstick()
#time.sleep(1)
#show_status(bstick)
foo=True
while foo:
#  foo=False
  for color in ["white", "yellow", "green", "red", "blue", "black"]: 
    c=blink_set_color_safe(bstick,color)
    print(color+" result is "+c)

#bstick.turn_off()
#time.sleep(1)
#show_status(bstick)

