class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        candles,res = [] ,[]
        for idx,c in enumerate(s):
            if c == "|":
                candles.append(idx)
                
        print(candles)
        
        def find_nearest_candle(startIdx, candles, flag):
            start,end = 0, len(candles)-1
            while(start <= end):
                mid = (start+end)//2
                if candles[mid] == startIdx:
                    return mid
                elif candles[mid] < startIdx :
                    start = mid + 1
                elif candles[mid] > startIdx:
                    end = mid - 1
            return start if flag == 0 else end #return start if flag is 0, i.e if we are trying to find a candle jus larger than the start query, or end if flag == 1 if we are trying to find a candle jus smaller than the end query
                    
        for start, end in queries:
            #nearest candle index to start 
            start_candle_index = find_nearest_candle(start, candles, 0)
            #nearest candle to end
            end_candle_index = find_nearest_candle(end,candles, 1)
            
            if start_candle_index > end_candle_index or start_candle_index >= len(candles) or candles[end_candle_index] > end or candles[start_candle_index] < start:
                res.append(0)#when there are 0 candles
                continue
            #number of candles
            num_candles = end_candle_index-start_candle_index-1 #excluding the indices
            # print("num candles in range",num_candles)
            
            #total items between first and last candle
            items = candles[end_candle_index]-candles[start_candle_index]-1
            
            #Remove the candles from the above interval to get the plates
            num_plates = max(0,items-num_candles)
            res.append(num_plates)
        return res