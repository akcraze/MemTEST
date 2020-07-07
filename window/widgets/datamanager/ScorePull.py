import sqlite3

def data_pull(self):
    try:
        connection = sqlite3.connect("score.db")
        cursr = connection.cursor()
        cursr.execute("Select  * from SCORE")
        dataObj = cursr.fetchall()
        scoreList = []
        for i in dataObj:
            for j in i:
                scoreList.append(j)
                
        return scoreList
    
    except Exception as error:
        raise error
