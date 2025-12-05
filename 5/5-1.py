from os import chdir, path

def main():
    chdir(path.realpath(path.dirname(__file__)))
    fresh_ids = set()
    available_ids = set()
    with open('./test.txt', 'r') as f:
        while (line := f.readline()) != "\n": # Read lines until finding an empty one
            start, stop = line.split("-")
            fresh_ids.update(range(int(start), int(stop)+1))

        while (line := f.readline()) != "": # Read lines until EOF
            available_ids.add(int(line.strip("\n")))
    fresh_and_available = fresh_ids.intersection(available_ids)
    print(len(fresh_and_available))

if __name__ == "__main__":
    main()