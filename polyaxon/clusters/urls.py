from django.urls import re_path

from rest_framework.urlpatterns import format_suffix_patterns

from libs.urls import SEQUENCE_PATTERN, INDEX_PATTERN
from clusters import views

clusters_urlpatterns = [
    re_path(r'^cluster/?$',
            views.ClusterDetailView.as_view()),
    re_path(r'^cluster/nodes/?$',
            views.ClusterNodeListView.as_view()),
]

cluster_nodes_urlpatterns = [
    re_path(r'^nodes/{}/?$'.format(SEQUENCE_PATTERN),
            views.ClusterNodeDetailView.as_view()),
    re_path(r'^nodes/{}/gpus/?$'.format(SEQUENCE_PATTERN),
            views.ClusterNodeGPUListView.as_view()),
    re_path(r'^nodes/{}/gpus/{}/?$'.format(SEQUENCE_PATTERN, INDEX_PATTERN),
            views.ClusterNodeGPUDetailView.as_view()),
]

urlpatterns = format_suffix_patterns(clusters_urlpatterns + cluster_nodes_urlpatterns)
