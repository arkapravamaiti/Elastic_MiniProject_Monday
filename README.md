# Incident Tickets ETL Pipeline - Elasticsearch Integration

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Elasticsearch](https://img.shields.io/badge/Elasticsearch-8.x-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

A complete ETL (Extract, Transform, Load) pipeline for processing and analyzing incident ticket data with Elasticsearch integration and advanced data enrichment capabilities.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Data Pipeline](#data-pipeline)
- [Project Structure](#project-structure)
- [Branching Strategy](#branching-strategy)
- [Version History](#version-history)
- [Contributing](#contributing)

## 🎯 Overview

This project demonstrates an enterprise-grade ETL pipeline that processes incident ticket data, performs data cleaning and enrichment, and indexes the data into Elasticsearch for advanced analytics and visualization in Kibana.

**Key Capabilities:**
- Automated data cleaning and standardization
- Rich data enrichment with derived metrics
- Elasticsearch integration with proper field mapping
- NaN/null value handling for JSON compatibility
- Scalable architecture for large datasets

## ✨ Features

### Data Processing
- **📂 CSV Data Ingestion**: Load incident ticket data from CSV files
- **🧹 Advanced Data Cleaning**: 
  - Remove duplicate tickets
  - Handle missing values intelligently
  - Standardize text fields
  - Validate date logic
  - Cap outliers in numeric fields

### Data Enrichment
- **📊 Derived Metrics**:
  - SLA breach detection
  - Resolution time calculations
  - First response time tracking
  - Escalation level categorization
  - Automation success tracking
  - Impact level assessment

- **🕐 Temporal Features**:
  - Opened weekday
  - Opened hour
  - Opened month
  - Opened quarter

### Elasticsearch Integration
- **💾 Efficient Indexing**: Bulk indexing with error handling
- **🔍 Field Mapping**: Proper data type mapping for analytics
- **⚠️ NaN Handling**: Convert NaN values to null for JSON compatibility
- **📈 Scalability**: Handle large datasets efficiently

## 🏗️ Architecture

```
Raw CSV Data
      ↓
Data Cleaning (dataClean.py)
      ↓
Enriched CSV
      ↓
Data Preparation (upload_to_es.py)
      ↓
Elasticsearch Indexing
      ↓
Kibana Dashboards
```

### Pipeline Stages:

1. **Extract**: Load data from `dummy_incident_tickets.csv`
2. **Transform**: 
   - Clean and standardize data
   - Handle special characters
   - Validate dates and numeric fields
   - Add derived features
3. **Load**: 
   - Index to Elasticsearch with proper field mapping
   - Handle NaN values for JSON compatibility

## 🔧 Prerequisites

- **Python**: 3.8 or higher
- **Elasticsearch**: 8.x (Cloud or local instance)
- **pip**: Python package manager
- **Git**: Version control

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/arkapravamaiti/Elastic_MiniProject_Monday.git
cd Elastic_MiniProject_Monday
```

### 2. Create Virtual Environment

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On Linux/Mac
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment

```bash
# Copy the sample environment file
cp .env.sample .env

# Edit .env with your Elasticsearch credentials
```

## ⚙️ Configuration

Create a `.env` file in the project root with the following configuration:

```bash
# Elasticsearch Cloud Configuration
ES_ENDPOINT=https://your-deployment.es.region.gcp.elastic.cloud:443
ES_API_KEY=your_api_key_here
ES_INDEX=incident_tickets_uploaded
```

### Configuration Parameters:

| Parameter | Description | Default | Required |
|-----------|-------------|---------|----------|
| `ES_ENDPOINT` | Elasticsearch cluster endpoint URL | - | ✅ |
| `ES_API_KEY` | Elasticsearch API key for authentication | - | ✅ |
| `ES_INDEX` | Index name for storing tickets | `incident_tickets_uploaded` | ❌ |

## 🚀 Usage

### Step 1: Clean and Enrich Data

```bash
python dataClean.py
```

**Output**: `cleaned_enriched_incident_tickets_updated_for_visualization.csv`

**This step performs:**
- Data cleaning and normalization
- Duplicate removal
- Date validation
- Numeric field validation
- Feature enrichment (SLA breach, weekday, etc.)

### Step 2: Upload to Elasticsearch

```bash
python upload_to_es.py
```

**Expected Output:**
```
📂 Loaded 100 incident tickets from CSV
✅ Data prepared for Elasticsearch
✅ Indexed 100 records to Elasticsearch

🎉 Upload complete! 100 incident tickets indexed to incident_tickets_uploaded
```

### Step 3: Verify Data

```bash
python verify_es.py
```

**This displays:**
- Index existence status
- Total document count
- Sample document structure
- Statistics by ticket status

## 🔄 Data Pipeline

### Input Data Schema (CSV)

**Base Fields:**
- Ticket Class, Priority, Number, Status
- Opened Date, Resolved Date, Closed Date
- Hostname, Queue ID, Summary
- Resolution Code, Closure Code
- Assignment details

**Enriched Fields (Added by Pipeline):**
- `SLA Breach`: 0/1 flag for missed targets
- `Opened Weekday`: Day of week ticket was opened
- `Opened Hour`: Hour of day (0-23)
- `Opened Month`: Month (1-12)
- `Opened Quarter`: Quarter (1-4)
- `First Response Time (min)`: Time to first response
- `Escalation Level`: L1, L2, L3, etc.
- `Automation Success`: yes/no flag
- `Impact Level`: low/medium/high

### Output Schema (Elasticsearch)

All **32 fields** are indexed with proper data types:
- **Text fields**: Analyzed for full-text search
- **Keyword fields**: Exact match and aggregations
- **Date fields**: Time-based analysis
- **Numeric fields**: Statistical analysis
- **Boolean fields**: Filters and aggregations

## 📁 Project Structure

```
Elastic_MiniProject_Monday/
├── .gitignore                    # Git ignore rules
├── README.md                     # This file
├── requirements.txt              # Python dependencies
├── .env.sample                   # Environment template
├── .env                          # Environment config (not in repo)
│
├── dummy_incident_tickets.csv    # Raw input data
├── cleaned_enriched_incident_tickets_updated_for_visualization.csv  # Processed data
│
├── dataClean.py                  # Data cleaning and enrichment
├── upload_to_es.py               # Elasticsearch upload script
├── utils.py                      # Utility functions (ES client)
├── verify_es.py                  # Data verification script
│
└── data/                         # Local data directory (git ignored)
```

## 🌳 Branching Strategy

This project follows Git Flow branching model:

### Branches:

| Branch | Purpose | Stability |
|--------|---------|-----------|
| **`main`** | Production-ready code | 🟢 Stable |
| **`stage`** | Pre-production testing | 🟡 Testing |
| **`dev`** | Active development | 🔴 Development |

### Workflow:

```
dev → stage → main
```

1. **Development** in `dev` branch
2. **Testing** in `stage` branch
3. **Production** deployment from `main` branch

### Pull Request Process:

1. Create feature branch from `dev`
2. Complete development and testing
3. Create PR: `feature` → `dev`
4. After testing, create PR: `dev` → `stage`
5. After validation, create PR: `stage` → `main`
6. Tag release in `main`

## 📌 Version History

### Version 0.1.0 (Initial Setup)
**Tag**: `v0.1.0`  
**Branch**: `dev`  
**Files Added:**
- requirements.txt
- utils.py
- .env.sample

**Description**: Initial project setup with utilities and dependencies

### Version 0.2.0 (Data Cleaning)
**Tag**: `v0.2.0`  
**Branch**: `dev`  
**Files Added:**
- dataClean.py

**Description**: Data cleaning and enrichment pipeline implementation

### Version 0.3.0 (ES Upload)
**Tag**: `v0.3.0`  
**Branch**: `dev`  
**Files Added:**
- upload_to_es.py

**Description**: Elasticsearch upload functionality with NaN handling

### Version 0.4.0 (Verification)
**Tag**: `v0.4.0`  
**Branch**: `dev`  
**Files Added:**
- verify_es.py

**Description**: Data verification and validation tools

### Version 1.0.0 (Production Release)
**Tag**: `v1.0.0`  
**Branch**: `main`  
**Description**: First production-ready release with complete ETL pipeline

## 🛠️ Development

### Running Tests

```bash
# Test data cleaning
python dataClean.py

# Test Elasticsearch upload
python upload_to_es.py

# Verify data in Elasticsearch
python verify_es.py
```

### Code Quality

- Follow PEP 8 style guide
- Add docstrings to all functions
- Include type hints where appropriate
- Write clear commit messages

### Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Maintenance tasks

**Example:**
```
feat(enrichment): Add SLA breach detection

- Implement SLA breach flag calculation
- Add target date validation
- Update documentation

Closes #123
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'feat: Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📊 Data Quality Metrics

The pipeline ensures:
- ✅ 100% data completeness (all fields preserved)
- ✅ Duplicate removal by ticket number
- ✅ Date validation and formatting
- ✅ Numeric field validation
- ✅ NaN/null handling for JSON compatibility
- ✅ Categorical field normalization

## 🔍 Troubleshooting

### Common Issues:

**Issue**: `ValueError: Please set ES_ENDPOINT and ES_API_KEY`
- **Solution**: Ensure `.env` file exists with valid credentials

**Issue**: NaN parsing errors in Elasticsearch
- **Solution**: The pipeline now handles this automatically (v0.3.0+)

**Issue**: No data in Elasticsearch
- **Solution**: Run `python verify_es.py` to check connection and index status

## 📞 Support

For issues or questions:
- Check the [documentation](#usage)
- Review [troubleshooting](#troubleshooting)
- Open an issue on GitHub

## 👤 Author

**Arkaprava Maiti**
- GitHub: [@arkapravamaiti](https://github.com/arkapravamaiti)
- Repository: [Elastic_MiniProject_Monday](https://github.com/arkapravamaiti/Elastic_MiniProject_Monday)

## 📅 Project Timeline

- **Created**: November 5, 2025
- **Last Updated**: November 5, 2025
- **Status**: Active Development

---

**Note**: This project demonstrates ETL pipeline concepts, data processing with Python, and integration with Elasticsearch for enterprise-grade data analytics.

**License**: Educational Use

---

Made with ❤️ for learning and demonstration purposes
