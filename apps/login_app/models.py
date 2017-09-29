# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.contrib import messages
import re
import bcrypt
# Create your models here.

class UserManager(models.Manager):
    def loginVal(self, postData): 
        results = {'status': True, 'errors': [], 'user': None}
        users = self.filter(email = postData['email'])
        if len(users) < 1: #Checks if user is alredy exists
            results['status'] = False
        else:
            if bcrypt.checkpw(postData['password'].encode(), users[0].password.encode()): #Checks if ecrypted passwords match.
                results['user'] = users[0]
            else:
                results['status'] = False
        return results

    def creator(self, postData):
        user = self.create(first_name = postData['first_name'], last_name = postData['last_name'], email = postData['email'], alias = postData['alias'], bday = postData['bday'], password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()))
        return user
#First Name Validations
    def validate(self, postData): #Registration Validation
        results = {'status': True, 'errors': []}
        if len(postData['first_name']) < 3: #Checks how long the First Name is.
            results['errors'].append('Your First Name is Too Short')
            results['status'] = False
        if ' ' in postData['first_name']: #Checks if there are any spaces in the First Name.
            results['errors'].append('There can not be any spaces in your First Name')
            results['status'] = False
        if postData['first_name'].isalpha() != True: #Checks if characters in first name are not letters
            results['errors'].append('Only Letters are allowed for your First Name')
            results['status'] = False
#Alias Validations
        if len(postData['alias']) < 3: #Checks how long the Alias is.
            results['errors'].append('Your Alias is Too Short')
            results['status'] = False
        if ' ' in postData['alias']: #Checks if there are any spaces in the Alias.
            results['errors'].append('There can not be any spaces in your Alias')
            results['status'] = False
        if len(self.filter(alias = postData['alias'])) > 0: #Checks if the email already exists in the database.
            results['errors'].append('Alias already exists')
            results['status'] = False
        if postData['alias'].isalpha() != True: #Checks if characters in Alias are not letters
            results['errors'].append('Only Letters are allowed for alias')
            results['status'] = False
#Last Name Validations
        if len(postData['last_name']) < 3: #Checks how long the Last Name is.
            results['errors'].append('Your Last Name is Too Short')
            results['status'] = False
        if ' ' in postData['last_name']: #Checks if there are any spaces in the Last Name
            results['errors'].append('There can not be any spaces in your Last Name')
            results['status'] = False
        if postData['last_name'].isalpha() != True: #Checks if characters are not letters
            results['errors'].append('Only Letters are allowed for your Last Name')
            results['status'] = False
#E-Mail Validations
        if not re.match("[^@]+@[^@]+\.[^@]+", postData['email']): #Checks validity of the email
            results['errors'].append('Your email is not valid')
            results['status'] = False
#Password Validations
        if len(postData['password']) < 8: #Checks the length of the password.
            results['errors'].append('Your password is too short')
            results['status'] = False
        if ' ' in postData['password']: #Checks if there are any spaces in the password.
            results['errors'].append('There can not be any spaces in your password')
            results['status'] = False  
        if postData['password'] != postData['c_password']: #Checks if the password and confirm password match.
            results['errors'].append("Your passwords don't match")
            results['status'] = False         
        if len(self.filter(email = postData['email'])) > 0: #Checks if the email already exists in the database.
            results['errors'].append('User already exists')
            results['status'] = False
        
        return results


        
class User(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    alias= models.CharField(max_length= 200, default="None")
    email = models.CharField(max_length = 200)
    bday = models.DateTimeField(default=datetime.now, blank=True)
    password = models.CharField(max_length= 200)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
  
    objects = UserManager()