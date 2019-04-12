import sys

print("Hello, Circle CI!")

if len(sys.argv) > 1:
    print("I think the secret is %s % sys.argv[1]")
