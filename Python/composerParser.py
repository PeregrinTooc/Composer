def parse(source, target):
    with open(source, 'r') as source:
        with open(target, 'w') as target:
            composers = list(source)
            for item in composers:
                target.write(item[:-10]+'\n')


if __name__ == "__main__":
    import sys
    parse(int(sys.argv[0], sys.argv[1]))
