import shutil
import subprocess

update = {
    "apt": [["sudo", "apt", "update"], ["sudo", "apt", "full-upgrade", "-y"]],
    "pacman": [["sudo", "pacman", "-Syu", "--noconfirm"]],
    "dnf": [["sudo", "dnf", "upgrade", "--refresh", "-y"]],
    "flatpak": [["flatpak", "update", "-y"]]
}

clean = {
    "apt": [["sudo", "apt", "autoremove", "-y"], ["sudo", "apt", "autoclean"]],
    "pacman": [["sudo", "pacman", "-Sc", "--noconfirm"]],
    "dnf": [["sudo", "dnf", "autoremove", "-y"], ["sudo", "dnf", "clean", "all"]],
    "flatpak": [["flatpak", "uninstall", "--unused", "-y"]]
}

update=input("would you like to update now?[Y/n]").lower()

def execute():
    if update=="Y":
        for tool in update:
            if shutil.which(tool):
                for cmds in tool:
                    subprocess.run(cmds)
    for tool in clean:
        if shutil.which(tool):
            for cmds in tool:
                subprocess.run(cmds)
    
execute()