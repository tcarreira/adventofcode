# My solutions to https://adventofcode.com/

- [2023](./2023/) (Python)
- [2022](./2022/) (Go)
- [2021](./2021/) (Python)
- [2020](./2020/) (Python)
- [2019](./2019/) (Python)


## Before starting

```
git submodule update --init --remote  # fetch and init submodules
python3 -m virtualenv .venv
. .venv/bin/activate
pip install -r requirements.txt -r aoc-to-markdown/requirements.txt
echo "SESSION_ID=<session cookie>" > .env
```

## Start a new problem

You may automatically fetch the data with:
```
./start_aoc_day.py
```

and refresh the `README.md`, after completing part 1, with:
```
./start_aoc_day.py last
```

You may use other arguments. For more information type `./start_aoc_day.py -h`
or visit [aoc-to-markdown repository](https://github.com/antonio-ramadas/aoc-to-markdown).

