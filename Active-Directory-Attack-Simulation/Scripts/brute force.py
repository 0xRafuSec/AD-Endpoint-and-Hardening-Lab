import subprocess
import time

server = "aioulab.server" # Change to a valid server
username = "Administrator"  # Change to a valid user
wrong_password = "WrongPass123!" # Change to a valid password

attempts = 55  # More than 50
delay_between_attempts = 5  # Spread over 5 minutes

print(f"Starting {attempts} failed login attempts against {server}...")

for i in range(attempts):
    command = f'runas /user:{server}\\{username} /savecred "cmd.exe /c echo Test"'
    subprocess.run(command, input=f"{wrong_password}\n", text=True, shell=True)
    print(f"Attempt {i+1} failed login executed.")
    time.sleep(delay_between_attempts)

print("Test completed. Check Wazuh for triggered brute-force alerts.")