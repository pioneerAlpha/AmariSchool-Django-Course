from django.db import models

class Testimonial(models.Model):
    address=models.CharField(max_length=100)
    rating=models.FloatField()
    img=models.ImageField(upload_to='picture')
    name=models.CharField(max_length=20)
    ocupation=models.CharField(max_length=100)
    opinion=models.TextField()
  


'''
'rating':4.9
'img':'img/testimonials/testimonials-5.jpg'
'name':'Samiur Abir'
'ocupation':'Freelancer'
'opinion':' Proin iaculis purus consequat sem cure digni ssim donec porttitora entum suscipit rhoncus. Accusantium quam, ultricies eget id, aliquam eget nibh et. Maecen aliquam, risus at semper.'

'''