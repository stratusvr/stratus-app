import os
import sys
import subprocess
import platform
import zipfile
import requests
import shutil
import re
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.core.text import LabelBase
from kivy.graphics import Color, RoundedRectangle



if platform.system() == "Windows":
    import winreg


def check_adb_installed():
    adb_path = shutil.which("adb")
    print(str(adb_path))
    return adb_path if adb_path else False

def is_valid_ip_address(ip):
    regex = (
        r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}"
        r"([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
    )
    return re.match(regex, ip) is not None

def create_ip_file(ip):
    formatted_ip = f"-s {ip}"
    with open("ip_address.txt", "w") as ip_file:
        ip_file.write(formatted_ip)

def push_ip_file(adb_path):
    if adb_path:
        result = subprocess.run(
            [adb_path, "push", "ip_address.txt", "/sdcard/CloudXRLaunchOptions.txt"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        if result.returncode == 0:
            print("IP address pushed to headset.")
        else:
            print("Error pushing IP address:", result.stderr.decode("utf-8"))



def download_adb_package():
    platform_tools_url = {
        "Windows": "https://dl.google.com/android/repository/platform-tools-latest-windows.zip",
        "Linux": "https://dl.google.com/android/repository/platform-tools-latest-linux.zip",
        "Darwin": "https://dl.google.com/android/repository/platform-tools-latest-darwin.zip"
    }
    url = platform_tools_url.get(platform.system())
    response = requests.get(url, stream=True)
    filename = url.split("/")[-1]

    with open(filename, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    return filename


def extract_and_install_adb(filename):
    with zipfile.ZipFile(filename, "r") as zip_ref:
        zip_ref.extractall("platform-tools")

    adb_path = os.path.abspath("platform-tools")
    add_adb_to_path(adb_path)


def add_adb_to_path(adb_path):
    if platform.system() == "Windows":
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment", 0, winreg.KEY_ALL_ACCESS)
        current_path, _ = winreg.QueryValueEx(key, "Path")
        if adb_path not in current_path:
            winreg.SetValueEx(key, "Path", 0, winreg.REG_EXPAND_SZ, current_path + ";" + adb_path)
        winreg.CloseKey(key)

        # Notify the system of the change
        import ctypes
        SendMessage = ctypes.windll.user32.SendMessageW
        SendMessage(0xFFFF, 0x001A, 0, 0)
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        with open(os.path.expanduser("~/.bashrc"), "a") as bashrc:
            bashrc.write(f'\nexport PATH="{adb_path}:$PATH"')
        os.system(f'source {os.path.expanduser("~/.bashrc")}')


def install_apk(adb_path):
    apk_filename = "stratus.apk"
    result = subprocess.run(['adb', "install", "-r", apk_filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.returncode == 0:
        print("stratus.apk installed successfully.")
    else:
        print("Error installing stratus.apk:", result.stderr.decode("utf-8"))

def show_success_popup():
    popup = Popup(
        title="Operation successful!",
        content=Label(text="Operation successful!"),
        size_hint=(None, None),
        size=(300, 200),
    )
    popup.open()


class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'

        # Logo image
        logo = Image(source='logo.png')
        self.add_widget(logo)

        # Install Application button
        install_button = Button(
            text='Install Application',
            background_normal='',
            background_color=(1, 1, 1, 1),
            height=30,
            size_hint_y=None
        )
        install_button.background_color = (0.5, 0.5, 0.5, 1)  # Change the color to your preference
        install_button.bind(on_press=self.install_application)
        install_button.canvas.before.clear()
        with install_button.canvas.before:
            Color(*install_button.background_color)
            RoundedRectangle(size=install_button.size, pos=install_button.pos, radius=[3,])
        self.add_widget(install_button)

        # Text input box container
        text_input_container = FloatLayout(size_hint=(1, None), height=30)

        # Text input box
        self.text_input = TextInput(
            hint_text='Enter IP address',
            size_hint=(None, None),
            width=16 * 20,  # 16 characters width, assuming a character width of 20 pixels
            height=30,  # Height set to accommodate a single line of text
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )

        text_input_container.add_widget(self.text_input)
        self.add_widget(text_input_container)

        # Push to Headset button
        push_button = Button(
            text='Push to Headset',
            background_normal='',
            background_color=(1, 1, 1, 1),
            height=30,
            size_hint_y=None
        )
        push_button.background_color = (0.5, 0.5, 0.5, 1)  # Change the color to your preference
        push_button.bind(on_press=self.push_to_headset)
        push_button.canvas.before.clear()
        with push_button.canvas.before:
            Color(*push_button.background_color)
            RoundedRectangle(size=push_button.size, pos=push_button.pos, radius=[3,])
        self.add_widget(push_button)


    def install_application(self, instance):
        adb_path = shutil.which("adb")
        if adb_path:
            result = subprocess.run(
                [adb_path, "install", "-r", "stratus.apk"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )

            if result.returncode == 0:
                print("stratus.apk installed successfully.")
                show_success_popup()
            else:
                print("Error installing stratus.apk:", result.stderr.decode("utf-8"))
        else:
            popup = Popup(
                title="ADB not found",
                content=Label(text="ADB was not found in the system's PATH. Please install ADB and add it to the PATH before proceeding."),
                size_hint=(None, None),
                size=(400, 200),
            )
            popup.open()

    def push_to_headset(self, instance):
        ip_address = self.text_input.text.strip()
        adb_path = shutil.which("adb")
        if is_valid_ip_address(ip_address):
            create_ip_file(ip_address)
            push_ip_file(adb_path)
            show_success_popup()
        else:
            popup = Popup(
                title="Invalid IP address",
                content=Label(text="Please enter a valid IP address."),
                size_hint=(None, None),
                size=(400, 200),
            )
            popup.open()


class MyApp(App):
    title = 'Stratus VR Launcher'
    def build(self):
        return MainLayout()


if __name__ == '__main__':
    MyApp().run()

       




# def check_adb_installed():
#     try:
#         result = subprocess.run(["adb", "version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#         return result.returncode == 0
#     except FileNotFoundError:
#         return False