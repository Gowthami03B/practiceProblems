from datetime import date
import copy
# (old_ticker: str, new_ticker: str, effective_date: str, company_id: int)
# sample_ticker_changes = [
#     ("FB", "META", "2022-06-09", 12345),
#     ("GOOG", "GOOGL", "2020-09-10", 54321),
#     ("META","XXXX","2032-06-09", 12345),
# ]

# get_pit_ticker(12345, date.today()) -> "META"
# get_pit_ticker(12345, date(2022, 1, 1)) -> "FB"
#map(id) - (FB,META,NEW_DATE), (META,XXXX,NEW_DATE)
from collections import OrderedDict
class PointInTimeTicker:
    def __init__(self, ticker_changes: list):
        ticker_changes.sort(key=lambda x:x[2])
        print(ticker_changes)
        self.ticker_changes_map = OrderedDict()
        for ticker in ticker_changes:
            old_ticker, new_ticker, effective_date, company_id = ticker
            if company_id in self.ticker_changes_map:
                self.ticker_changes_map[company_id].append((old_ticker,new_ticker,effective_date))
            else:
                self.ticker_changes_map[company_id] = []
                self.ticker_changes_map[company_id].append((old_ticker,new_ticker,effective_date))
        print(self.ticker_changes_map)

    """
    ("B", "C", "2022-02-01", 123)
    ("A", "B", "2022-01-01", 123)
    get_pit_ticker(123, "2020-01-01")
    
    sorted
    2023
    "2022-01-03"
    
    """
    def get_pit_ticker(self, company_id: int, as_of: date):#more efficient
        copy_ticker_changes = copy.deepcopy(self.ticker_changes_map)
        if company_id in self.ticker_changes_map:
            ticker_changes = copy_ticker_changes[company_id]
            #filter
            for ticker_change in ticker_changes:
                if len(ticker_changes) > 1:
                    old_ticker, new_ticker, effective_date = ticker_change
                    if as_of < effective_date:
                        ticker_changes.pop()
                
            old_ticker, new_ticker, effective_date = ticker_changes[-1]
            if as_of < effective_date:
                # print(self.ticker_changes_map)
                return old_ticker
            else:
                return new_ticker
        else:
            return self.get_current_ticker(company_id)

    @staticmethod
    def get_current_ticker(company_id: int) -> str:
        """
        Assume this method is implemented for you.
        Ex. PointInTimeTicker.get_current_ticker(12345) => "META"
        """
        return "ABC"

sample_ticker_changes = [
    ["META","TEST","2022-30-12", 12345],
    ["FB", "META", "2022-06-09", 12345],
    ["META","META1","2022-08-09", 12345],
    ["GOOG", "GOOGL", "2020-09-10", 54321] 
]
obj = PointInTimeTicker(sample_ticker_changes)
print(obj.get_pit_ticker(12345, "2020-01-01"))
print(obj.get_pit_ticker(12345, "2022-06-09"))
