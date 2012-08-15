import re
from datetime import datetime
from django.shortcuts import render_to_response
from django.core.paginator import ObjectPaginator
from Bango.blog.models import Post

MONTH_NAMES = ('', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 
               'August', 'September', 'October', 'November', 'December')

BANGO_VERSION = "0.3.0"

def frontpage(request, pagenum = 0):
    posts, pagedata = init()

    max_single_posts_on_page = 5
    pages = ObjectPaginator(posts, max_single_posts_on_page)
    viewpage = pages.get_page(pagenum)
    pagedata['post_list'] = viewpage

    pagedata.update({'subtitle': '',
                     'pages': pages.pages,
                     'pagenum': int(pagenum),
                     'page_list': range(0, pages.pages) })
    return render_to_response(  'listpage.xhtml', pagedata)

def singlepost(request, year, month, slug2):
    posts, pagedata = init()
    post = posts.get(date_created__year=year,
                     date_created__month=int(month),
                     slug=slug2)
    pagedata.update({'post': post})
    return render_to_response('singlepost.xhtml', pagedata)

def yearview(request, year):
    posts, pagedata = init()
    posts = posts.filter(date_created__year=year)
    pagedata.update({'post_list': posts,
                     'subtitle': '%s' % year})
    return render_to_response('listpage.xhtml', pagedata);

def monthview(request, year, month):
    posts, pagedata = init()
    posts = posts.filter(date_created__year=year)
    posts = posts.filter(date_created__month=int(month))
    pagedata.update({'post_list': posts,
                     'subtitle': '%s %s' % (MONTH_NAMES[int(month)], year)})
    return render_to_response('listpage.xhtml', pagedata)

def tagview(request, tag):
    allposts, pagedata = init()
    posts = []
    for post in allposts:
        tags = re.split(' ', post.tags)
        if tag in tags:
            posts.append(post)
    pagedata.update({'post_list': posts,
                     'subtitle': "Kategoria: %s" % tag})
    return render_to_response('listpage.xhtml', pagedata)

def init():
    posts = Post.objects.all()
    tag_data = create_tag_data(posts)
    archive_data = create_archive_data(posts)
    pagedata = {'version' : BANGO_VERSION,
                'post_list': posts,
                'tag_counts': tag_data,
                'archive_counts': archive_data }
    return posts, pagedata

def create_archive_data(posts):
    archive_data = []
    count = {}
    mcount = {}
    for post in posts:
        year = post.date_created.year
        month = post.date_created.month
        if year not in count:
            count[year] = 1
            mcount[year] = {}
        else:
            count [year] += 1
        if month not in mcount[year]:
            mcount[year][month] = 1
        else:
            mcount[year][month] += 1
    for year in sorted(count.iterkeys(), reverse=True):
        archive_data.append({'isyear': True,
                             'year': year,
                             'count': count[year]})
        for month in sorted(mcount[year].iterkeys(), reverse=True):
            archive_data.append({'isyear': False,
                                 'yearmonth': '%d/%02d' % (year, month),
                                 'monthname': MONTH_NAMES[int(month)],
                                 'count': mcount[year][month]})
    return archive_data

def create_tag_data(posts):
    tag_data = []
    count = {}
    for post in posts:
        tags = re.split(" ", post.tags)
        for tag in tags:
            if tag not in count:
                count[tag] = 1
            else:
                count[tag] += 1
    for tag, count in sorted(count.iteritems(), key=lambda(k, v): (v, k), reverse=True):
        tag_data.append({'tag': tag,
                         'count': count})
    return tag_data 
