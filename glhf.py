import httpx
import random
import ctypes
import threading
import os
from colorama import Fore, init, deinit


class MrX:
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
        "Pragma": "no-cache",
        "Host": "store.epicgames.com",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.8",
        "x-requested-with": "XMLHttpRequest",
        "Content-Type": "application/json",
    }
    BASE_URL = "https://store.epicgames.com/graphql"
    CODE_LENGTH = 20

    def __init__(self):
        self.client = httpx.Client()
        self.cpm = 0
        self.invalid = 0
        self.hit = 0
        self.threads = 0

    def set_title(self):
        title = f"| Invalid: {self.invalid} | Hit: {self.hit} | CPM: {self.cpm} | Bot: {self.threads} |"
        ctypes.windll.kernel32.SetConsoleTitleW(title)

    def banner(self):
        banner_text = f"""{Fore.LIGHTMAGENTA_EX}
                            ──────────────────▒
                            ─────────────────░█
                            ────────────────███
                            ───────────────██ღ█
                            ──────────────██ღ▒█──────▒█
                            ─────────────██ღ░▒█───────██
                            ─────────────█ღ░░ღ█──────█ღ▒█
                            ────────────█▒ღ░▒ღ░█───██░ღღ█
                            ───────────░█ღ▒░░▒ღ░████ღღღ█
                            ───░───────█▒ღ▒░░░▒ღღღ░ღღღ██─────░█
                            ───▓█─────░█ღ▒░░░░░░░▒░ღღ██─────▓█░
                            ───██─────█▒ღ░░░░░░░░░░ღ█────▓▓██
                            ───██────██ღ▒░░░░░░░░░ღ██─░██ღ▒█
                            ──██ღ█──██ღ░▒░░░░░░░░░░ღ▓██▒ღღ█
                            ──█ღღ▓██▓ღ░░░▒░░░░░░░░▒░ღღღ░░▓█
                            ─██ღ▒▒ღღ░░ღღღღ░░▒░░░░ ღღღღ░░ღღღ██
                            ─█ღ▒ღღ█████████ღღ▒░ღ██████████ღ▒█░
                            ██ღღ▒████████████ღღ████████████░ღ█▒
                            █░ღღ████████████████████████████ღღ█
                            █▒ღ██████████████████████████████ღ█
                            ██ღღ████████████████████████████ღ██
                            ─██ღღ██████████████████████████ღ██
                            ──░██ღღ██████████████████████ღღ██
                            ────▓██ღ▒██████████████████▒ღ██
                            ───░──░███ღ▒████████████▒ღ███
                            ────░░───▒██ღღ████████▒ღ██
                            ───────────▒██ღ██████ღ██
                            ─────────────██ღ████ღ█
                            ───────────────█ღ██ღ█
                            ────────────────█ღღ█
                            ────────────────█ღ█░
                            ─────────────────██░
                                                           """
        print(banner_text)

    def request(self, key):
        data = {
            "query": "mutation lockCodeMutation($codeId: String, $locale: String) {  CodeRedemption {    lockCode(codeId: $codeId, locale: $locale) {      success      data {        namespace        title        description        image        eulaIds        entitlementName        codeUseId      }    }  }}",
            "variables": {"codeId": key, "locale": "tr"},
        }

        try:
            response = self.client.post(self.BASE_URL, headers=self.HEADERS, json=data)
            response.raise_for_status()
        except httpx.RequestError as e:
            print(f"An error occurred while requesting: {e}")
            self.cpm -= 1
            return
        except httpx.HTTPStatusError as e:
            print(f"HTTP error occurred: {e}")
            self.cpm -= 1
            return

        if 'errors":[{"message' in response.text:
            print(
                f"\n{Fore.RED}[-] {Fore.YELLOW} Invalid Code -> {Fore.GREEN}{key} | 🔍 Tg: @CleinKelvinn"
            )
            self.invalid += 1
            self.cpm += 1
        else:
            print(
                f"\n{Fore.CYAN}[+] {Fore.LIGHTMAGENTA_EX} Hit -> {Fore.LIGHTRED_EX}{key} | 🔍 Tg: @CleinKelvinn"
            )
            with open("Hit.txt", "a") as f:
                f.write(key + "\n")
            self.hit += 1
            self.cpm += 1

        self.set_title()

    def generate_key(self):
        chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWYZX"
        return "".join(random.choice(chars) for _ in range(self.CODE_LENGTH))

    def thread_starter(self):
        key = self.generate_key()
        self.request(key)

    def start_checking(self):
        while True:
            if threading.active_count() <= self.threads:
                threading.Thread(target=self.thread_starter, daemon=True).start()

    def main(self):
        init(autoreset=True)
        self.banner()
        try:
            self.threads = int(
                input(f"\n{Fore.YELLOW}> {Fore.WHITE}[50 Bot is Better] Threads: ")
            )
        except ValueError:
            print(f"{Fore.RED}Invalid input! Please enter a number.")
            return

        os.system("cls" if os.name == "nt" else "clear")
        self.banner()
        print(f"\n{Fore.YELLOW}> {Fore.LIGHTRED_EX}Checker Running..")
        self.start_checking()
        deinit()


if __name__ == "__main__":
    MrX().main()
