print('Please fill the seeds file')

import psycopg2

conn = psycopg2.connect(database="anythink-market",
                        host="postgres-python",
                        user="postgres",
                        password="postgres",
                        port="5432")

# Write to table
def create_user(user_name,email,salt,hashed_password):
   
    query = "insert into public.users (username,email,salt,hashed_password,created_at,updated_at) VALUES (%s,%s,%s,%s,now(),now())"
    data = (
        
        user_name,email,salt,hashed_password
        )
   
    try:
        
        cur = conn.cursor()
        cur.execute(query,data)
        #response = cur.fetchall()
        #print(response)
        print("SUCCESS: Transaction complete")
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error :
        print("Database error: ", error)
        conn.rollback()
        raise

def create_items(slug,title,description,body):
   
    query = "insert into public.items (slug, title, description, body, image, seller_id, created_at, updated_at) VALUES (%s,%s,%s,%s,%s,%s,now(),now())"
    data = (
        
        slug
        ,title
        ,description
        ,body
        ,'https://cdn.shopify.com/s/files/1/0712/4751/products/SMA-25_2000x.jpg?v=1629409085'
        ,1
        )
   
    try:
        
        cur = conn.cursor()
        cur.execute(query,data)
        #response = cur.fetchall()
        #print(response)
        print("SUCCESS: Transaction complete")
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error :
        print("Database error: ", error)
        conn.rollback()
        raise

def create_comment(body):
   
    query = "insert into public.comments (body, seller_id, item_id, created_at, updated_at) VALUES (%s,%s,%s,now(),now())"
    data = (
        
        body
        ,3
        ,28
        )
   
    try:
        
        cur = conn.cursor()
        cur.execute(query,data)
        #response = cur.fetchall()
        #print(response)
        print("SUCCESS: Transaction complete")
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error :
        print("Database error: ", error)
        conn.rollback()
        raise

#write_to_postgres('go')

for x in range(100):
    create_user('hello' + str(x),'hello' + str(x),'a','a')

for x in range(100):
    create_items('item' + str(x),'item' + str(x),'item','item')

for x in range(100):
    create_comment('comment' + str(x))