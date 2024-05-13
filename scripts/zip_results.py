"""
# Zip "Embedding Model + NoReranker" search results in <search_results>/<model_name>/NoReranker to <save_path>/<md5>.zip.
python zip_results.py \
--results_path search_results \
--model_name bge-m3 \
--save_path search_results/zipped_results

# Zip "Embedding Model + Reranker" search results in <search_results>/<model_name>/<reranker_name> to <save_path>/<md5>.zip.
python zip_results.py \
--results_path search_results \
--model_name bge-m3 \
--reranker_name bge-reranker-v2-m3 \
--save_path search_results/zipped_results
"""
import os
import zipfile
import hashlib
import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--results_path', type=str, required=True, help="Path to the search results directory")
    parser.add_argument('--model_name', type=str, required=True, help="Model name used for the search")
    parser.add_argument('--reranker_name', type=str, default='NoReranker', help="Reranker name used for the search. Default: NoReranker")
    parser.add_argument('--save_path', type=str, required=True, help="Path to the directory to save the zipped search results")
    parser.add_argument('--overwrite', action='store_true', help="Overwrite the existing zipped file if it exists")
    return parser.parse_args()


def calculate_folder_md5(folder_path):
    md5 = hashlib.md5()

    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'rb') as f:
                while True:
                    data = f.read(4096)
                    if not data:
                        break
                    md5.update(data)

    return md5.hexdigest()


def zip_results(results_path: str, save_path: str, overwrite: bool = False):
    md5 = calculate_folder_md5(results_path)
    
    os.makedirs(save_path, exist_ok=True)
    zip_filename = os.path.join(save_path, f'{md5}.zip')
    
    if os.path.exists(zip_filename) and not overwrite:
        print(f"Zipped file {zip_filename} already exists.\n")
        return False
    
    try:
        print("Zipping search results...")
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(results_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, results_path))
    except Exception as e:
        print(f"Failed to zip search results in {results_path}: {e}\n")
        return False
    
    print(f"Zip search results in {results_path} to {zip_filename}.\n")
    return True


def main():
    args = get_args()
    
    print("=========================================")
    results_path = os.path.join(args.results_path, args.model_name, args.reranker_name)
    success = zip_results(results_path, args.save_path, overwrite=args.overwrite)
    print("=========================================")
    if success:
        print("Success! Now you can upload the zipped search results to the 🤗  Hugging Face Leaderboard!")
    else:
        print("Failed! Please check the error message and try again!")


if __name__ == '__main__':
    main()
