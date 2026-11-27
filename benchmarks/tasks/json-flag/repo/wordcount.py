import argparse
import sys


def count(text):
    return {"lines": text.count("\n"), "words": len(text.split()), "chars": len(text)}


def main(argv=None):
    parser = argparse.ArgumentParser(description="Count lines, words and characters.")
    parser.add_argument("file", nargs="?", help="file to read (default: stdin)")
    args = parser.parse_args(argv)
    text = open(args.file, encoding="utf-8").read() if args.file else sys.stdin.read()
    c = count(text)
    print(f"{c['lines']} {c['words']} {c['chars']}")


if __name__ == "__main__":
    main()
