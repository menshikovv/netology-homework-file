import os

def merge_files(folder_path):
    file_list = os.listdir(folder_path)
    file_contents = {}

    for filename in file_list:
        with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
            lines = file.readlines()
            file_contents[filename] = lines

    sorted_files = sorted(file_contents.items(), key=lambda x: len(x[1]))

    with open(os.path.join(folder_path, 'result.txt'), 'w', encoding='utf-8') as result_file:
        for filename, lines in sorted_files:
            result_file.write(f"{filename}\n")
            result_file.write(f"{len(lines)}\n")
            result_file.writelines(lines)

def main():
    folder_path = 'files'
    merge_files(folder_path)
    print("Файлы успешно объединены. Проверьте «result.txt» в указанной папке.")

if __name__ == '__main__':
    main()
