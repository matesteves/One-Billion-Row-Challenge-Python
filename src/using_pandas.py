import pandas as pd
from multiprocessing import Pool, cpu_count
from tqdm import tqdm  # Import tqdm for progress bar

CONCURRENCY = cpu_count()  # Get the number of available CPU cores

total_rows = 1_000_000_000  # Known total number of rows
chunksize = 100_000_000  # Define the chunk size
filename = "data/measurements.txt"  # Ensure this is the correct file path

def process_chunk(chunk):
    # Aggregate data within the chunk using Pandas
    aggregated = chunk.groupby('station')['measure'].agg(['min', 'max', 'mean']).reset_index()
    return aggregated

def create_df_with_pandas(filename, total_rows, chunksize=chunksize):
    total_chunks = total_rows // chunksize + (1 if total_rows % chunksize else 0)
    results = []

    with pd.read_csv(filename, sep=';', header=None, names=['station', 'measure'], chunksize=chunksize) as reader:
        # Wrap the iterator with tqdm to visualize progress
        with Pool(CONCURRENCY) as pool:
            for chunk in tqdm(reader, total=total_chunks, desc="Processing"):
                # Process each chunk in parallel
                result = pool.apply_async(process_chunk, (chunk,))
                results.append(result)

            results = [result.get() for result in results]

    final_df = pd.concat(results, ignore_index=True)

    final_aggregated_df = final_df.groupby('station').agg({
        'min': 'min',
        'max': 'max',
        'mean': 'mean'
    }).reset_index().sort_values('station')

    return final_aggregated_df

if __name__ == "__main__":
    import time

    print("Starting file processing.")
    start_time = time.time()
    df = create_df_with_pandas(filename, total_rows, chunksize)
    took = time.time() - start_time

    print(df.head())
    print(f"Processing took: {took:.2f} sec")