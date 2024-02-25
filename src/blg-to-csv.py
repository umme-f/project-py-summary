import pandas as pd
import os

# Function to convert BLG to CSV
def blg_to_csv(blg_file, output_folder):
    # Read BLG file
    data = pd.read_csv(blg_file, delimiter='\t')

    # Extract file name without extension
    file_name = os.path.splitext(os.path.basename(blg_file))[0]

    # Define CSV file path
    csv_file = os.path.join(output_folder, file_name + '.csv')

    # Save as CSV
    data.to_csv(csv_file, index=False)
    print(f"Converted {blg_file} to {csv_file}")

def main():
    # Input folder containing BLG files
    input_folder = 'data/input_blgs'

    # Output folders to save CSV files
    output_folders = {
        'cpu': 'output/cpu_data',
        'memory': 'output/memory_data',
        'network': 'output/network_data'
    }

    # Create output folders if they don't exist
    for folder in output_folders.values():
        os.makedirs(folder, exist_ok=True)

    # Iterate through BLG files in the input folder
    for file in os.listdir(input_folder):
        if file.endswith('.blg'):
            blg_file = os.path.join(input_folder, file)
            # Determine the type of data and select the corresponding output folder
            if 'cpu' in file.lower():
                output_folder = output_folders['cpu']
            elif 'memory' in file.lower():
                output_folder = output_folders['memory']
            elif 'network' in file.lower():
                output_folder = output_folders['network']
            else:
                print(f"Unknown data type for file: {file}")
                continue
            blg_to_csv(blg_file, output_folder)

if __name__ == "__main__":
    main()
