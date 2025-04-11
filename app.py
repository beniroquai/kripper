from arkitekt_next import register
import time
import uc2rest

port = "unknown"# # let it discover the port itself
ESP32 = uc2rest.UC2Client(serialport=port, baudrate=115200, DEBUG=True, skipFirmwareCheck =True)

# wake up open gripper
ESP32.gripper.close(isBlocking=True)
ESP32.gripper.open(isBlocking=True)

@register
def open_gripper() -> str:
    """
    """
    ESP32.gripper.open(isBlocking=True)
    return "gripper opened"

@register
def close_gripper() -> str:
    """
    """
    ESP32.gripper.close(isBlocking=True)
    return "gripper closed"

