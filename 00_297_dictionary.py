data = { "query" : "진연"}    #dictionary는 { } 로 표시 {key : value} 

print("data :", data)                           # data : {'query': '진연'}
print("data.keys():", data.keys())
print("data.values():", data.values())
print("type(data) :", type(data))               # type(data) : <class 'dict'>

print("data['query'] :", data['query'])         # data['query'] : 진연

print("data.get('query') :", data.get('query')) # data.get('query') : 진연

print("============")

mydata = {"이름" : "김진연", "직업" : "기술교사", "별자리" : "물고기자리"}  
print("mydata :", mydata)                           # mydata : {'이름': '김진연', '직업': '기술교사', '별자리': '물고기자리'}
print("mydata['이름'] :", mydata['이름'])            # mydata['이름'] : 김진연
print("mydata.get('이름') :", mydata.get('이름'))    # mydata.get('이름') : 김진연

print("============")

myfamily = {"아빠" : {"이름" : "김진연", "직업" : "기술교사", "별자리" : "물고기자리"},
            "엄마" : {"이름" : "양정화", "직업" : "유치원교사", "별자리" : "양자리"},  
            "큰아들" : {"이름" : "김민수", "직업" : "초등학생", "별자리" : "사자자리"},  
            "작은아들" : {"이름" : "김민수", "직업" : "어린이집원생", "별자리" : "황소자리"}  }

print("myfamily :", myfamily)                                                # myfamily : {'아빠': {'이름': '김진연', '직업': '기술교사', '별자리': '물고기자리'}, 
                                                                             #               '엄마': {'이름': '양정화', '직업': '유치원교사', '별자리': '양자리'}, 
                                                                             #               '큰아들': {'이름': '김민수', '직업': '초등학생', '별자리': '사자자리'}, 
                                                                             #               '작은아들': {'이름': '김민수', '직업': '어린이집원생', '별자리': '황소자리'}}
print("mydata['아빠'] :", myfamily['아빠'])                                   # mydata['아빠'] : {'이름': '김진연', '직업': '기술교사', '별자리': '물고기자리'}
print("mydata['아빠']['직업'] :", myfamily['아빠']['직업'])                    # mydata['아빠']['직업'] : 기술교사
print("mydata.get('아빠').get('직업') :", myfamily.get('아빠').get('직업'))    # mydata.get('아빠').get('직업') : 기술교사