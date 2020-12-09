#!/usr/bin/env python
# coding: utf-8

# In[20]:


#!/usr/bin/env python
# coding: utf-8

"""
Created on Mon Nov 23 20:36:58 2020
Project : Realistics Data Generation For Interview Management System
Project To Do Load Test
@author: Nilesh Pise

"""

from faker import Faker
from pymysql import connect
from pymysql import cursors
from pymysql.cursors import DictCursor
from datetime import datetime
from datetime import timedelta 
from datetime import date
from random import choice, randint
import pandas as pd
import numpy as np


fake = Faker('en_IN')

host = 'localhost'
user_db = 'root'
password_db = ''
db = 'interview'
rows = input('Enter the no of records you want to insert.')

def phone_number(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


def get_candidates_id():
    
    try:
        connection = connect(host= host, user= user_db, password=password_db, db= db) 
        cursor = connection.cursor(DictCursor)
        sql_get_candidates_id = "SELECT COUNT(`cand_id`) FROM `candidates`"
        cursor.execute(sql_get_candidates_id)
        result = cursor.fetchone()
        connection.commit()
        return result['COUNT(`cand_id`)']
        
    except:
        return 13
    
    
def reports():
    question_id = randint(6, 8)
    cand_id = randint(1, get_candidates_id())
    result = choice(['Osm One', 'Not bad.', 'Quite Interesting', 'This is what i want', 'really good.', 'Interesting.'])
    
    try:
        connection = connect(host= host, user= user_db, password=password_db, db= db)
        cursor = connection.cursor()
        reports_queery = "INSERT INTO `reports`(`question_id`, `cand_id`, `result`) VALUES (%s,%s,%s)"
        cursor.execute(reports_queery,(question_id, cand_id, result))
        connection.commit()
    except: 
        None
    
    
def candidates(user_name, email):
    cand_name = user_name
    cand_email = email
    cand_phone = phone_number(10)
    cand_age = randint(22,40)
    cand_address = fake.address()
    cand_qualification = choice(['M.Tech in Data Science', 'M.Tech in CSE', 'B.Tech in CSE', 'B.Tech in ME', ''])
    

    try:
        connection = connect(host= host, user= user_db, password=password_db, db= db)
        cursor = connection.cursor()
        candidates_queery = "INSERT INTO `candidates`(`cand_name`, `cand_email`, `cand_phone`, `cand_age`, `cand_address`, `cand_qualification`) VALUES (%s,%s,%s,%s,%s,%s)"
        cursor.execute(candidates_queery,(cand_name, cand_email, cand_phone, cand_age, cand_address, cand_qualification))
        connection.commit()
    except: 
        None
        
        
        
        
def comments():
    comment = choice(['Nice Interview.', 'THis was osm Interview','It was quite hard to crack.', 'ops.. not bad.'])
    cand_id = randint(1, get_candidates_id())
    
    try:
        connection = connect(host= host, user= user_db, password=password_db, db= db)
        cursor = connection.cursor()
        comments_queery = "INSERT INTO `comments`(`comment`, `cand_id`) VALUES (%s, %s)"
        cursor.execute(comments_queery,(comment, cand_id))
        connection.commit()
    except: 
        None



def user():
    user_name = fake.first_name() + " " + fake.last_name()
    email = user_name.split()[0] + str(phone_number(5)) + "@gmail.com"
    password = user_name.split()[1] + str(phone_number(6))
    
    try:
        connection = connect(host= host, user= user_db, password=password_db, db= db)
        cursor = connection.cursor()
        user_queery = "INSERT INTO `user`(`user_name`, `email`, `password`) VALUES (%s,%s,%s)"
        cursor.execute(user_queery,(user_name, email, password))
        connection.commit()
    except: 
        None
        
    try:
        candidates(user_name= user_name, email= email)
    except:
        None
        

        
for i in range(0, int(rows)):
    print("{} Records Inserted.".format(i))
    user()
    reports()
    comments()


# In[99]:




