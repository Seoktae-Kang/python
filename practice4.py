# cabinet = {3:"유재석", 100: "김태호", 120: "홍길동"}
# print(cabinet)
# print(cabinet[3])
# print(cabinet[120])

# print(cabinet.get(5))
# print(cabinet.get(5), "사용가능")

# print("hi")

# print(3 in cabinet)
# print(5 in cabinet)


cabinet = {"A-3": "유재석", "B-100": "김태호"}
print(cabinet["A-3"])

# 새손님
print(cabinet)
cabinet["A-3"] ="김종국"
cabinet["C-20"] = "조세호"

print(cabinet)


# 간 손님
del cabinet["A-3"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())


# 목용탕 폐점
cabinet.clear()
print(cabinet)