import os
import argparse

def generate_graphviz_tree(root_path):
    graph = ['digraph G {']

    def traverse_directory(directory):
        nonlocal graph
        files = os.listdir(directory)
        for file in files:
            file_path = os.path.join(directory, file)
            if os.path.isdir(file_path):
                graph.append(f'"{os.path.basename(directory)}" -> "{file}" [color=blue];')
                graph.append(f'"{file}" [shape=folder];')
                traverse_directory(file_path)
            else:
                graph.append(f'"{os.path.basename(directory)}" -> "{file}" [color=green];')
                graph.append(f'"{file}" [shape=file];')

    traverse_directory(root_path)
    graph.append('}')

    return '\n'.join(graph)

def main():
    parser = argparse.ArgumentParser(description='Generate directory tree in Graphviz format')
    parser.add_argument('path', help='Root path to start generating tree')

    args = parser.parse_args()

    if not os.path.exists(args.path):
        print("Path doesn't exist.")
        return

    graph = generate_graphviz_tree(args.path)
    print(graph)

if __name__ == "__main__":
    main()
