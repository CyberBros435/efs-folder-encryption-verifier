import subprocess

target_folder = r"D:\SOC_Projects\Assignment_Folder"

result = subprocess.run(
    ["cipher", "/c", target_folder],
    capture_output=True,
    text=True
)

print(result.stdout)     # what cipher printed — the real report
# print(result.returncode) # 0 = success, non-zero = failed
# print(result.stderr)     # error text, if any

# print(result.stderr)
# print(result.returncode)
# print(result.stdout)