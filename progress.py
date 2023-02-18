import requests, pytz, json, os, math
from datetime import datetime
import calendar, time
from dotenv import load_dotenv


load_dotenv()
IST = pytz.timezone("Asia/Kolkata")


def send_req(content):
    url = os.getenv("DISCORD_URL")

    headers = {"Content-Type": "application/json"}

    data = {
        "content": content,
        "avatar_url": "https://i.pinimg.com/736x/9c/ed/98/9ced98a5437a7bed4b5575e1b4e732ab.jpg",
    }

    requests.post(url=url, data=json.dumps(data), headers=headers)


def check_progress(year_progress):
    # year_progress = 60
    with open("progress.json", "r+") as pr:
        progress = json.load(pr)

    bar = list()

    for i in range(0, 20):
        if i < year_progress / 5:
            bar.append("▓")
        else:
            bar.append("▒")

    content = "".join(bar) + " **" + str(year_progress) + "%**"

    if progress["last_progress"] < year_progress:
        send_req(content=content)

    if year_progress == 100:
        progress["last_progress"] = 0
    else:
        progress["last_progress"] = year_progress

    with open("progress.json", "w") as pw:
        json.dump(progress, pw, indent=4)


def main():
    current_datetime = datetime.now(IST)

    current_year = current_datetime.year

    day_of_year = current_datetime.timetuple().tm_yday

    current_year_days = 365 if calendar.isleap(current_year) else 366

    year_progress = math.trunc((day_of_year / current_year_days) * 100)

    check_progress(year_progress=year_progress)

    print(current_datetime)

    return current_datetime.strftime("%B %d %Y %H:%M:%S")
