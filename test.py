import sys
import requests
import sleekxmpp

print("Hello, Circle CI!")

if len(sys.argv) > 1:
    print("I think the secret is %s" % sys.argv[1])

r = requests.get('https://lil.law.harvard.edu/')
print(r.status_code)
# print(r.text)
