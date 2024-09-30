class Solution:
    def simplifyPath(self, path: str) -> str:
        lst = path.split('/')
        reduntant = ['..']
        print(lst)
        new_lst = []
        for fol in lst:
            if fol in reduntant:
                try:
                    new_lst.pop()
                except:
                    pass
            elif fol != '' and fol != '.':
                new_lst.append(fol)
        new_dir = '/' + "/".join(new_lst)
        print(new_lst)
        return new_dir