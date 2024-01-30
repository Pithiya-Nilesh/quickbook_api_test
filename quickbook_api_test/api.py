import requests 
import frappe
import json

@frappe.whitelist()
def test():
    

    url = "https://sandbox-quickbooks.api.intuit.com/v3/company/9130355479284696/timeactivity"

    body = {
        "TxnDate": "2021-02-02",
        "EndTime": "17:00:00-08:00",
        "EmployeeRef": {
            "name": "Emily Platt",
            "value": "55"
        },
        "StartTime": "08:00:00-08:00",
        "NameOf": "Employee"
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=body, headers=headers)
    api_response = frappe.new_doc("Api Response")
    api_response.response = json.dumps(response.text, indent=4)
    api_response.insert(ignore_permissions=True)
    frappe.db.commit()
