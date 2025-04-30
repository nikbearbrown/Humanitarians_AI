# Enhanced Healthcare Agent System

## PROJECT TEAM : 
- Komal Albhar
- Shardul Deshmukh

## Table of Contents
- [Overview](#overview)
- [Agent Contracts](#agent-contracts)
  - [Inspiration from Relari](#inspiration-from-relari)
  - [Contract Structure](#contract-structure)
- [Project Architecture](#project-architecture)
- [Key Components](#key-components)
  - [DiagnosisAgent](#diagnosisagent)
  - [TreatmentAgent](#treatmentagent)
  - [Verification System](#verification-system)
- [Sample Data](#sample-data)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
- [Web Interface](#web-interface)
- [License](#license)

## Overview

The Healthcare Agent System demonstrates the implementation of Agent Contracts for medical diagnosis and treatment workflows. This system leverages the Groq API with Llama 3.3 70b model to create a reliable and accountable AI-assisted healthcare process.

The system consists of two specialized agents:
1. **DiagnosisAgent**: Processes patient symptoms to provide a primary diagnosis with confidence level and alternatives
2. **TreatmentAgent**: Recommends appropriate treatments based on diagnosis results and patient data

Each agent operates under a formal contract that defines requirements and guarantees about its behavior. The system includes verification mechanisms to ensure agents fulfill their contracts.

## Agent Contracts

### Inspiration from Relari

This project is inspired by the Relari framework for agent reliability. Relari represents a significant advancement in the field of AI safety and reliability by introducing a formal approach to specifying and enforcing agent behavior.

In the Relari framework:

- **Contracts** are explicit, formal specifications that define what an agent should and shouldn't do
- These contracts act as a form of "guardrails" that help ensure AI systems behave reliably
- Agents can be certified against these contracts, providing accountability and trust

The Relari philosophy emphasizes that reliability in AI systems doesn't emerge naturally but must be engineered deliberately through careful specification and verification. This project adopts that philosophy by implementing concrete contracts and verification mechanisms in a healthcare context.

### Contract Structure

In our system, following Relari principles, agent contracts consist of three key elements:

1. **Preconditions**: Requirements that must be met before an agent can perform its task. For example, the DiagnosisAgent requires that patient symptoms, age, and gender be provided before it can generate a diagnosis.

2. **Pathconditions**: Steps or processes that the agent must follow during its reasoning process. For example, the TreatmentAgent must check for medication interactions when formulating a treatment plan.

3. **Postconditions**: Requirements that the agent's output must satisfy. For example, the DiagnosisAgent must provide a primary diagnosis, alternative diagnoses, a confidence level, and diagnostic reasoning.

The contract specifications are stored in JSON format, making them easily machine-readable and verifiable.

## Project Architecture

The system follows a modular architecture:

```
enhanced_healthcare_system.py  # Core system implementation
streamlit_app.py               # Web interface
data/
├── patients.json             # Sample patient data
├── patients.csv              # Alternative sample data format
└── specs.json                # Agent contract specifications
results/
└── run_TIMESTAMP/            # Generated during execution
    ├── patient_XXX.json      # Individual patient results
    └── summary.json          # Batch processing summary
```

## Key Components

### DiagnosisAgent

The DiagnosisAgent takes patient information as input and produces a diagnosis following its contract. The contract requires:

**Preconditions:**
- Patient provides symptoms
- Patient provides age and gender

**Pathconditions:**
- Check patient medical history
- Analyze symptoms against common conditions
- Consider age and gender factors

**Postconditions:**
- Provide primary diagnosis
- List alternative diagnoses
- Include confidence level for primary diagnosis
- Provide diagnostic reasoning

### TreatmentAgent

The TreatmentAgent receives diagnosis results and patient information to recommend appropriate treatments. Its contract requires:

**Preconditions:**
- Valid diagnosis is provided
- Patient allergies are available
- Current medications are listed

**Pathconditions:**
- Check for medication interactions
- Consider patient age and medical history

**Postconditions:**
- Recommend appropriate medications
- Suggest relevant therapy options
- Provide lifestyle recommendations
- Specify follow-up timeline
- Note any special considerations or warnings

### Verification System

The system includes a Verifier that checks both agents' compliance with their contracts:

1. **Precondition Verification**: Ensures all required input data is present and valid
2. **Postcondition Verification**: Validates that output meets all requirements
3. **Certification**: Generates a certificate with a unique ID when verification passes

The verification results are included with the agent outputs, providing transparency and accountability.

## Sample Data

### Input Data

The system includes sample patient data in JSON format:

```json
{
  "id": "patient-001",
  "name": "John Davis",
  "patient_data": {
    "age": 45,
    "gender": "Male",
    "symptoms": [
      "persistent cough",
      "shortness of breath",
      "fatigue",
      "mild fever"
    ],
    "medical_history": [
      "asthma",
      "seasonal allergies"
    ],
    "allergies": [
      "penicillin"
    ],
    "current_medications": [
      "albuterol inhaler"
    ]
  }
}
```

### Output Data

The system produces detailed output for each patient:

```json
{
  "patient_info": {
    "id": "SAM-DNI8I3",
    "name": "Sam",
    "age": 45,
    "gender": "Male"
  },
  "diagnosis": {
    "primary_diagnosis": "Chronic Obstructive Pulmonary Disease (COPD)",
    "differential_diagnoses": [
      "Pneumonia",
      "Asthma exacerbation",
      "Allergic bronchopulmonary aspergillosis"
    ],
    "confidence": 0.7,
    "reasoning": "The patient's persistent cough and fatigue, combined with a history of asthma and seasonal allergies, suggest a chronic respiratory condition. COPD is a likely diagnosis given the patient's age and symptoms, although the absence of smoking history is not provided. The differential diagnoses consider the possibility of an infectious or allergic component."
  },
  "diagnosis_certification": {
    "certified": true,
    "certificate": "CERT-081fac4a-74d3-4810-9b5b-27305becef53",
    "issues": []
  },
  "treatment": {
    "medication": [
      "tiotropium bromide inhaler (18 mcg, 1 inhalation daily)",
      "salmeterol-fluticasone inhaler (50-500 mcg, 1 inhalation twice daily)",
      "hydrocodone-guaifenesin (5-10 mg, 1-2 tablets every 4-6 hours as needed)"
    ],
    "therapy": [
      "Pulmonary rehabilitation program",
      "Smoking cessation program",
      "Oxygen therapy as needed"
    ],
    "lifestyle": [
      "Avoid exposure to dust and other environmental allergens",
      "Maintain a healthy weight",
      "Engage in regular physical activity, such as walking or yoga",
      "Eat a balanced diet rich in fruits, vegetables, and whole grains"
    ],
    "follow_up": {
      "schedule": "Follow up with primary care physician in 2 weeks",
      "tests": "Pulmonary function tests (PFTs) every 3-6 months",
      "monitoring": "Monitor oxygen saturation levels and adjust oxygen therapy as needed"
    },
    "considerations": [
      "Patient's allergy to penicillin should be considered when prescribing antibiotics",
      "Monitor for potential interactions between albuterol inhaler and newly prescribed medications",
      "COPD exacerbations may require hospitalization or adjustment of treatment plan"
    ]
  },
  "treatment_certification": {
    "certified": true,
    "certificate": "CERT-f14a7464-0495-4174-be06-563d68ce76d9",
    "issues": []
  },
  "processing_time": "2.490804",
  "timestamp": "2025-04-25T03:39:22.517114"
}
```

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Groq API key (Sign up at https://groq.com)
- Required Python packages (see requirements.txt)

### Installation

1. Clone this repository
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
3. Set up your Groq API key as an environment variable:
   ```
   export GROQ_API_KEY=your_key_here
   ```
   Or use a .env file

### Usage

#### Command Line Interface

Run the main script:
```
python enhanced_healthcare_system.py
```

You'll be prompted to:
1. Select a data source (JSON file, CSV file, or built-in scenarios)
2. Choose how many patients to process
3. View results for each patient

#### Batch Processing

The system supports batch processing of multiple patient records and saves results in JSON format for further analysis.

## Web Interface

A Streamlit web interface is included for easier interaction:

```
streamlit run streamlit_app.py
```

The interface provides:
- Single patient processing
- Batch processing
- History viewing
- Result visualization

## License

Proprietary. All rights reserved.

---

**Disclaimer**: This application is a demonstration of AI-assisted healthcare using Agent Contracts. Medical diagnoses and treatments should always be performed by licensed healthcare professionals.