a = {"덕성":1, "여자":2, "대학교":3}
a["덕성"] = 100
a["멋사"] =4
del a['대학교']
keys = a.keys()
for k in keys:
    print(k, end='')

#딕셔너리 예시들
    """ 딕셔너리 사용한 예시들
 keys와 values 각가만을 출력함 """
