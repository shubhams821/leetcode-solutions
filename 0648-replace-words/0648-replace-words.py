class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        lst = []
        dic=[]
        sen_lst = sentence.split()
        print(sen_lst)
        for i in dictionary:
            dic.append([i,len(i)])
        dic.sort(key=lambda dic: dic[1])
        for word in sen_lst:
            for i in range(len(word)+1):
                prefix = word[:i]
                if prefix in dictionary:
                    lst.append(prefix)
                    break
            else:
                lst.append(word)
        print(' '.join(lst))
        sen = ' '.join(lst)
        return sen