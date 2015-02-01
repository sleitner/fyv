from django.db import connections
import numpy as np

#todo: this could be a class of staticmethods?
def dictfetchall(c):
    "Returns all rows from a cursor as a dict"
    desc = c.description
    return [dict(zip([col[0] for col in desc], row))
            for row in c.fetchall()]

def search_replace(rows, search='', replace=" :/ "):
    if not search:
        return [[ el if el else replace for el in row] for row in rows]
    else :
        return [[ el if el!=search else replace for el in row] for row in rows]


def sigmoid(alpha):
    return 1/(1. + np.exp(-alpha))

def model(c, rows, state='newyork', mtype='logistic'):
    table_name =state+"_"+mtype
    c.execute("SELECT * FROM voter_history.newyork_logistic")
    result = c.fetchall()
    thetas = result[0]
    thetas = [theta for theta in thetas]  #unpack
    bias = thetas.pop()
    fe_i = result[1]
    fe_i = [int(i) for i in fe_i]  #unpack
    fe_i.pop()
    
    prob = np.zeros(len(rows))
    for i, row in enumerate(rows): 
        alpha = np.sum( (np.asarray(row)[fe_i]).astype(float) * np.asarray(thetas)) + bias 
        prob[i] = sigmoid(alpha)
    return prob*100


def query_cols(c):
    c.execute("show fields from voter_history.newyork")
    cols = c.fetchall()
    cols = [c[0] for c in cols]  #unpack field title:
    return cols

def query_display(c, firstname, lastname, zipcode, state='newyork'):
    if state == 'ohio':
        c.execute('''
        SELECT YEAR_OF_BIRTH, 
        `GENERAL-11/07/2000`, `GENERAL-11/06/2001`, `GENERAL-11/05/2002`, `GENERAL-11/04/2003`, `GENERAL-11/02/2004`, `GENERAL-11/08/2005`, `GENERAL-11/07/2006`, `GENERAL-11/06/2007`, `GENERAL-12/11/2007`, `GENERAL-11/04/2008`, `GENERAL-11/18/2008`, `GENERAL-11/03/2009`, `GENERAL-11/02/2010`, `GENERAL-11/08/2011`, `GENERAL-11/06/2012`, `GENERAL-11/05/2013` 
        FROM voter_history.ohio 
        WHERE FIRST_NAME=%s AND LAST_NAME=%s LIMIT 1000;
        ''', [firstname, lastname]) 
        rows = c.fetchall()
        rows = search_replace(rows, replace='-') #empty
        rows = search_replace(rows, search='X', replace='voted!')
        return (rows,[-1])

    elif( state == "newyork"):
        
        cols = query_cols(c)
        if zipcode:
            c.execute(''' SELECT * 
                  FROM voter_history.newyork 
                  WHERE firstname=%s AND lastname=%s AND zip=%s LIMIT 1000;
                  ''', [firstname, lastname, zipcode]) 
        else:
            c.execute(''' SELECT * 
                  FROM voter_history.newyork 
                  WHERE firstname=%s AND lastname=%s LIMIT 1000;
                  ''', [firstname, lastname]) 
        rows = c.fetchall()
        rows = [i for i in np.asarray(rows)]  #unpack 
        p = model(c, rows)
        return (cols, rows, p)

    else:
        return None
        
def query(firstname, lastname, zipcode):
# todo: to prevent injection attacks, paramaters ('firstname') go into execute with 
# implicit quotes around them; for strings that are NOT externally accessible 
# inputs you should devise a template that 
# gives more flexibility in handling parameters like state or the list of columns
    c = connections['votersdb'].cursor()
    (cols,rows,p) = query_display(c, firstname, lastname, zipcode)
    return (cols,rows,p) 
