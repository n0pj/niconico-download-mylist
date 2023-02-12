from niconico import NicoNico
from dotenv import load_dotenv
import pprint
import time
import os

load_dotenv()

DOWNLOAD_DIR = "downloads"
URL = os.getenv("MYLIST_URL")

def wapper_x(line_list):
    if not os.path.exists(DOWNLOAD_DIR):
        os.mkdir(DOWNLOAD_DIR)
    for i in range(len(line_list)):
        url = line_list[i][1]

        print(f"Downloading {url}")

        with client.video.get_video(url) as video:
            file_name = f"{DOWNLOAD_DIR}/{video.video.id} - {video.video.title.replace('/', '-')}.mp4"

            if os.path.exists(file_name):
                print(f"Skipping    {url} as it already exists")
                continue

            video.download(file_name)

            print(f"Downloaded  {url}")

    return 0

client = NicoNico()
for mylist in client.video.get_mylist(URL):
    line_list = []
    for line in mylist.items:
        line_list.append([line.video.id, line.video.url, line.video.title])

# total
print(f"Total: {len(line_list)}")

wapper_x(line_list)

exit()
