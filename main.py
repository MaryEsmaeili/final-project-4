import json
from file_watcher import FileWatcher

def load_config(config_file):
    """Load configuration from a JSON file."""
    with open(config_file, 'r') as f:
        return json.load(f)

def main():
    config = load_config('application.json')
    watcher = FileWatcher(config)
    watcher.watch()

if __name__ == "__main__":
    main()
