#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for atrib in dir(hidden_4):
        if atrib[0] and atrib[1] != '_':
            print("{}".format(atrib))
