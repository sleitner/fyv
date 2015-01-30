from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from lists.queryvoter import query
from lists.queryvoter import query_cols

class List(models.Model):
    def get_absolute_url(self):
        return reverse('view_list', args=[self.id])

    @staticmethod
    def create_new_twittNY(item_firstname, item_lastname, item_zipcode='', list_=''):
        if not list_:
            list_ = List.objects.create()
            Person.objects.create(firstname=item_firstname, lastname=item_lastname, list=list_)
        # find_nearby_zips(item_zipcode)
        (cols,rows,p) = query(item_firstname, item_lastname, item_zipcode)
        print(rows)
        for i,row in enumerate(rows):
            d = dict(zip(cols,row))
            # these could be extracted from the dictionary version with a **
            print(i)
            Voter.objects.create(
                    lastname = d['lastname'],
                    firstname = d['firstname'],
                    middlename = d['middlename'],
                    suffix = d['suffix'],
                    city = d['city'],
                    zip = d['zip'],
                    zip4 = d['zip4'],
                    DOB = d['DOB'],
                    gender = d['gender'],
                    party = d['party'],
                    countycode = d['countycode'],
                    legdistrict = d['legdistrict'],
                    towncity = d['towncity'],
                    ward = d['ward'],
                    congressdistrict = d['congressdistrict'],
                    lastvote = d['lastvote'],
                    regdate = d['regdate'],
                    P1993 = d['P1993'],
                    P1994 = d['P1994'],
                    P1995 = d['P1995'],
                    P1996 = d['P1996'],
                    P1997 = d['P1997'],
                    P1998 = d['P1998'],
                    P1999 = d['P1999'],
                    P2000 = d['P2000'],
                    P2001 = d['P2001'],
                    P2002 = d['P2002'],
                    P2003 = d['P2003'],
                    P2004 = d['P2004'],
                    P2005 = d['P2005'],
                    P2006 = d['P2006'],
                    P2007 = d['P2007'],
                    P2008 = d['P2008'],
                    P2009 = d['P2009'],
                    P2010 = d['P2010'],
                    P2011 = d['P2011'],
                    P2012 = d['P2012'],
                    P2013 = d['P2013'],
                    P2014 = d['P2014'],
                    G1992 = d['G1992'],
                    G1993 = d['G1993'],
                    G1994 = d['G1994'],
                    G1995 = d['G1995'],
                    G1996 = d['G1996'],
                    G1997 = d['G1997'],
                    G1998 = d['G1998'],
                    G1999 = d['G1999'],
                    G2000 = d['G2000'],
                    G2001 = d['G2001'],
                    G2002 = d['G2002'],
                    G2003 = d['G2003'],
                    G2004 = d['G2004'],
                    G2005 = d['G2005'],
                    G2006 = d['G2006'],
                    G2007 = d['G2007'],
                    G2008 = d['G2008'],
                    G2009 = d['G2009'],
                    G2010 = d['G2010'],
                    G2011 = d['G2011'],
                    G2012 = d['G2012'],
                    G2013 = d['G2013'],
                    G2014 = d['G2014'],
                    nyid = d['nyid'],
                    prob=p[i],
                    list=list_)
        return list_

    @staticmethod
    def create_new(item_firstname, item_lastname, item_zipcode=''):
        list_ = List.objects.create()
        Person.objects.create(firstname=item_firstname, lastname=item_lastname, list=list_)
        # find_nearby_zips(item_zipcode)
        (cols,rows,p) = query(item_firstname, item_lastname, item_zipcode)
        
        state = 'newyork'
        if state == 'ohio':
            # column names: head -1  SWVF_1_44.TXT| perl -pe 's/,/\n/g' |grep GENERAL |perl -pe 's/-//g'|perl -pe 's/\///g'
            for row in rows:
                # these could be extracted from the dictionary version with a **
                Voter.objects.create(firstname=item_firstname, lastname=item_lastname,
                                 byr = row[0],
                                 GENERAL11072000=row[1],
                                 GENERAL11062001=row[2],
                                 GENERAL11052002=row[3],
                                 GENERAL11042003=row[4],
                                 GENERAL11022004=row[5],
                                 GENERAL11082005=row[6],
                                 GENERAL11072006=row[7],
                                 GENERAL11062007=row[8],
                                 GENERAL12112007=row[9],
                                 GENERAL11042008=row[10],
                                 GENERAL11182008=row[11],
                                 GENERAL11032009=row[12],
                                 GENERAL11022010=row[13],
                                 GENERAL11082011=row[14],
                                 GENERAL11062012=row[15],
                                 GENERAL11052013=row[16],
                                 list=list_)
        elif state == 'newyork':
            for i,row in enumerate(rows):
                d = dict(zip(cols,row))
                print(d)
                # these could be extracted from the dictionary version with a **
                Voter.objects.create(
                    lastname = d['lastname'],
                    firstname = d['firstname'],
                    middlename = d['middlename'],
                    suffix = d['suffix'],
                    city = d['city'],
                    zip = d['zip'],
                    zip4 = d['zip4'],
                    DOB = d['DOB'],
                    gender = d['gender'],
                    party = d['party'],
                    countycode = d['countycode'],
                    legdistrict = d['legdistrict'],
                    towncity = d['towncity'],
                    ward = d['ward'],
                    congressdistrict = d['congressdistrict'],
                    lastvote = d['lastvote'],
                    regdate = d['regdate'],
                    P1993 = d['P1993'],
                    P1994 = d['P1994'],
                    P1995 = d['P1995'],
                    P1996 = d['P1996'],
                    P1997 = d['P1997'],
                    P1998 = d['P1998'],
                    P1999 = d['P1999'],
                    P2000 = d['P2000'],
                    P2001 = d['P2001'],
                    P2002 = d['P2002'],
                    P2003 = d['P2003'],
                    P2004 = d['P2004'],
                    P2005 = d['P2005'],
                    P2006 = d['P2006'],
                    P2007 = d['P2007'],
                    P2008 = d['P2008'],
                    P2009 = d['P2009'],
                    P2010 = d['P2010'],
                    P2011 = d['P2011'],
                    P2012 = d['P2012'],
                    P2013 = d['P2013'],
                    P2014 = d['P2014'],
                    G1992 = d['G1992'],
                    G1993 = d['G1993'],
                    G1994 = d['G1994'],
                    G1995 = d['G1995'],
                    G1996 = d['G1996'],
                    G1997 = d['G1997'],
                    G1998 = d['G1998'],
                    G1999 = d['G1999'],
                    G2000 = d['G2000'],
                    G2001 = d['G2001'],
                    G2002 = d['G2002'],
                    G2003 = d['G2003'],
                    G2004 = d['G2004'],
                    G2005 = d['G2005'],
                    G2006 = d['G2006'],
                    G2007 = d['G2007'],
                    G2008 = d['G2008'],
                    G2009 = d['G2009'],
                    G2010 = d['G2010'],
                    G2011 = d['G2011'],
                    G2012 = d['G2012'],
                    G2013 = d['G2013'],
                    G2014 = d['G2014'],
                    nyid = d['nyid'],
                    prob=p[i],
                    list=list_)
            
        return list_

##########################################################
class Person(models.Model):
    firstname = models.CharField(default='', max_length=100)
    lastname = models.CharField(default='', max_length=100)
    zipcode = models.IntegerField(default=None, null=True)
    list = models.ForeignKey(List, default=None)

    class Meta:
        ordering = ('id',)
       # unique_together = ('list', 'firstname')

    def __str__(self):
        return self.lastname

class Voter(models.Model):
    lastname = models.CharField(default='', max_length=100, null=True)
    firstname = models.CharField(default='', max_length=100, null=True)
    middlename = models.CharField(default='', max_length=100, null=True)
    suffix = models.CharField(default='', max_length=3, null=True)
    city = models.CharField(default='', max_length=100, null=True)
    zip = models.IntegerField(default='0', null=True)
    zip4 = models.IntegerField(default='0', null=True)
    DOB = models.IntegerField(default='0', null=True)
    gender = models.CharField(default='', max_length=3)
    party = models.CharField(default='', max_length=100)
    countycode = models.IntegerField(default='0', null=True)
    legdistrict = models.IntegerField(default='0', null=True)
    towncity = models.CharField(default='', max_length=100, null=True)
    ward = models.IntegerField(default='0', null=True)
    congressdistrict = models.IntegerField(default='0', null=True)
    lastvote = models.IntegerField(default='0', null=True)
    regdate = models.IntegerField(default='0', null=True)
    P1993 = models.IntegerField(default='0')
    P1994 = models.IntegerField(default='0')
    P1995 = models.IntegerField(default='0')
    P1996 = models.IntegerField(default='0')
    P1997 = models.IntegerField(default='0')
    P1998 = models.IntegerField(default='0')
    P1999 = models.IntegerField(default='0')
    P2000 = models.IntegerField(default='0')
    P2001 = models.IntegerField(default='0')
    P2002 = models.IntegerField(default='0')
    P2003 = models.IntegerField(default='0')
    P2004 = models.IntegerField(default='0')
    P2005 = models.IntegerField(default='0')
    P2006 = models.IntegerField(default='0')
    P2007 = models.IntegerField(default='0')
    P2008 = models.IntegerField(default='0')
    P2009 = models.IntegerField(default='0')
    P2010 = models.IntegerField(default='0')
    P2011 = models.IntegerField(default='0')
    P2012 = models.IntegerField(default='0')
    P2013 = models.IntegerField(default='0')
    P2014 = models.IntegerField(default='0')
    G1992 = models.IntegerField(default='0')
    G1993 = models.IntegerField(default='0')
    G1994 = models.IntegerField(default='0')
    G1995 = models.IntegerField(default='0')
    G1996 = models.IntegerField(default='0')
    G1997 = models.IntegerField(default='0')
    G1998 = models.IntegerField(default='0')
    G1999 = models.IntegerField(default='0')
    G2000 = models.IntegerField(default='0')
    G2001 = models.IntegerField(default='0')
    G2002 = models.IntegerField(default='0')
    G2003 = models.IntegerField(default='0')
    G2004 = models.IntegerField(default='0')
    G2005 = models.IntegerField(default='0')
    G2006 = models.IntegerField(default='0')
    G2007 = models.IntegerField(default='0')
    G2008 = models.IntegerField(default='0')
    G2009 = models.IntegerField(default='0')
    G2010 = models.IntegerField(default='0')
    G2011 = models.IntegerField(default='0')
    G2012 = models.IntegerField(default='0')
    G2013 = models.IntegerField(default='0')
    G2014 = models.IntegerField(default='0')
    nyid = models.IntegerField(default='0')
    prob = models.FloatField(default='-1.0')
    # ohio
#    firstname = models.CharField(default='', max_length=100)
#    lastname = models.CharField(default='', max_length=100)
#    byr = models.IntegerField(default='0')
#    GENERAL11072000=models.CharField(default='', max_length=10)
#    GENERAL11062001=models.CharField(default='', max_length=10)
#    GENERAL11052002=models.CharField(default='', max_length=10)
#    GENERAL11042003=models.CharField(default='', max_length=10)
#    GENERAL11022004=models.CharField(default='', max_length=10)
#    GENERAL11082005=models.CharField(default='', max_length=10)
#    GENERAL11072006=models.CharField(default='', max_length=10)
#    GENERAL11062007=models.CharField(default='', max_length=10)
#    GENERAL12112007=models.CharField(default='', max_length=10)
#    GENERAL11042008=models.CharField(default='', max_length=10)
#    GENERAL11182008=models.CharField(default='', max_length=10)
#    GENERAL11032009=models.CharField(default='', max_length=10)
#    GENERAL11022010=models.CharField(default='', max_length=10)
#    GENERAL11082011=models.CharField(default='', max_length=10)
#    GENERAL11062012=models.CharField(default='', max_length=10)
#    GENERAL11052013=models.CharField(default='', max_length=10)
    list = models.ForeignKey(List, default=None)
#    person = models.ForeignKey(Person, default=None)

