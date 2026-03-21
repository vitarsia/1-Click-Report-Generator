import csv
import sys
import os

def process_csv(file_path):
    total = 0
    count = 0

    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # skip header

        for row in reader:
            if not row or len(row) < 2:
                continue
            try:
                value = float(row[1])
                total += value
                count += 1
            except ValueError:
                continue

    average = total / count if count > 0 else 0

    return total, average


def write_report(total, average):
    os.makedirs("output", exist_ok=True)
    with open("output/report.txt", "w") as f:
        f.write(f"Total: {total}\n")
        f.write(f"Average: {average}\n")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <csv_file>")
        sys.exit(1)

    file_path = sys.argv[1]

    total, average = process_csv(file_path)
    write_report(total, average)

    print("Report generated in output/report.txt")