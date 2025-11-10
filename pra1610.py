from urllib import request

with request.urlopen("https://api.github.com") as f:
    data = f.read()
    print("Status:", f.status, f.reason)
    for k, v in f.getheaders():
        print(f"{k}:{v}")
    print("Data:", data.decode("utf-8"))
