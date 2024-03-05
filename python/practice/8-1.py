import os
import argparse

def ls(directory='.', show_hidden=False, long_format=False):
    files = os.listdir(directory)
    if not show_hidden:
        files = [f for f in files if not f.startswith('.')]
    files.sort()

    if long_format:
        for file in files:
            file_path = os.path.join(directory, file)
            file_stats = os.stat(file_path)
            print(f"{file_stats.st_mode:10o} {file_stats.st_nlink:3} {file_stats.st_uid:5} {file_stats.st_gid:5} {file_stats.st_size:10} {file} {file_stats.st_mtime}")
    else:
        print('\n'.join(files))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Analog of the ls command')
    parser.add_argument('directory', nargs='?', default='.', help='Directory to list (default: current directory)')
    parser.add_argument('-a', '--all', action='store_true', help='Show all files, including hidden files')
    parser.add_argument('-l', '--long', action='store_true', help='Use a long listing format')

    args = parser.parse_args()

    ls(args.directory, args.all, args.long)
