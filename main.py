# s = "Hello how are you Contestant"
# k = 4
# s = s.split()
# p = ""
# for i in s[:k]:
#     p += f"{i} "
# (p)

# def arithmeticTriplets(nums, diff):
#     q = []
#     w = []
#     count = 0
#     for i in nums:
#         if i == 0:
#             continue
#         if i + diff in nums:
#             # yield i
#             q.append(nums.index(i))
#             w.append(nums.index(i - diff))
#             nums.remove(i)
#             nums.remove(i + diff)
#             count += 1
#     if len(q) > 0 and len(w) > 0:
#         return count
#     return 0
# print(arithmeticTriplets([0, 2, 3], 1))
#
# sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
#
#
#
# # print(max([len(i.split()) for i in sentences]))
# # print(max(map(lambda x : len(x.split()))))
#
# nums = [1,2,3,1,1,3]
# print(sum(map(lambda i: nums[i:].count(i+1), enumerate(nums))))
import bcrypt
# password = "1234"
# bytes = password.encode("utf-8")
# salt = bcrypt.gensalt()
# hash = bcrypt.hashpw(bytes, salt)

# import smtplib
# import time
# from email.message import EmailMessage
# arr = ['saidakbaruraimov7@gmail.com',
# 'mohirmirahmadov@gmail.com',
# 'zoirbekergashev4567@gmail.com',
# 'khayrullo.devs@gmail.com',
# 'imonqulovf1234@gmail.com',
# 'samidilloravshanov13@gmail.com',
# 'shahrizodaxakimova12@gmail.com',
# '9140380@gmail.com',
# 'shohjahonobruyev3@gmail.com',
# 'diyorbekdilmurodov1@gmail.com',
# 'suratovdoniyor@gmail.com',
# 'dilshodbekakhmatov@gmail.com',
# 'nurillayevezozbek@gmail.com',
# 'saidakbaruraimov7@gmail.com',
# 'mohirmirahmadov@gmail.com',
# 'zoirbekergashev4567@gmail.com',
#  'azamovshahboz06082001@gmail.com']
# # ybxfgtkoxfumwxgr
# for i in arr:
#     email_address = "saidakbaruraimov7@gmail.com"
#     email_password = "ybxfgtkoxfumwxgr"
#
#     # create email
#     msg = EmailMessage()
#     msg['Subject'] = "Email subject"
#     msg['From'] = email_address
#     msg['To'] = i
#     msg.set_content("Assalomu Aleykum ")
#
#
#     start = time.time()
#     with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#         smtp.login(email_address, email_password)
#         smtp.send_message(msg)

import httpx
#
# response = httpx.get("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS5SSWo21eTwP74oojyRhJi9Q4BOgZzyG012w&usqp=CAU")
# d = response.content
# with open("img.png", "wb") as f:
#     f.write(d)


