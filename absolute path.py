def absolute_file_path(path_fname):
    import os
    return os.path.abspath('path_fname')
print('absolute file path',absolute_file_path('access env var.py'))