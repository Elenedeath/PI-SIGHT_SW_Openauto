import subprocess
import re
from time import sleep
import os

def get_mac_address():
    """Get MAC adress of SIGHTER RC"""
    output = subprocess.check_output(["bluetoothctl", "devices"]).decode("utf-8")
    pattern = r"Device\s+([^\s]+)\s+SIGHTER RC"
    match = re.search(pattern, output)
    if match:
        return match.group(1)
    else:
        return None

def check_connection(mac_address):
  global connection
  if mac_address:
    info = subprocess.check_output(["bluetoothctl", "info", mac_address]).decode("utf-8")
    pattern = r"Connected:\s+([^\s]+)\s"
    matches = re.findall(pattern, info)
    for connected in matches:
      if connected == "yes":
        connection = 1
      else:
        connection = 0
  else:
    # SIGHTER RC device not found
    connected = 0

def main():
  os.system('sudo rfkill block wifi')

  global connection
  connection = 0
  keyboard_mac_address = None

  while True :
    sleep(0.2)
    keyboard_mac_address = get_mac_address()
    check_connection(keyboard_mac_address)
    if connection == 1 :
      os.system('sudo rfkill unblock wifi')
      break

if __name__ == "__main__":
  main()