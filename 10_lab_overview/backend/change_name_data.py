from pathlib import Path
from shutil import copytree, rmtree

raw_data_path = Path(__file__).parent / "raw_data"
cleaned_data_path = Path(__file__).parent / "cleaned_data"

if cleaned_data_path.is_dir():
    rmtree(cleaned_data_path)

cleaned_data_path.mkdir(parents=True, exist_ok=True)

for folder in raw_data_path.iterdir():
    new_name = folder.name.split()[0]
    copytree(folder, cleaned_data_path / new_name)

