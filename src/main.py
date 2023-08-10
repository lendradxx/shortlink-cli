import lib.shortener as shortener, argparse

if __name__ == '__main__':
    argument = argparse.ArgumentParser()
    argument.add_argument('url', help='URL to shorten')
    
    args = argument.parse_args()
    print(f"Original URL: {args.url}")
    print(f"Shorten URL: {shortener.tinyurl(args.url)}")