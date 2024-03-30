def main():
    convert(input("File name: "))

def convert(ext):
    ext= ext.lower().strip()
    if ext.find("gif")>=0:
        print("image/gif")
    elif ext.find("jpg")>=0 or ext.find("jpeg")>=0:
        print("image/jpeg")
    elif ext.find("png")>=0:
        print("image/png")
    elif ext.find("zip")>=0:
        print("application/zip")
    elif ext.find("txt")>=0:
        print("text/plain")
    elif ext.find("pdf")>=0:
        print("application/pdf")
    else:
          print("application/octet-stream")

main()