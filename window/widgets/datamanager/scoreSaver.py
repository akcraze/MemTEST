import  sqlite3
def data_push(self,score):

            try:
                  connection = sqlite3.connect("score.db")
                  cursr = connection.cursor()
                  cursr.execute("create table if not exists SCORE(score int(20));") 
                  cursr.execute(f"INSERT INTO SCORE VALUES (\"{score}\") ;")
                  connection.commit()
                  
            except Exception as error:
                  raise error
