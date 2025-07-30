import requests
import sys


def get_pagerduty_services(api_key, from_email_address):
    """
    Parameters:
    - api_key: Your PagerDuty API key

    """
    url = "https://api.pagerduty.com/services"

    headers = {
        "Accept": "application/vnd.pagerduty+json;version=2",
        "Authorization": f"Token token={api_key}",
        "Content-Type": "application/json",
        "From": from_email_address,
    }

    params = {"limit": 100}  # Adjust as needed; PagerDuty paginates results

    services = []

    while url:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code != 200:
            print(f"Error: {response.status_code} - {response.text}")
            sys.exit(1)
        data = response.json()
        services.extend(data.get("services", []))
        url = data.get("next")  # PagerDuty API v2 pagination
        params = {}  # Only needed for the first request
    return services


# Main function to run the script with command line arguments
if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: python create_services.py <API_KEY> <FROM_EMAIL_ADDRESS>")
        sys.exit(1)

    api_key = sys.argv[1]
    from_email_address = sys.argv[2]

    services = get_pagerduty_services(api_key, from_email_address)
    print(f"Found {len(services)} services:\n")

    for svc in services:
        print(f"{svc['id']}: {svc['name']}")
