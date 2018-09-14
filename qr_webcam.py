from qrtools import QR
import time
while True:
  MyCode = QR()
  MyCode.data_decode [MyCode.data_type] (MyCode.data)
  MyCode.decode_webcam()
  print MyCode.data