import tls_client, random, string, json, colorama, os, time, threading
from colorama import Fore
from json import load

os.system('cls')
session = tls_client.Session(
    client_identifier="chrome112",
    random_tls_extension_order=True
)

info = Fore.LIGHTBLUE_EX + ' ( / ) '
unknown = Fore.LIGHTWHITE_EX + ' ( ? ) '
error = Fore.LIGHTRED_EX + ' ( - ) '
success = Fore.LIGHTGREEN_EX + ' ( + ) '
bold = '\033[1m'
def ask():
    i = input(f"{info} Do You Wanna Continue?(y/n): ")
    if i == 'y':
        print(f"{info} Started Program")
    else:
        return
ask()
def generate_random_string(length=12):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))
def abp(text, delay=0.01):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
abp(f"{info}{bold}Reading Config.....")
config = json.load(open('config.json', 'r'))

class cfg:
    name = config["name"]
    random_name = config["random_name"]
    password = config["password"]
    random_password = config["random_password"]

abp(f"{bold}{info}Configuring things....")
abp(f"{bold}{info}Configured things starting gen...")
os.system('cls')
logo = """
██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗░██╗░░░░░░░██╗░█████╗░░█████╗░██╗░░░░░░░░░░░░░██╗░██████╗
██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝░██║░░██╗░░██║██╔══██╗██╔══██╗██║░░░░░░░░░░░░░██║██╔════╝
██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░░╚██╗████╗██╔╝██║░░██║██║░░██║██║░░░░░░░░░░░░░██║╚█████╗░
██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░░░████╔═████║░██║░░██║██║░░██║██║░░░░░░░░██╗░░██║░╚═══██╗
██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗░░╚██╔╝░╚██╔╝░╚█████╔╝╚█████╔╝███████╗██╗╚█████╔╝██████╔╝
╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░╚════╝░░╚════╝░╚══════╝╚═╝░╚════╝░╚═════╝░                                                                        
"""

print(logo)
def send_options_request(url):
    response = session.options(url)
    if response.status_code == 200:
        return True
    else:
        print(f"{bold}{error}OPTIONS request failed with status code: {response.status_code}")
        return False
def genr():
    ip = random.choice(["us", "au", "gb", "ae", "sa", "tw", "th", "it", "nl", "br", "ar", "sg", "nz", "mx", "tr", "ca", "in", "es", "de"])
    proxy = f"http://wlhqh7mq18qrgyr-country-{ip}:h2pl7s8692fqamc@rp.proxyscrape.com:6060"
    if cfg.random_password == 'true':
        psw = generate_random_string()
    elif cfg.random_password == 'false':
        psw = cfg.password
    else:
        print(f"{bold}{error}Error in config | 'random_password' must be 'true' or 'false'")
        return

    if cfg.random_name == 'true':
        name = str(random.choice(string.ascii_lowercase) + generate_random_string())
        eml = f"{name}@gmail.com"
    elif cfg.random_name == 'false':
        sters = generate_random_string()
        eml = f"{cfg.name}{sters}@gmail.com"
    else:
        print(f"{bold}{error}Error in config | 'random_name' must be 'true' or 'false'")
        return

    url = "https://ajax.streamable.com/users"
    if not send_options_request(url):
        return
    headers = {
        "authority": "ajax.streamable.com",
        "method": "POST",
        "path": "/users",
        "scheme": "https",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Cache-Control": "no-cache",
        "Content-Type": "application/json",
        "Origin": "https://streamable.com",
        "Pragma": "no-cache",
        "Referer": "https://streamable.com/",
        "Sec-Ch-Ua": '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "Windows",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"
    }
    payload = {
        "email": eml,
        "password": psw,
        "username": eml,
        "verification_redirect": "https://streamable.com?alert=verified"
    }
    post_response = session.post(url, headers=headers, json=payload, proxy=proxy)
    if post_response.status_code in [200, 204]:
        account_info = f"{eml}:{psw}"
        print(f"{bold}{success}Created Account: {account_info}")
        with open('accounts.txt', 'a') as file:
            file.write(account_info + '\n')
    else:
        print(f"{bold}{error}Error occurred while creating account | {eml}:{psw}| sc: {post_response.status_code}")
        print(post_response.text)
def threaded_genr():
    try:
        while True:
            genr()
    except Exception as e:
        print(f"{bold}{error}Error in thread: {e}")
num_threads = int(input("Enter the number of threads to run: "))
threads = []
for _ in range(num_threads):
    thread = threading.Thread(target=threaded_genr)
    thread.start()
    threads.append(thread)
for thread in threads:
    thread.join()

print("Account generation process completed.")
