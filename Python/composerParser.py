from composer import composer
from composer import composerString


def parse(source, target):
    with open(source, 'r') as source:
        with open(target, 'w') as target:
            target.write("[\n")
            composers = list(source)
            for item in composers:
                composerObject = composer(composerString(item))
                print(composerObject)
                composerJson = composerObject.toJson().replace('\n', '')+',\n'
                print(composerJson)
                target.write(composerJson)
            target.write("]")


if __name__ == "__main__":
    import sys
    parse(sys.argv[0], sys.argv[1])
