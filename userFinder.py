import requests
from bs4 import BeautifulSoup

class TextColor:
    RED = '\033[91m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    END = '\033[0m'

def check_social_profile(platform, username):
    if platform == "instagram":
        url = f"https://imginn.com/{username}/"
        display_url = f"https://instagram.com/{username}"
    elif platform == "twitter":
        url = f"https://nitter.privacydev.net/{username}"
        display_url = f"https://x.com/{username}"
    elif platform == "youtube":
        url = f"https://youtube.com/@{username}"
        display_url = url
    elif platform == "reddit":
        url = f"https://old.reddit.com/user/{username}"
        display_url = f"https://reddit.com/user/{username}"
    elif platform == "myanimelist":
        url = f"https://myanimelist.net/profile/{username}"
        display_url = url
    elif platform == "github":
        url = f"https://github.com/{username}"
        display_url = url
    elif platform == "snapchat":
        url = f"https://www.snapchat.com/add/{username}"
        display_url = url
    elif platform == "chess":
        url = f"https://www.chess.com/member/{username}"
        display_url = url
    elif platform == "twitch":
        url = f"https://twitchtracker.com/{username}"
        display_url = f"https://twitch.tv/{username}"
    elif platform == "minecraft":
        url = f"https://api.mojang.com/users/profiles/minecraft/{username}"
        display_url = url
    elif platform == "bitbucket":
        url = f"https://bitbucket.org/{username}"
        display_url = url
    elif platform == "9gag":
        url = f"https://9gag.com/u/{username}"
        display_url = url
    elif platform == "pastebin":
        url = f"https://pastebin.com/u/{username}"
        display_url = url
    elif platform == "redbubble":
        url = f"https://www.redbubble.com/people/{username}"
        display_url = url
    elif platform == "openstreetmap":
        url = f"https://www.openstreetmap.org/user/{username}"
        display_url = url
    elif platform == "patreon":
        url = f"https://www.patreon.com/{username}"
        display_url = url
    elif platform == "pensador":
        url = f"https://www.pensador.com/autor/{username}"
        display_url = url
    elif platform == "vsco":
        url = f"https://vsco.co/{username}/gallery"
        display_url = url
    elif platform == "tiktok":
        url = f'https://tiktok.wpme.pl/@{username}'
        display_url = f'https://tiktok.com/@{username}'
        return check_tiktok_profile(url, display_url)
    elif platform == "rapfame":
        url = f'https://rapfame.app/user/{username}'
        display_url = url
    else:
        return None

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return display_url
    elif response.status_code == 404:
        return 404
    elif response.status_code == 429:
        return 404
    elif response.status_code == 304:
        return 304
    elif response.status_code == 500:
        return 404
    else:
        return None


def check_tiktok_profile(url, display_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        if "API error code 10 (EMPTY_RESPONSE)" in soup.text:
            return display_url 
        elif "API error code 10221 (USER_BAN)" in soup.text:
            return 404  
        else:
            return None  # Lỗi gì đó lạ lắm, chưa rõ luôn!
    else:
        return None


# Danh sách các "sân chơi" mạng xã hội
platforms = [
    "instagram", "twitter", "youtube", "reddit", "myanimelist", "github", "snapchat",
    "chess", "twitch", "minecraft", "bitbucket", "9gag", "pastebin",
    "redbubble", "openstreetmap", "patreon", "pensador", "vsco", "tiktok", "rapfame",
]

username = input(f"{TextColor.RED}Nhập tên tài khoản đi nào, đừng ngại: {TextColor.END}")
profile_found = False

for platform in platforms:
    result = check_social_profile(platform, username)

    if result == 404:
        print(f"{TextColor.RED}Ôi xời, {platform.capitalize()} không có ai tên này đâu!{TextColor.END}")
    elif isinstance(result, str):
        print(f"{TextColor.GREEN}Bingo! Tìm thấy tài khoản trên {platform.capitalize()}: {result} - Ghê chưa?{TextColor.END}")
        profile_found = True
    else:
        print(f"{TextColor.YELLOW}Hài hước cái gì đây? {platform.capitalize()} trả về lỗi lạ, chịu thua luôn!{TextColor.END}")

if not profile_found:
    print(f"{TextColor.RED}Hic, tìm hoài mà chả thấy cái tài khoản nào! Thử tên khác coi?{TextColor.END}")
else:
    print(f"{TextColor.GREEN}Xong phim! Đã tìm được ít nhất một tài khoản, ez!{TextColor.END}")