class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        sentence1 = sentence1.split(" ")
        sentence2 = sentence2.split(" ")

        if len(sentence1) > len(sentence2):
            sentence1, sentence2 = sentence2, sentence1
        
        l1,r1 = 0, len(sentence1)-1
        l2,r2 = 0, len(sentence2) -1
        while l1 <=r1 and sentence1[l1] == sentence2[l2]:
            l1+=1
            l2+=1
        while l2<=r2 and sentence1[r1] == sentence2[r2]:
            r1-=1
            r2-=1
        return r1 < l1
