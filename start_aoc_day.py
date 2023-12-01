#!/usr/bin/env python3
import fileinput
import os
import re
import sys
from datetime import datetime, timedelta
from dotenv import load_dotenv

curdir = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(1, curdir + "/aoc-to-markdown")  # xxx: lib does not have __init__
import aoc_to_markdown

# get the same (previous) year for ~11 months after finishing aoc
year = (datetime.now() - timedelta(days=11*30)).year
output_dir = f"{year}/"


def setup_session_id() -> bool:
    if os.getenv("SESSION_ID"):
        return True
    else:
        print("SESSION_ID is needed in order to download the input")
        answer = input("Want to input the session cookie value? [N/<cookie>] ")

        if answer and answer not in "Nn":
            os.environ["SESSION_ID"] = answer
            return True
    return False


def setup_program_arguments(last=False):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        with open(f"{output_dir}/README.md", "w") as f:
            f.write(f"# Solutions to [https://adventofcode.com/{year}](https://adventofcode.com/{year})\n\n<Story>\n\n")
            for i in range(1,26):
                f.write(f"- Day {i:02d}\n")
            f.write("\n")

    sys.argv = [sys.argv[0], "-o", output_dir, "-y", year]

    if last:
        folder_syntax = re.compile("^day-(\\d+)$")
        last_day = max(
            [
                int(folder_syntax.search(f).group(1))
                for f in os.listdir(output_dir)
                if folder_syntax.match(f)
            ],
            default=1,
        )
        sys.argv.append("-d")
        sys.argv.append(f"{last_day}")

    elif setup_session_id():  # don't download input again
        sys.argv.append("-i")

    sys.argv.append("-b")
    sys.argv.append(f"solver.py")


def update_readme():
    with fileinput.FileInput(f"{output_dir}README.md", inplace=True) as f:
        for line in f:
            match = re.search("- Day ([0-9]{2})", line.strip())
            if match:
                day_str = match.group(1)
                dirname = f"day-{day_str}"
                if os.path.exists(f"{output_dir}{dirname}"):
                    print(f"- [Day {day_str}]({dirname})")
                    continue

            print(line, end="", flush=True)


def main():
    load_dotenv()

    # manually set arguments for aoc_to_markdown
    # (until main accepts arguments)
    if len(sys.argv) <= 1:
        setup_program_arguments()
    elif len(sys.argv) == 2 and sys.argv[1] == "last":
        setup_program_arguments(last=True)

    aoc_to_markdown.main()
    update_readme()


if __name__ == "__main__":
    main()
