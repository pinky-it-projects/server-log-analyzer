
# Server Log Analyzer

A Python project that analyzes server log files, counts ERROR and CRITICAL messages, identifies the most frequent error code, and generates a report.


## Features

- Read server log files (.log)
- Count ERROR and CRITICAL messages
- Identify the most frequent error code
- Save ERROR messages to error.txt
- Save CRITICAL messages to critical.txt
- Generate a summary report in rapport.txt
- Allow users to enter a log filename
- Handle missing files using try/except


## Requirements

- Python 3
- A terminal (PowerShell, Command Prompt, or Linux terminal)
- A text editor such as Visual Studio Code
- No external Python libraries required



## How to Run

1. Download or clone this repository.
2. Open the project folder in a terminal.
3. Make sure a log file such as `server.log` is in the project folder.
4. Run the following command:

   ```bash
   python analyzer.py
   ```

5. Enter the log filename when prompted:

   ```text
   Voer de bestandsnaam in: server.log
   ```

6. The program generates three output files:
   - `error.txt`
   - `critical.txt`
   - `rapport.txt`



## Example Output

When analyzing `server.log`, the program generates the following report in `rapport.txt`:

```text
ERROR: 27
CRITICAL: 8
Meeste voorkomende code: E404 : 10
```

The program also creates:
- `error.txt` — Contains all ERROR log entries.
- `critical.txt` — Contains all CRITICAL log entries.
- `rapport.txt` — Contains the summary report.



## Project Structure

```text
server-log-analyzer/
│
├── analyzer.py       # Main Python program
├── README.md         # Project documentation
├── server.log        # Main test log file
├── small_test.log    # Small test log file
├── error.txt         # Generated ERROR entries
├── critical.txt      # Generated CRITICAL entries
└── rapport.txt       # Generated summary report
```
