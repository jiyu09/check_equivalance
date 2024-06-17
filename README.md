# check_equivalance.py
이 모듈은 관계 R이 동치 관계인지 확인하는 모듈입니다.

## cheak_reflexive(R, A)
관계 R이 반사 관계인지 확인하는 함수입니다.
```
def cheak_reflexive(R, A) :
    reflex = set([(x, x) for x in list(A)])
    return reflex.issubset(R)
```
이 함수에서는 전체 집합인 A를 입력받아 반사 관계 집합을 생성하고 그 관계가 R의 부분집합이면 True를 반환, 아니면 False 반환합니다.

## cheak_symmetric(R)
관계 R이 대칭 관계인지 확인하는 함수입니다.
```
def cheak_symmetric(R) :
    symmetric = set([(y, x) for (x, y) in list(R)])
    return symmetric.issubset(R)
```
이 함수에서는 R을 입력받아 각 요소에 대한 대칭 관계 집합을 생성하고 그 관계가 R의 부분집합이면 True를 반환, 아니면 False 반환합니다.

## cheak_transitive(R)
관계 R이 전이 관계인지 확인하는 함수입니다.
```
def cheak_transitive(R) :
    R_list = list(R)
    transitive_list = []
    for (a, b) in R_list :
        for (c, d) in R_list :
            if b == c :
                transitive_list.append((a, d))
    transitive = set(transitive_list)
    return transitive.issubset(R)
```
이 함수에서는 R을 입력받아 각 요소에 대한 전이 관계 집합을 생성하고 그 관계가 R의 부분집합이면 True를 반환, 아니면 False 반환합니다.

## check_equivalance(R, A)
관계 R이 동치 관계인지 확인하는 함수입니다.
```
def check_equivalance(R, A) :
    return cheak_reflexive(R, A) and cheak_symmetric(R) and cheak_transitive(R)
```
이 함수에서는 앞서 만든 세 함수를 호출하여 반사, 대칭, 전이 관계가 모두 만족하면 True를 반환, 아니면 False 반환합니다.
