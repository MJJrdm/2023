#TODO: 现在前后端对接是每秒调用一次接口，之后应考虑使用websocket
import datetime
from typing import List, Dict

from django.db.models import Min, Q

from games import models
from django.contrib.auth.models import User
from numpy import ceil, arange
from .games_service import Game
import logging

LOGGER = logging.getLogger(__name__)

class GameStatusChange():
    def change(self):
        running_game = models.Game.objects.filter(status= 1)
        if running_game.exists() is True:
            for game in running_game:
                now = datetime.datetime.now()
                update = game.updated_at.replace(tzinfo=None)
                delta = now - update
                if delta.seconds > 5:
                    game.status = 3
                    game.save()
                else:
                    continue
        else:
            LOGGER.info('No running game')


# game rank list
class GameRankListService():
    def get_page_number(self, pagesize: int) -> int:
        rank_list_query = models.Game.objects.filter(status=2).values('player__username').annotate(
            min_duration=Min('duration')).order_by('min_duration', 'id').values('player__username', 'game_name',
                                                                                'puzzle_calendar__month',
                                                                                'puzzle_calendar__day', 'duration')
        pagenumber = ceil(len(rank_list_query) / pagesize)
        return pagenumber

    def list(self, pagination: int, pagesize: int):
        GameStatusChange().change()
        rank_list = []
        rank_list_query = models.Game.objects.filter(status=2).values('player__username').annotate(
            min_duration=Min('duration')).order_by('min_duration', 'id').values('player__username', 'game_name',
                                                                                'puzzle_calendar__month',
                                                                                'puzzle_calendar__day', 'duration')
        pagenumber = ceil(len(rank_list_query) / pagesize)
        if pagination <= pagenumber and pagination > 0:
            if len(rank_list_query)>0:
                list_id_range = arange((pagination - 1) * pagesize + 1, (pagination) * pagesize + 1)
                for index in list_id_range:
                    if index <= len(rank_list_query):
                        item = rank_list_query[int(index) - 1]
                        rank_list.append({'rank': index,
                                          'player': item.get('player__username'),
                                          'puzzle_date': '.'.join([str(item.get('puzzle_calendar__month')),
                                                                   str(item.get('puzzle_calendar__day'))]),
                                          'puzzle_duration': item.get('duration'), })
                        # 'pagination':pagination,
                        # 'pagesize':pagesize,
                        # 'total_records':len(rank_list_query)
                    else:
                        continue
                return len(rank_list_query), rank_list

            else:
                return len(rank_list_query), rank_list
        else:
            return len(rank_list_query), rank_list


#TODO:需添加查询玩家的游戏记录功能。
# game history list
class GameHistoryListService():
    def list(self, pagination: int, pagesize: int):
        GameStatusChange().change()
        history_list = []
        history_list_query = models.Game.objects.filter(status__in=[2, 3]).order_by('-created_at').values(
            'player__username', 'game_name', 'puzzle_calendar__month', 'puzzle_calendar__day', 'duration', 'created_at',
            'status')
        pagenumber = ceil(len(history_list_query) / pagesize)
        if pagination <= pagenumber and pagination > 0:
            list_id_range = arange((pagination - 1) * pagesize + 1, (pagination) * pagesize + 1)
            if len(history_list_query) >0:
                for index in list_id_range:
                    if index <= len(history_list_query):
                        item = history_list_query[int(index) - 1]
                        status = '中止' if item.get('status') == 3 else '通关'
                        history_list.append({'rank': index,
                                             'game_name': item.get('game_name'),
                                             'player': item.get('player__username'),
                                             'puzzle_date': '.'.join([str(item.get('puzzle_calendar__month')),
                                                                      str(item.get('puzzle_calendar__day'))]),
                                             'puzzle_start': item.get('created_at'),
                                             'puzzle_duration': item.get('duration'),
                                             'status': status, })
                        # 'pagination':pagination,
                        # 'pagesize':pagesize,
                        # 'total_records':len(history_list_query)
                    else:
                        continue
                return len(history_list_query), history_list

            else:
                return len(history_list_query) , history_list
        else:
            return len(history_list_query), history_list


class GameRealTimeService():
    def list(self, pagination: int, pagesize: int):
        GameStatusChange().change()
        real_time_list = []
        real_time_list_query = models.Game.objects.filter(status=1).order_by('-created_at').values('player__username', 'id',
                                                                                                   'game_name',
                                                                                                   'puzzle_calendar__month',
                                                                                                   'puzzle_calendar__day',
                                                                                                   'duration',
                                                                                                   'cell_status')
        pagenumber = ceil(len(real_time_list_query) / pagesize)
        if pagination <= pagenumber and pagination > 0:
            list_id_range = arange((pagination - 1) * pagesize + 1, (pagination) * pagesize + 1)
            if len(list_id_range) > 0:
                for index in list_id_range:
                    if index <= len(real_time_list_query):
                        item = real_time_list_query[int(index) - 1]
                        real_time_list.append({'rank': index,
                                               'game_id': item.get('id'),
                                               'game_name': item.get('game_name'),
                                               'player': item.get('player__username'),
                                               'puzzle_date': '.'.join([str(item.get('puzzle_calendar__month')),
                                                                        str(item.get('puzzle_calendar__day'))]),
                                               'puzzle_duration': item.get('duration'),  # TODO:修改已拼时间
                                               'puzzle_cell': item.get('cell_status'), })
                        # 'pagination':pagination,
                        # 'pagesize':pagesize,
                        # 'total_records':len(real_time_list_query)
                    else:
                        continue
                return len(real_time_list_query), real_time_list
            else:
                return len(real_time_list_query), real_time_list
        else:
            return len(real_time_list_query), real_time_list



class GameTerminate():
    def abort_game(self, game_id: int):
        # check game  over,Bool
        # update data
        game_query = models.Game.objects.all().filter(id=game_id)
        if game_query.exists() is True :
            game = game_query[0]
            game.status = 3 if game.status !=2 else 2
            game.save()


class GameStart():
    def start_game(self, game_name: str, player_name: str, month: int, day: int):
        player = User.objects.get(username=player_name)
        calendar = models.Calendar.objects.get_or_create(month=month, day=day)
        # if models.Game.objects.filter(Q(game_name=game_name) & Q(player=player)).exists() is False:
        instance = models.Game.objects.create(game_name=game_name, player=player, puzzle_calendar=calendar[0],
                                              status=1)
        return {'game_id': instance.id}


class GameStatusCheckService():
    def get_game_status(self, game_id: int, duration_seconds: int, puzzle_cell: List[List[int]], ):
        game_query = models.Game.objects.filter(id=game_id).values('puzzle_calendar__month', 'puzzle_calendar__day',
                                                                   'duration', 'cell_status', 'status')
        if game_query.exists() is True:
            game = models.Game.objects.get(id=game_id)
            month, day = game_query[0].get('puzzle_calendar__month'), game_query[0].get('puzzle_calendar__day')
            # check game  over,Bool
            game_status = Game().get_game_status(month, day, puzzle_cell)
            # update data
            game.duration = datetime.timedelta(seconds=duration_seconds)
            game.cell_status = puzzle_cell
            if game_status == True:  # TODO:change to close thread
                game.status = 2
            game.save()

            # # check game solveable: bool
            # solvable = Game().check_game_solvable(month, day, puzzle_cell)
            # solvable = False if solvable is None else solvable
            return {"game_id": game_id,
                    # "solvable": solvable,
                    "game_over": game_status}


class GameStatus():
    def info(self,game_id:int):
        game_query = models.Game.objects.filter(id= game_id).values('player__username', 'id','game_name','puzzle_calendar__month',
                                                                     'puzzle_calendar__day','duration','cell_status')
        if game_query.exists() is True:
            game = game_query[0]
            return {'game_id': game.get('id'),
                   'game_name': game.get('game_name'),
                   'player': game.get('player__username'),
                   'puzzle_date': '.'.join([str(game.get('puzzle_calendar__month')),
                                            str(game.get('puzzle_calendar__day'))]),
                   'puzzle_duration':game.get('duration'),
                   'puzzle_cell': game.get('cell_status'), }





