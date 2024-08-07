import os
import pexpect
from packages import ADDONS, ADDONS_LINKS

def main():
    # spicetify-cli
    spicetify_install = pexpect.spawn("sh", ["-c", "curl -fsSL https://raw.githubusercontent.com/spicetify/cli/main/install.sh | sh"])
    spicetify_install.sendline("n")
    spicetify_install.interact()

    # spicetify-marketplace
    spicetify_marketplace_install = pexpect.spawn("sh", ["-c", "curl -fsSL https://raw.githubusercontent.com/spicetify/marketplace/main/resources/install.sh | sh"])
    spicetify_marketplace_install.interact()

def addons():
    os.system("spicetify config custom_apps lyrics-plus")
    os.system("spicetify apply")
    
    # Downloading extensions
    os.chdir('.config/spicetify/Extensions')
    for addon in ADDONS_LINKS:
        install_package(addon)
    os.chdir('..')
    os.chdir('..')
    os.chdir('..')

    # Applying extensions
    for addon in ADDONS:
        config_package(addon)
    
    os.system("spicetify backup apply")    

def config_package(package_name: str):
    os.system(f"spicetify config extensions {package_name}")
    os.system("spicetify apply")

def install_package(package_name: str):
    os.system(f'curl -O {package_name}')

def theme():
    os.system("git clone --depth=1 https://github.com/spicetify/spicetify-themes.git")
    os.chdir("spicetify-themes")
    os.system('cp -r * ~/.config/spicetify/Themes')
    change_theme('Ziro', 'rose-pine-moon')
    os.chdir('..')

def change_theme(theme_name: str, sub_theme: str):
    os.system(f"spicetify config current_theme {theme_name}")
    os.system(f"spicetify config color_scheme {sub_theme}")
    os.system("spicetify apply")

if __name__ == "__main__":
    main()
    addons()
    theme()     

