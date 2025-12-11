from os import chdir, path

def main():
    chdir(path.realpath(path.dirname(__file__)))
    with open('./input.txt', 'r') as f:
        

if __name__ == "__main__":
    main()