import zipfile, os

mode = input().strip().lower()
if mode == "zip":
    src = input().strip()
    dst = input().strip() or "archive.zip"
    with zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED) as z:
        if os.path.isdir(src):
            for root, _, files in os.walk(src):
                for f in files:
                    p = os.path.join(root, f)
                    z.write(p, os.path.relpath(p, src))
        else:
            z.write(src, os.path.basename(src))
    print("Đã nén vào", dst)
elif mode == "unzip":
    zf = input().strip()
    out = input().strip() or "."
    with zipfile.ZipFile(zf, "r") as z:
        z.extractall(out)
    print("Đã giải nén vào", out)
else:
    print("Chọn zip hoặc unzip")
