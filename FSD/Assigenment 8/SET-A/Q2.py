from flask import Flask
import psycopg2
app=Flask(__name__)


def db_connect():
    conn=psycopg2.connect(
        dbname="hospital",
        user="postgres",
        password="Tanuja@1106",
        host="localhost",
        port="5432"

    )
    
    return conn
@app.route('/')
def home():
   try:
        conn=db_connect()
        cur=conn.cursor()

        cur.execute("""
           CREATE TABLE IF NOT EXISTS patient(
           id serial PRIMARY KEY,
           NAME VARCHAR(100),
           age INT,
           disease VARCHAR(100)
           );


        """)
        conn.commit()
        cur.close()
        conn.close()
        return "create table successfully !"
   except  Exception as e:  
       return f"error:{e}" 

@app.route('/insert_records')
def insert_records():  
      try:      
          conn = db_connect()      
          cur = conn.cursor()       
          patients = [          
                ("sejal", 24, "Fever"),
                ("Priya", 31, "Diabetes"),
                ("parag", 45, "Hypertension"),            
                ("amruta", 28, "Asthma"),            
                ("vijay", 52, "Arthritis")        ]        
          cur.executemany("INSERT INTO Patient(name,age,disease) VALUES(%s,%s,%s)",patients)
          conn.commit()        
          cur.close()        
          conn.close()        
          return "5 record inserted sucessfully!"    
      except Exception as e:        
          return f"Error: {e}"
@app.route('/search_patient/<int:pid>')
def search_patient(pid):    
    try:        
        conn = db_connect()        
        cur = conn.cursor()        
        cur.execute("SELECT * FROM Patient WHERE id = %s;",(pid,))        
        patient = cur.fetchone()        
        cur.close()        
        conn.close()        
        if patient:            
            return f"Patient Details : ID={patient[0]}, Name={patient[1]}, Age={patient[2]}, Disease={patient[3]}"        
        else:            
            return "No patient associated with that ID"    
    except Exception as e:        
        return f"Error : {e}"
    

if __name__=='__main__':
    app.run(debug=True)