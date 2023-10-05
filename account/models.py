from django.db import models

class Profile(models.Model):
    full_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='static/profiles/', null=True, blank=True)
    bio = models.TextField(verbose_name='profile bio')
    email = models.EmailField(blank=False)
    telegram_username = models.CharField(max_length=250, null=True, blank=True)
    languages = models.ManyToManyField('Language')
    skills =models.ManyToManyField('Skill')
    region = models.ManyToManyField('Region')
    country = models.ForeignKey('Country', on_delete=models.PROTECT)
    hub = models.ForeignKey('Hub',on_delete=models.PROTECT)
    github_username = models.CharField(max_length=100, null=True, blank=True)
    facebook_username = models.CharField(max_length=100, null=True, blank=True)
    website_link = models.URLField('website link', null=True, blank=True)
    whatsapp_number = models.CharField(max_length=20, null=True, blank=True)
    telephone_number = models.CharField(max_length=20)
    instagram_user = models.CharField(max_length=100, null=True, blank=True)
    linkedin_username = models.CharField(max_length=100, null=True, blank=True)
    twitter_username = models.CharField(max_length=100, null=True, blank=True)
    mastodon = models.CharField(max_length=100, null=True, blank=True) # should it be a URL or Username?
    wikifab = models.CharField(max_length=100, null=True, blank=True)
    other = models.CharField(max_length=100, null=True, blank=True)

    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
    
class Language(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Language"
        verbose_name_plural = "Langauges"
    
class Skill(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"
    
class Country(models.Model):
    # how to map regions to specific countries
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"
    
class Hub(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Hub"
        verbose_name_plural = "Hubs"

class Region(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regions"