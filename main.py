import os


path = 'gts_data'
test_dirs = [e.path for e in os.scandir(path) if e.is_dir()]

