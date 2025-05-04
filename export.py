import requests
import csv

# 1. Login
login_url = "http://localhost:8000/api/login"
credentials = {"email": "demo@demo.gr", "password": "demo1"}
response = requests.post(login_url, json=credentials)

if response.status_code == 200:
    token = response.json().get("token")
    print(" Login successful!")
    
    # 2. Λήψη δεδομένων JSON
    projects_url = "http://localhost:8000/api/csv"
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
    
    projects_response = requests.get(projects_url, headers=headers)
    
    if projects_response.status_code == 200:
        projects = projects_response.json()
        
        # Εξαγωγή σε CSV
        if isinstance(projects, list) and len(projects) > 0:  # Ελέγχουμε αν είναι λίστα
            with open("projects.csv", "w", newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=projects[0].keys())
                writer.writeheader()  # Γράφει τα headers (στήλες)
                writer.writerows(projects)  # Γράφει όλα τα δεδομένα
            print(" CSV saved successfully! (projects.csv)")
        else:
            print(" No projects data or invalid format!")
    else:
        print(" Failed to fetch projects:", projects_response.json())
else:
    print(" Login failed:", response.json())