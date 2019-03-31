'''
Created on Jul 29, 2015

@author: Sara
'''
import cx_Oracle

def create_connection():
    return cx_Oracle.Connection('T762084/T762084@10.123.79.61/georli06')

def create_cursor(con):
    return cx_Oracle.Cursor(con)