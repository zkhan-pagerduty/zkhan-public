import sys
import csv
import requests

"""This script creates PagerDuty services and also associates them with a business service. Data is provided via a CSV file input. 
The CSV file should contain the service name, escalation policy ID, and the business service to associate with.
The script reads the CSV file, constructs the necessary API requests, and creates the services in PagerDuty. 
Refer to the PagerDuty API Documentation here: https://developer.pagerduty.com/api-reference/7062f2631b397-create-a-service and 
https://developer.pagerduty.com/api-reference/3fb4a13b59634-associate-service-dependencies
"""


def create_service(
    api_key, from_email, service_name, escalation_policy_id, business_service_id
):

    url = "https://api.pagerduty.com/services"
    headers = {
        "Authorization": f"Token token={api_key}",
        "Accept": "application/vnd.pagerduty+json;version=2",
        "Content-Type": "application/json",
        "From": from_email,
    }

    service_payload = {
        "service": {
            "name": service_name,
            "escalation_policy": {
                "id": escalation_policy_id,
                "type": "escalation_policy_reference",
            },
        }
    }
    service_response = requests.post(url, headers=headers, json=service_payload)
    if service_response.status_code == 201:
        print(
            f"Created service '{service_name}' with escalation policy '{escalation_policy_id}'"
        )
        service_id = service_response.json()["service"]["id"]
    else:
        print(
            f"Failed to create service '{service_name}': {service_response.status_code} - {service_response.text}"
        )
        return

    # Step 2: Associate the new service with the business service
    # This is done by creating a dependency from the business service to the technical service
    if not business_service_id:
        print("No business service ID provided, skipping association.")
        return

    dependency_payload = {
        "relationships": [
            {
                "supporting_service": {
                    "id": service_id,
                    "type": "technical_service_reference",
                },
                "dependent_service": {
                    "id": business_service_id,
                    "type": "business_service_reference",
                },
            }
        ]
    }

    dependency_response = requests.post(
        "https://api.pagerduty.com/service_dependencies/associate",
        headers=headers,
        json=dependency_payload,
    )

    if dependency_response.status_code not in (200, 201):
        print(
            "Failed to associate service with business service:",
            dependency_response.text,
        )
        return

    print("Service successfully associated with business service!")


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
            business_service_id = row["business_service_id"]
            create_service(
                api_key,
                from_email,
                service_name,
                escalation_policy_id,
                business_service_id,
            )


if __name__ == "__main__":
    main()
