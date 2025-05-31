Refill Agent API — Contract-Driven Design Documentation
📌 Project Overview
The Refill Agent API is a Flask-based application that simulates the behavior of a healthcare agent handling medication refill requests. The logic is governed by a Contract-Driven Design using Relari's Agent Contract paradigm, enforcing preconditions, path conditions, and postconditions to ensure consistent, safe, and logical behavior.
________________________________________
🧱 Directory Structure
graphql
CopyEdit
agent-contracts-refill/
│
├── app/
│   ├── __init__.py
│   ├── contracts.py       # Defines the RefillContract (with all contract checks)
│   ├── logic.py           # Core logic for handling refill requests
│   ├── mock_db.py         # Mock database simulating patient data
│   └── routes.py          # API route that triggers the contract-driven logic
│
├── run.py                 # Flask app launcher
└── requirements.txt       # (optional) For Python package dependencies
________________________________________
🔄 API Endpoint
POST /process_refill
•	Description: Processes a refill request after validating via contract-based conditions.
•	Request Body (JSON):
json
CopyEdit
{
  "patient_id": "12345",
  "prescription_number": "RX123",
  "medication_name": "XYZ"
}
•	Success Response (200):
json
CopyEdit
{
  "message": "Refill approved for John Doe. Pickup in 2 hours. Confirmation: REF45123"
}
•	Error Responses:
o	Missing fields:
json
CopyEdit
{
  "message": "Preconditions not met.",
  "errors": ["Missing or empty field: patient_id"]
}
o	Unsupported medication:
json
CopyEdit
{
  "message": "Path conditions not met.",
  "errors": ["Medication not supported"]
}
o	Postcondition failure:
json
CopyEdit
{
  "message": "Postconditions failed after refill.",
  "errors": ["Postcondition failed: Refill not approved"]
}
________________________________________
✅ Contract-Driven Design
✔️ 1. Preconditions
Ensures that the input meets all basic schema requirements.
Implemented using Pydantic for validation:
python
CopyEdit
class RefillInput(BaseModel):
    patient_id: str
    prescription_number: str
    medication_name: str
Fails if any required field is missing or empty.
________________________________________
✔️ 2. Path Conditions
Controls the valid logical paths the agent can take.
Example: Only specific medications are eligible for refills.
python
CopyEdit
if self.data.get("medication_name") not in ["XYZ", "ABC", "123", "Paracetamol"]:
    self.errors.append("Medication not supported")
________________________________________
✔️ 3. Postconditions
Checks if the action performed meets expected outcomes.
Example: Message must contain "Refill approved".
python
CopyEdit
if "Refill approved" not in response_message:
    self.errors.append("Postcondition failed: Refill not approved")
________________________________________
💡 Mock Database
mock_db.py simulates patient and prescription records:
python
CopyEdit
MOCK_DB = {
    "12345": {
        "name": "John Doe",
        "prescriptions": {
            "RX123": {
                "medication": "XYZ",
                "last_filled": "2024-03-15"
            }
        }
    }
}
________________________________________
🔧 Business Logic (logic.py)
•	Extracts values from input
•	Checks contracts in this order:
1.	check_preconditions
2.	check_path_conditions
3.	Executes refill and simulates update
4.	check_postconditions
•	Returns appropriate message or error response
________________________________________
🧪 Testing the API
You can test the /process_refill endpoint using curl:
bash
CopyEdit
curl -X POST http://127.0.0.1:5000/process_refill ^
  -H "Content-Type: application/json" ^
  -d "{\"patient_id\": \"12345\", \"prescription_number\": \"RX123\", \"medication_name\": \"XYZ\"}"
________________________________________
🚀 How to Run
1.	Navigate to project root:
bash
CopyEdit
cd agent-contracts-refill
2.	Start Flask server:
bash
CopyEdit
python run.py
3.	Server will run at:
http://127.0.0.1:5000
________________________________________
🏁 Final Notes
•	Scalability: Easily extendable to handle other agent actions.
•	Maintainability: Contracts are modular and separated from logic.
•	Verifiability: Each stage of execution is explicitly validated.
•	Inspired by: Relari Agent Contracts

 
 
