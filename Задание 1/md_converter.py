import os
from sys import argv


def make_md(path):
    files_directory = []
    for file_dir, _, files in os.walk(path):
        for filename in files:
            if filename.endswith('.py') and filename != os.path.basename(__file__):
                with open(path + "/" + filename) as f:
                    if "# title" in f.read():
                        files_directory.append(os.path.join(file_dir, filename))

    md_path = path + "/" + path.split("/")[-1] + ".md"

    if os.path.exists(md_path):
        os.remove(md_path)

    if files_directory:

        f = open(md_path, 'a+')
        f.write("# " + path.split("/")[-1] + "\n\n")
        f.close()

        titles = []

        for curr_file in files_directory:
            f = open(curr_file)
            line = f.readline().replace("# title ", "") + "".replace("\n", "") + ""
            titles.append(line)
            f.close()

        for i in range(len(titles)):
            title = titles[i]
            titles[i] = f'+ [{title}](#{title})\n'
        titles = ''.join(titles)

        f = open(md_path, 'a+')
        f.write(titles)
        f.close()

        for current_file in files_directory:
            f = open(current_file)
            lines = f.readlines()

            for i in range(len(lines) - 1):
                line = lines[i]
                if line.startswith('# title'):
                    lines[i] = line.replace("# title", "\n##") + "\n"
                elif line.startswith('# description'):
                    lines[i] = line.replace("# description", "") + "\n"
                elif line.startswith('# code'):
                    lines[i] = '```python\n'
            lines.append('\n```\n')
            f = open(md_path, 'a+')
            f.write(''.join(lines))
            f.close()


if __name__ == "__main__":
    if len(argv) < 2:
        print("Укажите путь папки, где лежат .py файлы")
    else:
        file_directory = argv[1]
        if os.path.exists(file_directory) and os.path.isdir(file_directory):
            make_md(file_directory)
        else:
            print("Такой папки не существует")
