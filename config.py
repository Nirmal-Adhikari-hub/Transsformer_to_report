from pathlib import Path
import sys

def get_config():
    return{

        "batch_size": 8,
        "num_epochs": 20,
        "lr": 1e-6,
        "seq_len": 350,
        "d_model": 512,
        "datasource": "msarmi9/korean-english-multitarget-ted-talks-task",
        "lang_src": "english",
        "lang_tgt": "korean",
        "model_folder": "weights",
        "model_basename": "tmodel_",
        # "preload": "latest",
        # "preload": "tmodel_02.pt",
        "preload": None,
        "tokenizer_file": "tokenizer_{0}.json",
        "experiment_name": "runs/tmodel"
    }


def get_weights_file_path(config, epoch: str):
    model_folder = config['model_folder']
    model_basename = config['model_basename']
    model_filename = f"{model_basename}{epoch}.pt"
    # return str(Path("config.py").resolve().parent.parent / model_folder / model_filename)///
    return str(Path('.') / model_folder / model_filename)


def latest_weights_file_path(config):
    model_folder = f"{config['datasource']}_{config['model_folder']}"
    model_filename = f"{config['model_basename']}*"
    weights_files = list(Path(model_folder).glob(model_filename))
    if len(weights_files) == 0:
        return None
    weights_files.sort()
    return str(weights_files[-1])