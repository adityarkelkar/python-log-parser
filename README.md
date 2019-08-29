# Python Log Parser
This is a self made project to parse log files with a python script

### Specification
- The main idea of this project is to find ways to parse a log file and extract meaningful data from it
- There is a sample log file provided which I will attempt to parse to extract data like IP addressed, request types etc

### Parse function
- Sample parse file defines 3 functions here
    1. **Read file**: Read a sample log file and extract all IP addresses mentioned using a regular expression
    2. **Count IP**: Count the frequency of each IP
    3. **Create CSV**: Gather data from the above two functions and export it to a CSV file