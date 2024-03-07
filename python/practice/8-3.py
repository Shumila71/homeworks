import sys
import re

def process_quotes(text):
    in_code_block = False
    lines = text.split('\n')
    new_lines = []

    for line in lines:
        if line.strip().startswith('```'):
            in_code_block = not in_code_block

        if in_code_block:
            new_lines.append(line)
        else:
            new_line = re.sub(r'(?<!`)\"(.*?)\"(?!`)', r'«\1»', line)
            new_line = re.sub(r"(?<!`)'(.*?)'(?!`)", r'«\1»', new_line)
            new_lines.append(new_line)

    return '\n'.join(new_lines)

def main():
    if len(sys.argv) == 1:  
        text = sys.stdin.read()
        processed_text = process_quotes(text)
        print(processed_text)
    elif len(sys.argv) == 2:  
        file_name = sys.argv[1]
        with open(file_name, 'r',encoding='UTF-8') as file:
            text = file.read()
        processed_text = process_quotes(text)
        with open(file_name[:-3] + '_processed.md', 'w',encoding='UTF-8') as file:  
            file.write(processed_text)
        print("Файл обработан успешно.")
    else:
        print("Использование: python script.py [имя_файла.md]")

if __name__ == "__main__":
    main()
