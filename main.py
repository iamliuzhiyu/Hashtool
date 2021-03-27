import hashlib
while True:
    try:
        text = input("请输入要进行hash操作的文本：")
    except KeyboardInterrupt:
        exit()
    output = hashlib.sha256(text.encode("utf-8")).hexdigest()
    print("sha256: " + output)
    output = hashlib.sha512(text.encode("utf-8")).hexdigest()
    print("sha512: " + output)
    output = hashlib.sha384(text.encode("utf-8")).hexdigest()
    print("sha384: " + output)
    output = hashlib.sha224(text.encode("utf-8")).hexdigest()
    print("sha224: " + output)
    output = hashlib.sha1(text.encode("utf-8")).hexdigest()
    print("sha1: " + output)
    output = hashlib.md5(text.encode("utf-8")).hexdigest()
    print("md5: " + output)