import json
import re
from pathlib import Path

if __name__ == "__main__":
    input_file = Path("food_gifs.txt")
    all_gifs = []
    with open(file = input_file, mode = "r", encoding = "utf-8") as opened:
        lines = opened.readlines()

        for line in lines:
            matched = re.match(pattern = "<a href=\"(.*\.gif)\"", string = line)
            if matched:
                url = matched.group(1)
                all_gifs.append(url)

    output_file = Path("food_gif_urls.txt")
    output_file.touch(exist_ok = True)
    output_file.write_text(json.dumps(all_gifs, ensure_ascii = False, indent = 4), encoding = "utf-8")
