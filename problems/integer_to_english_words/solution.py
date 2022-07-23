class Solution:
    def numberToWords(self, num: int) -> str:
        #take  a bow
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
           'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        thousand = 'Thousand Million Billion'.split()
        def word(num, idx=0):
            if num == 0:
                return []#if it's 0, i.e 50, 905, anything Zero is not needed
            if num < 20:
                return [to19[num-1]]#0 indexed, hence num-1
            if num < 100:
                return [tens[(num//10)-2]] + word(num%10)#97, 97//10 - 2 = 7, tens[7] = Ninety, we are always concatenating lists +. word(reminder = num % 10)
            if num < 1000:#say 897, 897//100 = 8, find 8-1 in to19 + Hundred, word(reminder)
                return [to19[num//100-1]] + ['Hundred'] + word(num%100)

            p, r = num//1000, num%1000 #quotient and reminder like above
            space = [thousand[idx]] if p % 1000 !=0 else []#to construct big numbers #just remember the logic
            #say 3050000, first iteration word(3050) + Thousand + word(0)
            #p = 3, q=50 - word(3) + thousand[1] + word(50)
            #3 Million fifty thousand
            return  word(p, idx+1) + space + word(r)
        return ' '.join(word(num)) or 'Zero'