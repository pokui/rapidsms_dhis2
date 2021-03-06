from django.db import models


def promote(modeladmin, request, queryset):
    queryset.update(created=True)

promote.short_description = "Update facility Code"
# Create your models here.
class CodeStatus(models.Model):
    id = models.IntegerField(primary_key=True)
    facility = models.TextField()
    ftype = models.CharField(max_length=32)
    code = models.CharField(max_length=32)
    created = models.BooleanField()
    has_dups = models.BooleanField()
    fuzzy_matched = models.TextField()
    dups = models.TextField()
    pmatch = models.DecimalField(max_digits=5, decimal_places=3)
    fid = models.IntegerField()
    cdate = models.DateTimeField()
    class Meta:
        db_table = u'code_status'

    def __unicode__(self):
        if self.created:
            r = "(*)"
        else: r = ""
        return "%s %s ===> %s %s ===>%s"%(self.facility, self.ftype, self.fuzzy_matched, self.ftype, r)

class Dhis2Mapping(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    field_slug = models.TextField()
    keyword = models.TextField()
    dhis2_uid = models.TextField()
    dhis2_type = models.TextField()
    dhis2_dataelement = models.TextField()
    cdate = models.DateTimeField()

    def __unicode__(self):
        return self.name
    class Meta:
        db_table = u'dhis2_mapping'

