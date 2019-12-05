import csv


def create_csv(filename, string, l):
    """Create csv files"""
    with open("Results/" + filename, "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=",")

        writer.writerow([string, l])


def create_csv_list(filename, string, l):
    """Create csv files and arrange the contents in list format"""
    with open("Results/" + filename, "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=",")

        writer.writerow([string])
        for element in sorted(l):
            writer.writerow([element])


def create_csv_dictionary(filename, string, d):
    """Create csv files and arrange the contents in dictionary format"""
    with open("Results/" + filename, "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=",")

        writer.writerow([string])
        for key, value in sorted(d.items()):
            writer.writerow([key, value])