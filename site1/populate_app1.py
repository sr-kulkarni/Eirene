import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','site1.settings')
import django
django.setup()

from app1.models import Category, Page

def populate():
	child_cat = add_cat('Charities for Children')

	add_page(child_cat,title="Child Relief and You",url="www.cry.org")
	add_page(child_cat,title="Comic Relief",url="www.ba.com")
	add_page(child_cat,title="World Vision",url="www.worldvision.in")

	old_cat = add_cat('Charities for Old people')
	add_page(old_cat,title="Help Age India", url="www.helpageindia.org")

	gen_cat = add_cat('General Charities')
	add_page(gen_cat,title="Prime Ministers Relief Fund",url="www.irctc.in")
	add_page(gen_cat,title="United Way",url="www.unitedway.com")


	for c in Category.objects.all():
		for p in Page.objects.filter(category = c):
			print " {0} --> {1}".format(str(c),str(p))


def add_page(cat, title, url, views=0):
	p = Page.objects.get_or_create(category=cat,title=title)[0]
	p.url = url
	p.views = views
	p.save()
	return p

def add_cat(name):
	c = Category.objects.get_or_create(name=name)[0]
	c.views = 0
	c.likes = 0
	return c


if __name__ == '__main__':
	print "Populating the values"
	populate()