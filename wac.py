import argparse
from utils import get_sites, load_urls_from_file

def main():
    parser = argparse.ArgumentParser(description="A tool for checking the availability of websites")

    # Arguments
    parser.add_argument("urls", nargs="*", type=str, help="URLs to check")
    parser.add_argument("-f", "--file", type=str, help="File to read the URLs from")
    parser.add_argument("-w", "--write", type=str, help="File to write the output to")

    # Parse arguments
    args = parser.parse_args()

    if not args.urls and not args.file:
        parser.print_help()
        return

    try:
        urls = args.urls
        if args.file:
            urls = load_urls_from_file(args.file)

        if urls:
            get_sites(urls, args.write)
        else:
            print("No URLs provided.")
    except KeyboardInterrupt as e:
        print("Stopped")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
