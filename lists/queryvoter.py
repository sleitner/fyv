from django.db import connections

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


def query_display(c, firstname, lastname, state='ohio'):
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
        zipcode = 14174
        c.execute('''
        SELECT lastname, firstname, middlename, city, zip, DOB, gender, lastvote, regdate, G2014, G2012, G2010 
        FROM voter_history.newyork 
        WHERE FIRST_NAME=%s AND LAST_NAME=%s AND ZIP=%s LIMIT 1000;
        ''', [firstname, lastname, zipcode]) 
        rows = (c.fetchall(),[-1])
    else:
        return None
        
def query(firstname, lastname):
# todo: to prevent injection attacks, paramters go into execute with quotes around them
# for strings that are NOT externally accessible inputs you should devise a template that 
# gives more flexibility in handling parameters like state or the list of columns
    c = connections['votersdb'].cursor()
    (rows,id) = query_display(c, firstname, lastname)
    #    p = query_prediction(c, firstname, lastname)
    return rows
