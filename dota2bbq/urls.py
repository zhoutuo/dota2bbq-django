from django.conf.urls import patterns, url

urlpatterns = patterns("dota2bbq.views",
    url(r"^$", "index"),
    url(r"^heroes/$", "heroes"),
    url(r"^items/$", "items"),
    url(r"^hero/(?P<hero_name>[\w ']+)/$", "hero"),
    url(r"^signin/$", "signin"),
    url(r"^signoff/$", "signoff"),
    url(r"^manage/$", "manage"),
    url(r"^manage/hero_create/$", "hero_create"),
    url(r"^manage/hero_edit/(?P<hero_name>[\w ']+)/$", "hero_edit"),
    url(r"^manage/hero_delete/(?P<hero_name>[\w ']+)/$", "hero_delete"),
    url(r"^manage/skill_edit/(?P<hero_name>[\w ']+)/$", "skill_edit"),
    url(r"^manage/skill_build/(?P<hero_name>[\w ']+)/$", "skill_build"),
    url(r"^manage/item_create/$", "item_create"),
    url(r"^manage/item_edit/(?P<item_name>[\w ']+)/$", "item_edit"),
    url(r"^manage/item_delete/(?P<item_name>[\w ']+)/$", "item_delete"),
    url(r"^ajax/combined/$", "combined_feed"),
    url(r"^ajax/items/$", "items_feed"),
)
