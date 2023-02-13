class Solution:
    def reformatDate(self, d: str) -> str:
        parts = d.split() 
        months = {'Jan': '01', 'Feb': '02', 
                  'Mar': '03', 'Apr': '04', 
                  'May': '05', 'Jun': '06', 
                  'Jul': '07', 'Aug': '08', 
                  'Sep': '09', 'Oct': '10', 
                  'Nov': '11', 'Dec': '12'}
        
        day = parts[0][:-2]
        month = months[parts[1]]
        year = parts[2]

        if int(day) < 10: 
            day = '0' + day
        
        return '-'.join([year, month, day]) 
