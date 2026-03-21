import csv
import sys
import os
import matplotlib.pyplot as plt

def process_csv(file_path):
    dates = []
    values = []
    total = 0

    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)

        for row in reader:
            if not row or len(row) < 2:
                continue
            try:
                date = row[0]
                value = float(row[1])

                dates.append(date)
                values.append(value)

                total += value
            except ValueError:
                continue

    average = total / len(values) if values else 0

    return dates, values, total, average


def write_report(total, average):
    os.makedirs("output", exist_ok=True)

    with open("output/sales_summary.txt", "w") as f:
        f.write(f"Total: {total}\n")
        f.write(f"Average: {average}\n")


def create_chart(dates, values):
    os.makedirs("output", exist_ok=True)

    plt.figure()
    plt.plot(dates, values, marker='o')
    plt.title("Sales Over Time")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig("output/sales_trend.png")
    plt.close()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <csv_file>")
        sys.exit(1)

    file_path = sys.argv[1]

    dates, values, total, average = process_csv(file_path)

    write_report(total, average)
    create_chart(dates, values)

    print("Report and chart generated in output/")