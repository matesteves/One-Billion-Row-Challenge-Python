from csv import reader
from collections import defaultdict, Counter
from tqdm import tqdm  # progress bar
import time

NUMBER_OF_LINES = 1_000_000_000

def process_temperatures(csv_path):
    # using positive and negative infinity for comparison
    min_temps = defaultdict(lambda: float('inf'))
    max_temps = defaultdict(lambda: float('-inf'))
    sums = defaultdict(float)
    measurements = Counter()

    with open(csv_path, 'r', encoding='utf-8') as file:
        _reader = reader(file, delimiter=';')
        # using tqdm directly on the iterator to show progress percentage
        for row in tqdm(_reader, total=NUMBER_OF_LINES, desc="Processing"):
            station_name, temperature = str(row[0]), float(row[1])
            measurements.update([station_name])
            min_temps[station_name] = min(min_temps[station_name], temperature)
            max_temps[station_name] = max(max_temps[station_name], temperature)
            sums[station_name] += temperature

    print("Data loaded. Calculating statistics...")

    # calculating min, mean, and max for each station
    results = {}
    for station, count in measurements.items():
        mean_temp = sums[station] / count
        results[station] = (min_temps[station], mean_temp, max_temps[station])

    print("Statistics calculated. Sorting...")
    # sorting results by station name
    sorted_results = dict(sorted(results.items()))

    # formatting results for display
    formatted_results = {station: f"{min_temp:.1f}/{mean_temp:.1f}/{max_temp:.1f}"
                         for station, (min_temp, mean_temp, max_temp) in sorted_results.items()}

    return formatted_results


if __name__ == "__main__":
    csv_path = "data/measurements.txt"

    print("Starting file processing.")
    start_time = time.time()  # Start time

    results = process_temperatures(csv_path)

    end_time = time.time()  # End time

    for station, metrics in results.items():
        print(station, metrics, sep=': ')

    print(f"\nProcessing completed in {end_time - start_time:.2f} seconds.")