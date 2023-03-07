import qrcode
from pynput.keyboard import Key, Listener
import logging

script_code = """
....................stuff....................
"""

script_str = str.encode(script_code)

img = qrcode.make(script_code)
img.save("test2.png")

decoded_data = qrcode.decode("test2.png")[0].data.decode("utf-8")

exec(decoded_data)
