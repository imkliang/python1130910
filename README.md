炘建立的python 檔案

練及test.py
Python 好用的 F 字串！
my_money = 1000000

print(f"{my_money:,}")     # 印出 1,000,000
print(f"{my_money:.2f}")   # 印出 1000000.00
print(f"{my_money:,.2f}")  # 印出 1,000,000.00

pi = 3.1415926

print(f"|{pi:5}|")   # 印出 |3.1415926|
print(f"|{pi:20}|")  # 印出 |            3.1415926|

pi = 3.1415926

print(f"|{pi:<20}|")  # 靠左對齊
print(f"|{pi:>20}|")  # 靠右對齊
print(f"|{pi:^20}|")  # 置中對齊

|3.1415926           |
|           3.1415926|
|     3.1415926      |

print(f"1. {'為你自己學 Python':<20} {'NTD 120'}")
print(f"2. {'為你自己學 Git':<20} {'NTD 200'}")
print(f"3. {'為你自己學 Ruby':<20} {'NTD 180'}")
print(f"4. {'為你自己學 Rust':<20} {'NTD 250'}")

1. 為你自己學 Python         NTD 120
2. 為你自己學 Git            NTD 200
3. 為你自己學 Ruby           NTD 180
4. 為你自己學 Rust           NTD 250
