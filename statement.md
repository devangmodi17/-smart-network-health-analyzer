# Smart Network Health Analyzer

## 1. Problem Statement

Network problems such as slow response, high latency, and packet loss can affect internet performance. It is often difficult for a normal user to understand the actual condition of a network connection.

The Smart Network Health Analyzer is a Python-based command-line system that checks network connectivity and performance, calculates an overall health score, and provides a simple diagnosis of possible network problems.

## 2. Scope

The project focuses on basic network monitoring and diagnostic analysis. It measures latency and packet loss, evaluates network health, identifies possible problems using predefined rules, and stores previous test results for later analysis.

## 3. Target Users

- Students and beginners who want to understand basic network performance.
- Home users who want to check their network condition.
- Users who need a simple command-line network diagnostic tool.

## 4. High-Level Features

1. Network information checking
2. Internet connectivity testing
3. Network performance analysis
4. Network health score calculation
5. Rule-based network diagnosis
6. Network history storage and summary
7. Continuous network monitoring

## 5. Non-Functional Requirements

1. Performance
   The system should provide network analysis results within a reasonable time.

2. Reliability
   The system should handle network testing errors without crashing.

3. Usability
   The command-line interface should be simple and easy to understand for beginners.

4. Maintainability
   The project should use separate modules so that individual components can be modified easily.

5. Portability
   The project should be structured so that it can be adapted to other operating systems in future.

6. Data Integrity
   Network history should be stored in a structured format without losing previously recorded results.

## 6. Functional Requirements

1. The system shall display a main menu for selecting network analysis operations.

2. The system shall collect basic network information such as hostname and IP address.

3. The system shall test internet connectivity using a network ping test.

4. The system shall measure network latency and packet loss.

5. The system shall calculate a network health score based on measured network performance.

6. The system shall classify the network condition as Healthy, Moderate, Poor, or Critical.

7. The system shall identify possible network problems using predefined diagnostic rules.

8. The system shall provide recommendations based on detected network conditions.

9. The system shall save network analysis results in a history file.

10. The system shall display previous network results and provide a history summary.

11. The system shall support continuous network monitoring at regular intervals.

12. The system shall allow the user to exit the application through the main menu.

## 7. Design Decisions and Rationale

### Modular Structure

The project is divided into separate Python modules such as network information, connectivity, performance, health score, diagnosis, history, and monitoring. This makes the project easier to understand, test, and maintain.

### Command-Line Interface

A command-line interface was selected because it is simple, lightweight, and suitable for a Python Essentials project. It also allows the complete application to be executed through the terminal.

### Rule-Based Health Analysis

Predefined rules are used to calculate the network health score and identify possible problems. This makes the analysis understandable and easy to modify.

### JSON History Storage

JSON is used to store previous network results because it is simple, structured, and supported by Python's standard library without requiring an external database.

### Continuous Monitoring

A separate monitoring module was included to repeatedly collect network measurements and store the results. This adds a monitoring feature beyond a single network test.



## 8. Implementation Details

The project is implemented using Python and follows a modular programming approach. The main program controls the menu and coordinates the different modules.

### Main Components

- `main.py` — Controls the application menu and connects the different modules.
- `network_info.py` — Collects basic network information.
- `connectivity.py` — Tests internet connectivity.
- `network_data.py` — Collects latency and packet loss data.
- `performance.py` — Analyzes network performance.
- `health_score.py` — Calculates the network health score and status.
- `diagnosis.py` — Identifies possible network problems and provides recommendations.
- `history.py` — Saves and displays previous network results.
- `monitor.py` — Performs continuous network monitoring.
- `test_analyzer.py` — Contains unit tests for important health score functions.

### Data Storage

Network results are stored in `history.json`. Each record contains the test time, latency, packet loss, health score, and health status.

### Error Handling

The application handles common situations such as network test timeouts, unavailable ping commands, missing history files, and unavailable network data without immediately terminating the program.

### Testing

The project uses Python's built-in `unittest` framework. The test suite checks health score calculation and health status classification.

## 9. Challenges Faced

### Network Data Collection

Collecting network information and performance data through system commands required handling different command outputs and possible errors.

### Network Connectivity Issues

Network tests may produce different results depending on the current internet connection, network congestion, or firewall settings.

### Data Parsing

The program needed to extract useful latency and packet loss values from the output of the ping command.

### Modularization

The initial version of the project was developed in a single Python file. It was later divided into separate modules to improve organization and maintainability.

### Continuous Monitoring

Implementing continuous monitoring required repeated network tests, timed intervals, and a safe way for the user to stop monitoring.


## 10. Learnings and Key Takeaways

During the development of this project, the following concepts were learned:

- Using Python modules to organize a larger program.
- Working with system commands using Python.
- Collecting and processing network performance data.
- Using conditional statements for rule-based analysis.
- Calculating and interpreting a health score.
- Storing structured data using JSON.
- Handling errors and exceptional situations.
- Using loops for continuous monitoring.
- Writing and executing unit tests.
- Organizing a project for GitHub and version control.

## 11. Future Enhancements

The project can be improved in the future by adding:

- Cross-platform support for Windows, Linux, and macOS.
- A graphical user interface for easier visualization.
- Network performance graphs and charts.
- More detailed network statistics.
- Additional diagnostic rules.
- Exporting network reports in PDF or CSV format.
- Database support for storing larger amounts of history.
- Email or notification alerts for serious network problems.


## 12. References

- Python Documentation — https://docs.python.org/3/
- Python `subprocess` module documentation — https://docs.python.org/3/library/subprocess.html
- Python `json` module documentation — https://docs.python.org/3/library/json.html
- Python `unittest` documentation — https://docs.python.org/3/library/unittest.html
