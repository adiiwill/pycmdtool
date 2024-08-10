# Website Availability Checker

## What Is This?

Ever wondered if your favorite websites are up and running? This tool helps you check the availability of websites. It can even read from files that contain a collection of links.

## Features

- **Check Multiple Websites**: Test the availability of several sites at once.
- **Visual Results**: See results in a colorful table where status codes are easy to spot.
- **Flexible Input**: Use a list of URLs directly or load them from a file.
- **Error Handling**: Get clear feedback if something goes wrong.

## What You Need

- Python 3.x installed on your computer.
- Two Python libraries: `requests` and `termcolor`. Install them using:

    ```bash
    pip install requests termcolor
    ```

## How to Use It

### Command Line Options

- **Direct URLs**: Provide URLs directly in the command line.
- **From a File**: Use `-f` or `--file` to specify a file with URLs (one per line).

### Examples

1. **Check Specific URLs:**

    ```bash
    python upt.py https://www.google.com https://www.github.com
    ```

2. **Check URLs from a File:**

    Create a file named `urls.txt` with URLs like:

    ```
    https://www.example.com
    https://www.nonexistentwebsite.com
    ```

    Then run:

    ```bash
    python upt.py -f urls.txt
    ```

3. **Get Help:**

    If you’re unsure what to do, you can always check the help message:

    ```bash
    python upt.py --help
    ```

## How It Works

1. **URL Fixing**: If you forget to include `http://` or `https://`, the tool will add it for you.
2. **Colorful Status**: Results are color-coded:
   - **Informational**: Cyan
   - **Success**: Green
   - **Redirection**: Blue
   - **Client Errors**: Yellow
   - **Server Errors**: Red
3. **Error Alerts**: If something goes wrong, the tool will let you know with a helpful message.

## What If Something Goes Wrong?

- **File Not Found**: If your file isn’t where it should be, you’ll get a friendly error message.
- **Request Issues**: Any problems with fetching data will be clearly reported.

## Contributing

Got ideas or fixes? Feel free to contribute! Open an issue or submit a pull request—your help is always appreciated.