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

def query(firstname, lastname, state='ohio'):
# todo: to prevent injection attacks, paramters go into execute with quotes around them
# for strings that are NOT externally accessible inputs you should devise a template that 
# gives more flexibility in handling parameters like state or the list of columns
    c = connections['votersdb'].cursor()
    c.execute("\
SELECT YEAR_OF_BIRTH, \
`GENERAL-11/07/2000`, `GENERAL-11/06/2001`, `GENERAL-11/05/2002`, `GENERAL-11/04/2003`, `GENERAL-11/02/2004`, `GENERAL-11/08/2005`, `GENERAL-11/07/2006`, `GENERAL-11/06/2007`, `GENERAL-12/11/2007`, `GENERAL-11/04/2008`, `GENERAL-11/18/2008`, `GENERAL-11/03/2009`, `GENERAL-11/02/2010`, `GENERAL-11/08/2011`, `GENERAL-11/06/2012`, `GENERAL-11/05/2013` \
FROM voter_history.ohio \
WHERE FIRST_NAME=%s AND LAST_NAME=%s LIMIT 1000;", [firstname, lastname]) 
    rows = c.fetchall()
    rows = search_replace(rows, replace='-') #empty
    rows = search_replace(rows, search='X', replace='voted!')
#    print(rows)
    return rows
