import glob
from os.path import dirname, isfile

def __list_all_models():
    work_dir = dirname(__file__)
    mod_paths = glob.glob(work_dir + "/*.py")

    all_models = [
        (f.replace(work_dir, "").replace("/", ".")[:-3])
        for f in mod_paths
        if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
    ]
    return all_models

ALL_MODELS = sorted(__list_all_models())
__all__ = ALL_MODELS + ["ALL_MODELS"]
