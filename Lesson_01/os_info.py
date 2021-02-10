# Have to collect Work Stations information
import platform
import sys

info = 'OS info is \n{} \n\nPython version is {}'.format(
    platform.uname(), sys.version, platform.architecture())

# Show "info" on the display
print(info)

# Open external txt file and write "info" into it. Close will perform automatically
with open('os_info.txt', 'w') as ff:
    ff.write(info)