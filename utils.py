import requests
import csv
from termcolor import colored
from urllib.parse import urlparse

def normalize_url(url: str) -> str:
    """Ensure the URL has a scheme (http or https)."""
    try:
        parsed_url = urlparse(url)
        if not parsed_url.scheme:
            url = f"http://{url}"
        return url
    except Exception as e:
        print(f"Error normalizing URL '{url}': {e}")
        return url

def get_status_color(status_code: int) -> str:
    """Return the color based on the HTTP status code."""
    try:
        if status_code < 200:
            return 'cyan'   # Informational responses
        elif 200 <= status_code < 300:
            return 'green'  # Success responses
        elif 300 <= status_code < 400:
            return 'blue'   # Redirection messages
        elif 400 <= status_code < 500:
            return 'yellow' # Client errors
        else:
            return 'red'    # Server errors (500–599)
    except Exception as e:
        print(f"Error determining status color for code {status_code}: {e}")
        return 'white'

def check_site(url: str, index: int, timeout: int) -> dict:
    """Check a single URL and return a dictionary of results."""
    try:
        url = normalize_url(url)
        req = requests.get(url, timeout=timeout)
        color = get_status_color(req.status_code)

        result = {
            'No.': index,
            'URL': req.url,
            'Status': req.status_code,
            'Reason': req.reason,
            'Time Elapsed (s)': req.elapsed.total_seconds()
        }
        print(colored(f"{index:<4} {req.url:<50} {req.status_code:<15} {req.reason:<25} {str(req.elapsed.total_seconds()):<15}", color))
        return result
    except requests.exceptions.RequestException as e:
        error_msg = {
            'No.': index,
            'URL': url,
            'Status': 'Failed',
            'Reason': 'Unable to resolve',
            'Time Elapsed (s)': 'N/A'
        }
        print(colored(f"{index:<4} {url:<50} {'Failed':<15} {'Unable to resolve':<25} {'N/A':<15}", "red"))
        return error_msg
    except Exception as e:
        error_msg = {
            'No.': index,
            'URL': url,
            'Status': 'Error',
            'Reason': str(e),
            'Time Elapsed (s)': 'N/A'
        }
        print(colored(f"{index:<4} {url:<50} {'Unknown Error':<15} {str(e):<25}", "red"))
        return error_msg

def get_sites(urls: list[str], writefile: str = None, timeout: int = 5):
    """Check a list of URLs and optionally write results to a CSV file."""
    header = f"{'No.':<4} {'URL':<50} {'Status':<15} {'Reason':<25} {'Time Elapsed':<15}"
    separator = "=" * 110
    print(header)
    print(separator)

    results = []
    for it, url in enumerate(urls):
        result = check_site(url, it + 1, timeout)
        results.append(result)

    if writefile:
        write_results_to_csv(results, writefile)

def write_results_to_csv(results: list[dict], writefile: str):
    """Write the results to a specified CSV file."""
    try:
        with open(writefile, "w", newline='') as csvfile:
            fieldnames = ['No.', 'URL', 'Status', 'Reason', 'Time Elapsed (s)']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(results)

        print(f"Results written to {writefile}")
    except FileNotFoundError as e:
        print(f"Failed to write to file '{writefile}': File not found - {e}")
    except IOError as e:
        print(f"Failed to write to file '{writefile}': I/O error - {e}")
    except Exception as e:
        print(f"Failed to write to file '{writefile}': {e}")

def load_urls_from_file(filepath: str) -> list[str]:
    """Load URLs from a file."""
    try:
        with open(filepath, "r") as reader:
            return [line.strip() for line in reader if line.strip()]
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        return []
    except IOError as e:
        print(f"Failed to read file '{filepath}': I/O error - {e}")
        return []
    except Exception as e:
        print(f"An error occurred while loading URLs from file '{filepath}': {e}")
        return []
