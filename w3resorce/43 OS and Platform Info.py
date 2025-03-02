#Write a Python program to get OS name, platform and release information.
import os
import platform
print(os.name)
print(platform.system())
print(platform.release())

#os.name: Gives a basic type identifier (e.g., 'nt' for Windows or 'posix' for Linux/macOS).
#platform.system(): Provides a more human-readable OS name (e.g., 'Windows', 'Linux', 'Darwin' for macOS).
#platform.release(): Provides the specific version or release of the OS (e.g., version number, kernel version).