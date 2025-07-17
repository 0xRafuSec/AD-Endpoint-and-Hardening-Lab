import subprocess

service_name = "SuspiciousServices"
binary_path = "C:\\Windows\\System32\\cmd.exe"

command = f'sc create {service_name} binPath= "{binary_path}" start= auto'
subprocess.run(command, shell=True)

print("Service Created! Check Event Viewer for ID 4697.")