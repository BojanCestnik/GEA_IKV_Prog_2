import subprocess

if __name__ == "__main__":
    interface = "eth0"
    new_mac = "22:11:22:33:44:55"

    print("Shutting down the interface ...")
    subprocess.run(["ifconfig", "eth0", "down"])

    print("Changing the interface MAC address of ", interface, " to ", new_mac)
    subprocess.run(["ifconfig", interface, "hw", "ether", new_mac])
   
    print("MAC address changed to ", new_mac, ".")
    subprocess.run(["ifconfig", interface, "up"])
   
    print("Network interface is turned on.")
    