class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # 기본적으로 글자가 숫자보다 우선순위기 때문에 글자와 숫자를 분류한 뒤 서로 합친다.
        letters, digits = [], []
        for log in logs:
            # 각 log는 글자/숫자 종류와 데이터가 띄어쓰기로 구분되어 있기 때문에
            # split으로 쪼갠 뒤 데이터 종류를 건너뛰고 배열의 1번째 요소가 숫자인지 판단한다.
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        # 정렬을 하는 것은 문자 파트이기 때문에 sort의 key를 이용해 각 log.split()의 0번째 요소인 데이터의 종류를 제외하고 정렬한다.
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits
