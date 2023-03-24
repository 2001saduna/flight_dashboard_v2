from datetime import datetime
import parser_1


def calculate_time():
   result = parser_1.readTextFile('junelogs.txt')
   first_line = result[0]
   first_time = datetime.strptime(first_line['time'], '%H:%S:%M')
   last_line = result[-1]
   last_time = datetime.strptime(last_line['time'], '%H:%S:%M')
   delta = last_time - first_time
   total_seconds = delta.total_seconds()
   hours = str(int(total_seconds // 3600)).zfill(2)
   minutes = str(int((total_seconds % 3600) // 60)).zfill(2)
   seconds = str(int(total_seconds % 60)).zfill(2)
   return f"{hours}:{minutes}:{seconds}"
   

