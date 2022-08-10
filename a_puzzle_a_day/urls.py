"""gac_aps URL Configuration
"""
from django.contrib import admin
# from django.shortcuts import redirect
from django.urls import path, include
# from django.views.generic import TemplateView, RedirectView
from rest_framework import routers

# For API documentation
# from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from games import views as games_view
from django.views.generic import TemplateView

schema_view = get_schema_view(
    openapi.Info(
        title="A-Puzzle-A-Day API Documentation",
        default_version='0.0.1',
        description="A-Puzzle-A-DayAPI说明文档",
    ),
    public=True,
    # permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui(
        'swagger', cache_timeout=0), name='schema-swagger'),
    path('redoc/', schema_view.with_ui(
        'redoc', cache_timeout=0), name='schema-redoc'),

    # url(r'^register/', CreateUserView.as_view()),
    # url(r'^logout/$', logout, {'next_page': '/'}),
    # url(r'^game/(?P<game_id>\d+)/$', GameView.as_view()),
    # url(r'^lobby/$', LobbyView.as_view()),

    path('', TemplateView.as_view(template_name="index.html")),


    path('get-game-rank-list/', games_view.get_game_rank_list, name='game_rank_list_api'),

    path('get-game-history-list/', games_view.get_game_history_list, name='game_history_list_api'),

    path('get-game-status/', games_view.get_game_status, name='game_status_api'),

    path('get-game-real-time-list/', games_view.get_game_real_time_list, name='game_real_time_api'),

    path('get-game-info-byid/', games_view.get_game_info_by_game_id, name='game_game_info_byid_api'),

    path('start-new-game/', games_view.start_new_game, name='start_new_game_api'),

    path('terminate-game/', games_view.terminate_game, name='abort_game_api'),

    path('login/', games_view.login, name='login_api'),

    path('register/', games_view.register, name='register_api'),

    path('logout/', games_view.logout, name='logout_api'),

    # 前端




]
