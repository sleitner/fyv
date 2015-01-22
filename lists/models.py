from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from lists.queryvoter import query

class List(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    shared_with = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='shared_lists'
    )

    def get_absolute_url(self):
        return reverse('view_list', args=[self.id])


    @property
    def name(self):
        return self.item_set.first().lastname


    @staticmethod
    def create_new(first_item_firstname, first_item_lastname, owner=None):
        list_ = List.objects.create(owner=owner)
        Person.objects.create(firstname=first_item_firstname, lastname=first_item_lastname, list=list_)
        rows = query(first_item_firstname, first_item_lastname)
        # column names: head -1  SWVF_1_44.TXT| perl -pe 's/,/\n/g' |grep GENERAL |perl -pe 's/-//g'|perl -pe 's/\///g'
        for row in rows:
            # these could be extracted from the dictionary version with a **
            Voter.objects.create(firstname=first_item_firstname, lastname=first_item_lastname,
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
        return list_

class Voter(models.Model):
    firstname = models.CharField(default='', max_length=100)
    lastname = models.CharField(default='', max_length=100)
    byr = models.IntegerField(default='0')
    GENERAL11072000=models.CharField(default='', max_length=10)
    GENERAL11062001=models.CharField(default='', max_length=10)
    GENERAL11052002=models.CharField(default='', max_length=10)
    GENERAL11042003=models.CharField(default='', max_length=10)
    GENERAL11022004=models.CharField(default='', max_length=10)
    GENERAL11082005=models.CharField(default='', max_length=10)
    GENERAL11072006=models.CharField(default='', max_length=10)
    GENERAL11062007=models.CharField(default='', max_length=10)
    GENERAL12112007=models.CharField(default='', max_length=10)
    GENERAL11042008=models.CharField(default='', max_length=10)
    GENERAL11182008=models.CharField(default='', max_length=10)
    GENERAL11032009=models.CharField(default='', max_length=10)
    GENERAL11022010=models.CharField(default='', max_length=10)
    GENERAL11082011=models.CharField(default='', max_length=10)
    GENERAL11062012=models.CharField(default='', max_length=10)
    GENERAL11052013=models.CharField(default='', max_length=10)
    list = models.ForeignKey(List, default=None)
#    person = models.ForeignKey(Person, default=None)

class Person(models.Model):
    firstname = models.CharField(default='', max_length=100)
    lastname = models.CharField(default='', max_length=100)
    list = models.ForeignKey(List, default=None)

    class Meta:
        ordering = ('id',)
       # unique_together = ('list', 'firstname')


    def __str__(self):
        return self.lastname

