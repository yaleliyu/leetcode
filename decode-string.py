class Solution:
    def findInnerString(self, s:str):
        if s[0] != '[':
            return s

        if len(s) <= 2:
            return ''

        list_buf = ['[']
        start = 1
        end = -1

        for idx, c in enumerate(s[1:]):
            if c == ']':
                if len(list_buf) == 1:
                    end = idx+1
                    break

                list_buf = list_buf[:-1]
            elif c == '[':
                list_buf.append('[')

        return s[start:end] if end > start else ''




    def decodeString(self, s: str) -> str:
        if len(s) == 0:
            return ''

        num_start = -1
        dup = 1
        result_str = ''
        for idx, c in enumerate(s):
            if c.isdigit():
                if num_start == -1:
                    num_start = idx
            else:
                if num_start != -1:
                    dup = int(s[num_start:idx])
                    num_start = -1

                if c == '[':
                    inner_str = self.findInnerString(s[idx:])
                    flat_str = self.decodeString(inner_str)*dup
                    result_str += flat_str
                    return result_str + self.decodeString(s[idx+len(inner_str)+2:])

                result_str += c

        return result_str

sln = Solution()
print(sln.decodeString('abc'))
print(sln.decodeString('[a]2[bc]'))
print(sln.decodeString('3[a2[c]]'))
print(sln.decodeString('2[abc]3[cd]ef'))
