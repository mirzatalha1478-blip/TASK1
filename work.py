def read_html_file(filename):
    with open(filename, "r") as file:
        return file.read()

if __name__ == "__main__":
    content = read_html_file("index.html")
    print("HTML content 07 loaded:")
    print(content)