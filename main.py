import os

TEXT = (
    "The printer jams every time I print something urgent, so today I "
    "printed my resignation, and it came out perfect.\n"
)


def output_dir():
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main():
    directory = output_dir()
    os.makedirs(directory, exist_ok=True)
    with open(os.path.join(directory, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(TEXT)


if __name__ == "__main__":
    main()
