import os
import re
import yaml


def remove_keys(string, keys=["[PDF]", "[PPT]"]):
    for key in keys:
        string = string.replace(key, "")
    string = string.replace("  ", " ")
    return string

def unicode_quote_to_ascii_quote(line):
    line = re.sub(u'\u201c','"',line)
    line = re.sub(u'\u201d','"',line)
    return line
    

def string_to_dic(line):
    template = {
        "title": "asdf",
        "image": "",
        "description": "",
        "authors": "",
        "link": {
            "url": "",
            "display": ""
        },
        "highlight": 0
    }
    cnt = line.count('"')
    assert cnt == 2, f"There should be only one pair of quotations. But found: {cnt}"
    authors, title, display = line.split('"')
    
    template['authors'] = authors.strip().strip(',')
    template['title'] = title.strip().strip(',')
    template['link']['display'] = remove_keys(display).strip().strip(',')
    return template


def get_bib_file_paths_in(dir_path):
    file_paths = []
    for file in os.listdir(dir_path):
        if file.endswith(".bib"):
            file_paths.append(os.path.join(dir_path, file))
    return file_paths


if __name__ == "__main__":
    # Get bib files
    bib_paths = get_bib_file_paths_in("./bibs")
    
    # Create dump directory
    if not os.path.exists("./yamls"):
        os.mkdir("./yamls")
    
    # For all bib files
    for file_path in bib_paths:
        dics = []
        # Read in and create dictionary
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = [unicode_quote_to_ascii_quote(line) for line in f.readlines()]
            line_cnt = 0
            for line in lines:
                try:
                    dics.append(string_to_dic(line))
                except Exception as e:
                    print(e)
                    print(f"Check: {file_path} line: {line_cnt+1}")
                line_cnt += 1
        
        # Dump as yaml
        if line_cnt == len(lines):
            # Change directory
            out_path = file_path.replace("bibs/", "yamls/")
            # Change file extension
            out_path = out_path.replace(".bib", ".yml")
            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(yaml.dump(dics, default_flow_style=False, allow_unicode=True))
        else:
            print(f"Skipping: {file_path}\n")

    print("Done!")