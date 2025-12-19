import subprocess
import sys

cmd = ['ping', '127.0.0.1', '-C', '4']
system = sys.platform

if system == 'win32':
    cmd = ['ping', '127.0.0.1']

proc = subprocess.run(cmd, capture_output=True, text=True)

print()

print(f'Args: {proc.args}')
print()
print(f'Stderr: {proc.stderr}')
print()
print(f'Stdout: {proc.stdout}')
print()
print(f'Retorncode: {proc.returncode}')
print()
