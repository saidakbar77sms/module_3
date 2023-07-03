strs = ["alic3","bob","3","4","00000"]
k = 0
for i in strs:
    if i.isdigit():
        if float(i) > k:
            k = int(i)
    elif len(i) > k:
        k = len(i)

print(k)
"""
sudo apt-get install git
git init
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/saidakbar77sms/Test.git
git push -u origin main
"""
