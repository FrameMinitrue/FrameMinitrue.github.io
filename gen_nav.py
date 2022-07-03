import os

def navigation(path):
    nav = "nav:\n"
    for root, dirs, files in os.walk(path):
        level = root.replace(path, '').count(os.sep)
        indent = ' ' * 2 * (level + 1)
        if root != "./docs/" and os.listdir(root):
            nav += indent + "- " + os.path.basename(root) + ": " + '\n'
        subindent = ' ' * 2 * (level + 2)
        for file in files:
            if root != "./docs/":
                nav += subindent + "- " + file[:-3] + ": \"" + root.replace('\\','/')[7:] + '/' + file + "\"\n"
            elif file == "index.md":
                nav += "  - 前言: \"" + file + "\"\n"
            else:
                nav += "  - " + file[:-3] + ": \"" + file + "\"\n"
    return nav

def replace_navigation():
    with open("mkdocs.yml", "r", encoding='utf8') as yml:
        lines = yml.readlines()
    with open("mkdocs.yml", "w", encoding='utf8') as yml:
        for line in lines:
            if line.startswith("nav:"):
                yml.write(navigation("./docs/"))
                break;
            else:
                yml.write(line)

if __name__ == "__main__":
    replace_navigation()
