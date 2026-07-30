import argparse
import json
import sys

import requests


def print_response(response):
    print("=" * 60)
    print(f"Status : {response.status_code} {response.reason}")

    print("\nHeaders:")
    for key, value in response.headers.items():
        print(f"{key}: {value}")

    print("\nBody:")
    try:
        print(json.dumps(response.json(), indent=4))
    except ValueError:
        print(response.text)

    print("=" * 60)


def send_get(url):
    response = requests.get(url, timeout=10)
    print_response(response)


def send_post(url, data):
    response = requests.post(url, data=data, timeout=10)
    print_response(response)


def main():
    parser = argparse.ArgumentParser(
        description="Simple HTTP Client using the requests library"
    )

    parser.add_argument(
        "method",
        choices=["GET", "POST"],
        help="HTTP method",
    )

    parser.add_argument(
        "url",
        help="Target URL",
    )

    parser.add_argument(
        "--data",
        nargs="*",
        help="POST data in key=value format",
    )

    args = parser.parse_args()

    try:
        if args.method == "GET":
            send_get(args.url)

        elif args.method == "POST":
            payload = {}

            if args.data:
                for item in args.data:
                    if "=" in item:
                        key, value = item.split("=", 1)
                        payload[key] = value

            send_post(args.url, payload)

    except requests.exceptions.RequestException as error:
        print(f"Request failed: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()