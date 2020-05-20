f=open("hitsong.csv",'w',encoding = 'UTF-8')
#csv파일에서 한글이 깨지는 경우 -> 엑셀 파일 사용 혹은 encoding = 'UTF-8-sig'추가
singers = ['박정현','임창정','izi','아이유']
songs = ['꿈에','소주한잔','응급실','좋은날']
for i in range(len(singers)):
    f.write(singers[i]+','+songs[i]+'\n')

f.close()