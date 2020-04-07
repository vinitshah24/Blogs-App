python manage.py makemigrations
python manage.py sqlmigrate blogs 0001
python manage.py migrate
python manage.py shell


____________________________________________________________________________
from blogs.models import Post
from django.contrib.auth.models import User
User.objects.all()
<QuerySet [<User: root>]>

user = User.objects.filter(username='root').first()
user.username
user.id
user.pk
____________________________________________________________________________

post1 = Post(
    title='Blog1',
    content = 'First Blog',
    author = user
)
post1.save()
____________________________________________________________________________

post2 = Post(
    title='Blog2',
    content = 'Second Blog',
    author = user
)
post2.save()
____________________________________________________________________________

Post.objects.all()
____________________________________________________________________________

post = Post.objects.first()
post.date_posted
post.author
post.author.email
post.author.password

user = User.objects.filter(username='root').first()
user.post_set.all() #GETS ALL USER's POST
user.post_set.create(    
    title='Blog3',
    content = 'Third Blog',
)
Post.objects.all()
____________________________________________________________________________

from django.contrib.auth.models import User
user = User.objects.filter(username='root').first()
user
#Since profile has one-one relationship, it can be directly accessed
user.profile
user.profile.image
user.profile.image.height
user.profile.image.width
user.profile.image.url
____________________________________________________________________________

#Inserting Test Data

import json
from blogs.models import Post
with open('test_data.json') as f:
    json_file = json.load(f)
    for post in json_file:
        post = Post(
            title=post['title'],
            content=post['content'],
            author_id=post['user_id']
        )
        post.save()
____________________________________________________________________________

from django.core.paginator import Paginator
posts = ['Post1','Post2','Post3','Post4','Post5','Post6','Post7','Post8']
p = Paginator(posts,2)      # 2 Posts per page
p.num_pages                 # Get # of pages

for page in p.page_range:
    print(page)             # printing page #'s

p1 = p.page(1)              # Go to the page #
p1.number                   # Get the current page #
p1.object_list              # Get all the contents
p1.has_previous()           # Check if there is a previous page
p1.has_next()               # Check if there is a next page
p1.next_page_number()       # Get the next page #
