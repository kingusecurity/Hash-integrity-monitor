# Directory Integrity Monitor

A beginner-friendly cybersecurity project built with Python that generates hashes, creates directory baselines, and detects file changes through integrity monitoring.

This project introduces real-world defensive security concepts used in File Integrity Monitoring (FIM) systems.

---

# Features

## Hash Generation

- MD5 hashing
- SHA256 hashing
- Fast text hashing

## Directory Baseline Creation

- Scan entire directories
- Create file integrity baselines
- Store hashes automatically

## Integrity Verification

Detect:

- Modified files
- Deleted files
- New files

## Logging System

- Timestamped logs
- Change tracking
- Verification history

## User Interface

- Colored terminal output
- Menu-driven design
- Beginner-friendly workflow

---

# Technologies Used

- Python 3
- hashlib
- os
- colorama
- datetime

---

# Project Structure

```text
directory-integrity-monitor/
│
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
├── hash_database.txt
├── hash_log.txt
└── screenshots/
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/kingusecurity/directory-integrity-monitor.git
```

## Move Into Project

```bash
cd directory-integrity-monitor
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# How To Run

```bash
python main.py
```

---

# Menu

```text
1. Generate MD5 Hash
2. Generate SHA256 Hash
3. Create Directory Baseline
4. Verify Directory Integrity
5. Exit
```

---

# Example Workflow

## Create Baseline

Directory:

```text
lab/
├── file1.txt
└── file2.txt
```

Run:

```text
3
```

Enter:

```text
lab
```

Baseline is created.

---

## Modify Files

Change:

```text
file1.txt
```

Delete:

```text
file2.txt
```

Create:

```text
file3.txt
```

---

## Verify Integrity

Run:

```text
4
```

Enter:

```text
lab
```

Example Output:

```text
MODIFIED: lab\file1.txt
DELETED: lab\file2.txt
NEW FILE: lab\file3.txt
```

---

# Cybersecurity Concepts Learned

- Hashing
- SHA256
- MD5
- File Integrity Monitoring
- Baselines
- Tamper Detection
- Change Detection
- Host-Based Security

---

# Python Concepts Learned

- Functions
- File Handling
- Hashlib
- os.walk()
- Dictionaries
- Logging
- Error Handling

---

# Real-World Applications

Similar concepts are used in:

- Host Intrusion Detection Systems
- Security Monitoring
- Malware Detection
- Digital Forensics
- Incident Response

---

# Future Improvements

- Recursive report generation
- Export to CSV
- Email alerts
- Real-time monitoring
- SQLite database storage
- GUI dashboard

---

# Screenshot

```markdown
![Tool Screenshot](screenshots/tool.png)
```

---

# Author

GitHub:

https://github.com/kingusecurity

---

# License

Open-source and intended for educational purposes.