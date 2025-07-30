import sys
import csv
import requests

"""This script creates PagerDuty services based on a CSV file input. The CSV file should contain the service name and escalation policy ID.
The script reads the CSV file, constructs the necessary API requests, and creates the services in PagerDuty. 
Refer to the PaherDuty API Documentation here: https://developer.pagerduty.com/api-reference/7062f2631b397-create-a-service 
"""


def create_service(api_key, from_email, service_name, escalation_policy_id):
    url = "https://api.pagerduty.com/services"
    headers = {
        "Authorization": f"Token token={api_key}",
        "Accept": "application/vnd.pagerduty+json;version=2",
        "Content-Type": "application/json",
        "From": from_email,
    }
    payload = {
        "service": {
            "name": service_name,
            "escalation_policy": {
                "id": escalation_policy_id,
                "type": "escalation_policy_reference",
            },
        }
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 201:
        print(
            f"Created service '{service_name}' with escalation policy '{escalation_policy_id}'"
        )
    else:
        print(
            f"Failed to create service '{service_name}': {response.status_code} - {response.text}"
        )


def main():
    if len(sys.argv) != 4:
        print(
            "Usage: python create_pagerduty_services.py <API_KEY> <FROM_EMAIL> <CSV_FILE>"
        )
        sys.exit(1)

    api_key = sys.argv[1]
    from_email = sys.argv[2]
    csv_file = sys.argv[3]

    with open(csv_file, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            service_name = row["service_name"]
            escalation_policy_id = row["escalation_policy_id"]
            create_service(api_key, from_email, service_name, escalation_policy_id)


if __name__ == "__main__":
    main()
