import argparse
import requests
from termcolor import colored
from urllib.parse import urlparse

def normalize_url(url: str) -> str:
    """Ensure the URL has a scheme (http or https)."""
    parsed_url = urlparse(url)
    if not parsed_url.scheme:
        # Default to 'http' if no scheme is provided
        url = f"http://{url}"
    return url

def getSites(urls: list[str]):
    # Header and separator
    print(f"{'No.':<4} {'URL':<50} {'Status':<15} {'Reason':<25} {'Time Elapsed':<15}")
    print("="*110)

    for it, url in enumerate(urls):
        try:
            # Normalize the URL
            url = normalize_url(url)
            req = requests.get(url, timeout=5)
            color = ""

            # Determine color based on status code
            if req.status_code < 200:           # Informational responses
                color = 'cyan'
            elif 200 <= req.status_code < 300:  # Success responses
                color = 'green'
            elif 300 <= req.status_code < 400:  # Redirection messages
                color = 'blue'
            elif 400 <= req.status_code < 500:  # Client errors
                color = 'yellow'
            else:                               # Server errors (500–599)
                color = 'red'
            
            # Print the result
            print(colored(f"{it + 1:<4} {req.url:<50} {req.status_code:<15} {req.reason:<25} {str(req.elapsed.total_seconds()):<15}", color))
        
        except requests.exceptions.RequestException as e:
            # Handle any errors during the HTTP request
            print(colored(f"{it + 1:<4} {url:<50} {"Failed to resolve":<15}", "red"))

def main():
    parser = argparse.ArgumentParser(description="A tool for checking the availability of websites")

    # Arguments
    parser.add_argument("urls", nargs="*", type=str, help="URLs to check")
    parser.add_argument("-f", "--file", type=str, help="File to read the URLs from")

    # Parse arguments
    args = parser.parse_args()

    # Handle cases where no arguments are provided
    if not args.urls and not args.file:
        parser.print_help()
        return

    try:
        if args.file:
            try:
                urls = []
                with open(args.file, "r") as reader:
                    urls = [line.strip() for line in reader if line.strip()]
                getSites(urls)
            except FileNotFoundError as e:
                print(f"File not found: {e}")
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            # Ensure urls is a list of strings
            if args.urls:
                getSites(args.urls)
            else:
                print("No URLs provided.")
    except KeyboardInterrupt:
        print("\nStopped")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
