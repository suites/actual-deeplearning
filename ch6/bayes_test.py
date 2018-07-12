from bayes import BayesianFilter
bf = BayesianFilter()

bf.fit('파격 세일 - 오늘까지만 30% 할인', '광고')
bf.fit('쿠폰 선물 & 무료 배송', '광고')
bf.fit('현데계 백화점 세일', '광고')
bf.fit('봄과 함께 찾아온 따뜻한 신제품 소식', '광고')
bf.fit('인기 제품 기간 한정 세일', '광고')
bf.fit('오늘 일정 확인', '중요')
bf.fit('프로젝트 진행 상황 보고', '중요')
bf.fit('계약 잘 부탁드립니다', '중요')
bf.fit('회의 일정이 등록되었습니다.', '중요')
bf.fit('오늘 일정이 없습니다.', '중요')

pre, scorelist = bf.predict('안녕하세요? 할인일정 입니다')
print('결과 =', pre)
print(scorelist)
