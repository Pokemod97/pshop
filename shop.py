import argparse
import PIL

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", help="choose photo mode")
    pictures = parser.add_mutually_exclusive_group()
    
if __name__ == '__main__':
    main()
