class Solution:
    def reformatDate(self, date: str) -> str:
        months = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}
        date_list = date.split(" ")
        res = []
        for val in reversed(date_list):
            if val.isdigit():
                res.append(val)
            elif val in months:
                res.append(months[val])
            else:
                if len(val) > 3:
                    res.append(val[:2])
                else:
                    res.append("0" + val[:1])
        return "-".join(res)
        