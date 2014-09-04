import pygal
from pygal.style import CleanStyle
import uuid
import os

def create_pie(stats, directory, fixapplied):
    b = stats
    grandScore = 0
    i = 1
    if fixapplied == "NO":
        for row in b.items():
            score = row[1].count('ON')/float(len(row[1]))
            if i <= 1:
                if score > 0.9:
                    grandScore += 1
            elif 1 < i <= 2:
                if score > 0.8:
                    grandScore += 1
            elif 2 < i <= 3:
                if score > 0.7:
                    grandScore += 1
            elif 4 < i <= 5:
                if score > 0.5:
                    grandScore += 1
            else:
                if score > 0.2:
                    grandScore += 1
            i += 1
    else:
        for row in b.items():
            score = row[1].count('ON')/float(len(row[1]))
            if i <= 1:
                if score < 0.9:
                    grandScore += 1
            elif 1 < i <= 2:
                if score < 0.8:
                    grandScore += 1
            elif 2 < i <= 3:
                if score < 0.7:
                    grandScore += 1
            elif 4 < i <= 5:
                if score < 0.5:
                    grandScore += 1
            else:
                if score < 0.2:
                    grandScore += 1
            i += 1

    if not os.path.exists("./app/static/" + directory):
        os.mkdir("./app/static/" + directory)

    filename = directory + "/" + str(uuid.uuid4()) + ".svg"
    pie_chart = pygal.Pie(style=CleanStyle)
    pie_chart.title = 'Website ability to withstand DoS (in %)'
    pie_chart.add('SAFE', grandScore)
    pie_chart.add('VULNERABLE', len(b)-grandScore)
    pie_chart.render_to_file('./app/static/' + filename)
    return filename