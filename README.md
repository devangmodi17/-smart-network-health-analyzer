# Smart Network Health Analyzer

## Overview

Smart Network Health Analyzer is a Python-based command-line application designed to check and analyze basic network performance.

The system collects network information, tests connectivity, measures latency and packet loss, calculates a network health score, identifies possible network issues, and stores previous results for analysis.

## Features

- Network information checking
- Internet connectivity testing
- Latency and packet loss analysis
- Network health score calculation
- Rule-based network diagnosis
- Network history storage
- Network history summary
- Continuous network monitoring
- Command-line interface

## Technologies Used

- Python 3
- Python Standard Library
- JSON
- Git and GitHub
- Visual Studio Code

## Project Structure

programming/
│
├── main.py
├── history.json
├── requirements.txt
├── statement.md
├── README.md
├── .gitignore
│
├── modules/
│   ├── network_info.py
│   ├── connectivity.py
│   ├── network_data.py
│   ├── performance.py
│   ├── health_score.py
│   ├── diagnosis.py
│   ├── history.py
│   └── monitor.py
│
└── tests/
    └── test_analyzer.py

## Requirements

- Python 3.x
- Windows operating system
- Command Prompt or PowerShell
- Internet/network connection for network testing

No external Python packages are required.

## Configuration

The project does not require any external API keys or configuration files.

The application uses the system's network connection and the Windows `ping` command for network testing.

No external Python packages are required.


## How to Run

### 1. Open the project folder

Open the project folder in Visual Studio Code.

### 2. Open the terminal

Open:

Terminal → New Terminal

### 3. Run the application

python main.py

### 4. Select an option

Use the displayed menu to select the required network analysis operation.

## Testing

The project includes unit tests for the health score and status calculation.

Run the tests using:

python -m unittest discover tests

All implemented tests should pass successfully.

## Health Score

The application calculates a network health score between 0 and 100 using latency and packet loss.

The project uses predefined rules to classify the network as:

- Healthy
- Moderate
- Poor
- Critical

These thresholds are project-defined rules for analysis.

## Future Enhancements

- Support for multiple operating systems
- Graphical dashboard
- More detailed network statistics
- Network performance graphs
- Additional diagnostic rules
- Exporting reports in different formats

## Author

Developed as a Python Essentials project.