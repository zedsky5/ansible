import sys
import re
import json
import numpy as np

def main():
    log_data = sys.stdin.read()
    pattern = re.compile(r"took (\d+) ms")

    # Find all matches in the input data and convert them to integers.
    timings = [int(x) for x in pattern.findall(log_data)]

    # Create dictionary to hold the results.
    results = {
        "mean": 0.0,
        "std_dev": 0.0,
        "line_count": len(timings),
        "timings_found": timings
    }

    # Perform calculations only if the 'timings' list is not empty.
    if timings:
        results["mean"] = round(np.mean(timings), 2)
        results["std_dev"] = round(np.std(timings), 2)

    # Ansible will use the results dictionary as a JSON formatted string.
    print(json.dumps(results))

if __name__ == "__main__":
    main()