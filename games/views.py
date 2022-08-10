# from django.shortcuts import render
from django.contrib import auth
from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers, status, generics
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django_filters import rest_framework as filters
from games import games_crud_service
from games.user_curd_sevice import UserInfoCRUDService

# Create your views here.

"""
login and register
"""


class UserInfoSerializer(serializers.Serializer):
    username = serializers.CharField(
        label="用户名",
        help_text="用户名", )

    password = serializers.CharField(
        allow_null=True,
        label="密码",
        help_text="密码",
    )

class UserLogoutRequestSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(
        label="用户id",
        help_text="用户id", )

@swagger_auto_schema(
    methods=['POST'],
    operation_summary="登录",
    request_body=UserInfoSerializer(),
    responses={'200': '登录成功',
               # '500_1': '登录输入的用户名不存在',
               # '500_2': '登录输入的密码不正确',
               '403': '用户名或密码不正确',
               }
)
@api_view(['POST'])
def login(request, *args, **kwargs):
    try:
        if request.method == 'POST':
            serializer = UserInfoSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            # user_query = UserInfoCRUDService().get(
            #     user_name=serializer.validated_data.get('username'))
            # password = serializer.validated_data.get('password')
            # if user_query.exists() is True:
            #     if user_query[0]["password"] == password:
            #         return Response(status=status.HTTP_200_OK, data={'code': '200', 'data': '登录成功'})
            #     else:
            #         return Response(status=status.HTTP_200_OK, data={'code': '500_2', 'data': '登录输入的密码不正确'})
            # else:
            #     return Response(status=status.HTTP_200_OK, data={'code': '500_1', 'data': '登录输入的用户名不存在'})
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')
            if username is None or password is None:
                return Response({"code": "500", "message": "请求参数错误", "data": ""})

            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                token_query_set = Token.objects.filter(user=user).values()
                if token_query_set.exists() is True:
                    token = token_query_set[0]['key']
                else:
                    token_create = Token.objects.create(user=user)
                    token = token_create.key                 
                response = {
                    "code": "200",
                    "message": "用户登录成功",
                    "data": {"user_id": user.id, "user_name": username, "token": token},
                }
            else:
                response = {
                    "code": "403",
                    "message": "用户名或密码错误",
                    "data": "",
                }
            return Response(response)
    except Exception as e:
        return Response(data={"code": "400", "message": u"error:{}".format(e), "data": ""},
                        status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    methods=['POST'],
    operation_summary="注销",
    request_body=UserLogoutRequestSerializer(),
    responses={'200': '成功退出',
               '403': '该用户未登录',
               }
)
@api_view(['POST'])
def logout(request, *args, **kwargs):
    try:
        if request.method == 'POST':
            serializer = UserLogoutRequestSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user_id = serializer.validated_data.get("user_id")
            old_token = Token.objects.filter(user_id=user_id)
            if old_token.exists() is True:
                old_token.delete()
                auth.logout(request)
                return Response({"code": "200", "message": "成功退出", "data": {"user_id": user_id}})
            else:
                return Response({"code": "403", "message": "该用户未登录", "data": ""})
    except Exception as e:
        return Response(data={"code": "400", "message": u"error:{}".format(e), "data": ""},
                        status=status.HTTP_400_BAD_REQUEST)



@swagger_auto_schema(
    methods=['POST'],
    operation_summary="注册",
    request_body=UserInfoSerializer(),
    responses={'200': '注册成功',
               '500_1': '注册输入的用户名已存在'}
)
@swagger_auto_schema(method='PUT',
                     operation_summary="重置密码",
                     operation_description="重置密码",
                     request_body=UserInfoSerializer(),
                     responses={'200': '密码重置成功',
                                '500_2': '重置输入的用户名不存在',
                                })
@api_view(['POST', 'PUT'])
def register(request, *args, **kwargs):
    try:
        if request.method == 'POST':
            serializer = UserInfoSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')
            user_query = UserInfoCRUDService().get(
                user_name=username)
            if user_query.exists() is True:
                return Response(status=status.HTTP_200_OK,
                                data={"code": "500_1", "message": "注册输入的用户名已存在", "data": ""})
            else:
                UserInfoCRUDService().create(user_name=username, password=password)
                return Response(status=status.HTTP_200_OK,
                                data={"code": "200", "message": "注册成功", "data": ""})
        if request.method == 'PUT':
            serializer = UserInfoSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')
            user_query = UserInfoCRUDService().get(
                user_name=username)
            if user_query.exists() is True:
                UserInfoCRUDService().put(user_name=username, password=password)
                return Response(status=status.HTTP_200_OK,
                                data={"code": "200", "message": "重置密码成功", "data": ""})
            else:
                return Response(status=status.HTTP_200_OK,
                                data={"code": "500_2", "message": "重置输入的用户名不存在", "data": ""})
    except Exception as e:
        return Response(data={"code": "400", "message": u"error:{}".format(e), "data": ""},
                        status=status.HTTP_400_BAD_REQUEST)


class PaginationSerializer(serializers.Serializer):
    pagination = serializers.IntegerField(
        label="输入页码",
        help_text="输入页码",
    )
    pagesize = serializers.IntegerField(
        label="输入每页显示条数",
        help_text="输入每页显示条数",
    )


"""
Game Rank List view
"""


class GameRankListSerializer(serializers.Serializer):
    rank = serializers.IntegerField(
        read_only=True,
        label="game rank",
        help_text="game rank", )
    player = serializers.CharField(
        read_only=True,
        label="game player",
        help_text="game player",
    )
    puzzle_date = serializers.CharField(
        read_only=True,
        label="puzzle_date",
        help_text="puzzle_date",
    )
    puzzle_duration = serializers.DurationField(
        read_only=True,
        label="puzzle duration",
        help_text="puzzle duration",
    )


@swagger_auto_schema(
    methods=['POST'],
    operation_summary="返回排行榜数据，",
    request_body=PaginationSerializer(),
    responses={200: GameRankListSerializer()},

)
@api_view(['POST'])
def get_game_rank_list(request, *args, **kwargs):
    try:
        if request.method == 'POST':
            serializer = PaginationSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            total_records, game_rank_list = games_crud_service.GameRankListService().list(
                pagination=serializer.validated_data.get('pagination'),
                pagesize=serializer.validated_data.get('pagesize'))
            serializer = GameRankListSerializer(
                game_rank_list, many=True)
            response = {"code": "200", "data": serializer.data,"message":'', "total": total_records}
            return Response(response)

    except Exception as e:
        response = {"code": "400", "data": '',"message":{"err_msg": u"error:{}".format(e)}, "total": ""}
        return Response(response)
        # return Response(data={'err_msg': u'error:{}'.format(e)},
        #                 status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_200_OK)


class GameHistoryListSerializer(serializers.Serializer):
    rank = serializers.IntegerField(
        read_only=True,
        label="game rank",
        help_text="game rank", )
    game_name = serializers.CharField(
        read_only=True,
        label="game name",
        help_text="game name",
    )
    player = serializers.CharField(
        read_only=True,
        label="game player",
        help_text="game player",
    )
    puzzle_date = serializers.CharField(
        read_only=True,
        label="puzzle_date",
        help_text="puzzle_date",
    )
    puzzle_start = serializers.DateTimeField(
        read_only=True,
        label="puzzle game start time ",
        help_text="puzzle game start time ",
    )
    puzzle_duration = serializers.DurationField(
        read_only=True,
        label="puzzle duration",
        help_text="puzzle duration",
    )
    status = serializers.CharField(
        read_only=True,
        label="puzzle game status",
        help_text="puzzle game status",
    )


@swagger_auto_schema(
    methods=['POST'],
    operation_summary="Return Game History List .",
    request_body=PaginationSerializer(),
    responses={200: GameHistoryListSerializer()}
)
@api_view(['POST'])
def get_game_history_list(request, *args, **kwargs):
    try:
        if request.method == 'POST':
            serializer = PaginationSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            total_records, game_history_list = games_crud_service.GameHistoryListService().list(
                pagination=serializer.validated_data.get('pagination'),
                pagesize=serializer.validated_data.get('pagesize'))
            serializer = GameHistoryListSerializer(
                game_history_list, many=True)
            response = {"code": "200", "data": serializer.data,"message":'',"total": total_records}
            return Response(response)

    except Exception as e:
        response = {"code": "400", "data":'',"message": {"err_msg": u"error:{}".format(e)}, "total": ""}
        return Response(response)
        # return Response(data={'err_msg': u'error:{}'.format(e)},
        #                 status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_200_OK)


class GameRealTimeListSerializer(serializers.Serializer):
    rank = serializers.IntegerField(
        read_only=True,
        label="game rank",
        help_text="game rank", )
    game_id = serializers.IntegerField(
        read_only=True,
        label="game id",
        help_text="game id",
    )
    game_name = serializers.CharField(
        read_only=True,
        label="game name",
        help_text="game name",
    )
    player = serializers.CharField(
        read_only=True,
        label="game player",
        help_text="game player",
    )
    puzzle_date = serializers.CharField(
        read_only=True,
        label="puzzle_date",
        help_text="puzzle_date",
    )
    puzzle_duration = serializers.DurationField(
        read_only=True,
        label="puzzle duration",
        help_text="puzzle duration",
    )
    puzzle_cell = serializers.ListField(
        read_only=True,
        label="puzzle cell status",
        help_text="puzzle cell satus",
    )


@swagger_auto_schema(
    methods=['POST'],
    operation_summary="实时游戏大厅.",
    request_body=PaginationSerializer(),
    responses={200: GameRealTimeListSerializer()}
)
@api_view(['POST'])
def get_game_real_time_list(request, *args, **kwargs):
    try:
        if request.method == 'POST':
            serializer = PaginationSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            total_records, game_real_time_list = games_crud_service.GameRealTimeService().list(
                pagination=serializer.validated_data.get('pagination'),
                pagesize=serializer.validated_data.get('pagesize'))
            serializer = GameRealTimeListSerializer(
                game_real_time_list, many=True)
            response = {"code": "200", "data": serializer.data, "message": "", "total": total_records}
            return Response(response)

    except Exception as e:
        response = {"code": "400", "message": {"err_msg": u"error:{}".format(e)},"data":'', "total": ""}
        return Response(response)
    return Response(status=status.HTTP_200_OK)


class GameStatusRequestSerializer(serializers.Serializer):
    game_id = serializers.IntegerField(
        label='game id',
        help_text="game id",
    )
    duration_seconds = serializers.IntegerField(
        label="Game Duration Seconds",
        help_text="Game Duration Seconds",
    )
    puzzle_cell = serializers.ListField(
        label="Game real-time coordinates",
        help_text="Game real-time coordinates",
    )


class GameStatusListSerializer(serializers.Serializer):
    game_id = serializers.IntegerField(
        label='game id',
        help_text="game id",
    )
    # solvable = serializers.BooleanField(
    #     read_only=True,
    #     label="Whether Game Is Solvable",
    #     help_text="Whether Game Is Solvable",
    # )
    game_over = serializers.BooleanField(
        read_only=True,
        label="Whether Game Is Over",
        help_text="Whether Game Is Over",
    )


@swagger_auto_schema(
    methods=['POST'],
    operation_summary="返回各游戏实时状态列表.",
    request_body=GameStatusRequestSerializer(),
    responses={200: GameStatusListSerializer()}
)
@api_view(['POST'])
def get_game_status(request, *args, **kwargs):
    try:
        if request.method == 'POST':
            serializer = GameStatusRequestSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            game_status_list = games_crud_service.GameStatusCheckService().get_game_status(
                game_id=serializer.validated_data.get('game_id'),
                duration_seconds=serializer.validated_data.get('duration_seconds'),
                puzzle_cell=serializer.validated_data.get('puzzle_cell'),
            )
            serializer = GameStatusListSerializer(
                game_status_list)
            response = {"code": "200", "data": serializer.data,"message":'', "total": len(serializer.data)}
            return Response(response)
    except Exception as e:
        response = {"code": "400","data":'', "message": {"err_msg": u"error:{}".format(e)}, "total": ""}
        return Response(response)
    return Response(status=status.HTTP_200_OK)


class GameStartSerializer(serializers.Serializer):
    game_name = serializers.CharField(
        label="game name",
        help_text="game name",
    )
    player = serializers.CharField(
        label="game player",
        help_text="game player",
    )
    month = serializers.IntegerField(
        label="Puzzle month",
        help_text="Puzzle month",
    )
    day = serializers.IntegerField(
        label="Puzzle day",
        help_text="Puzzle day",
    )


class GameStartReponseSerializer(serializers.Serializer):
    game_id = serializers.IntegerField(
        label="game id ",
        help_text="game id",
    )


@swagger_auto_schema(
    methods=['POST'],
    operation_summary="开始游戏.",
    request_body=GameStartSerializer(),
    responses={200: GameStartReponseSerializer()}
)
@api_view(['POST'])
def start_new_game(request, *args, **kwargs):
    try:
        if request.method == 'POST':
            serializer = GameStartSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            game_id = games_crud_service.GameStart().start_game(
                game_name=serializer.validated_data.get('game_name'),
                player_name=serializer.validated_data.get('player'),
                month=serializer.validated_data.get('month'),
                day=serializer.validated_data.get('day'))
            serializer = GameStartReponseSerializer(
                game_id)
            if game_id is not None:
                response = {"code": "200", "data": serializer.data,"message":'', "total": len(serializer.data)}
                return Response(response)
            else:
                response = {"code": "400","data":'', "message": {"err_msg": u" repeating data"}, "total": ""}
                return Response(response)
    except Exception as e:
        response = {"code": "400","data":'', "message": {"err_msg": u"error:{}".format(e)}, "total": ""}
        return Response(response)
    return Response(status=status.HTTP_200_OK)


class GameTerminateSerializer(serializers.Serializer):
    game_id = serializers.IntegerField(
        label="game id ",
        help_text="game id",
    )


@swagger_auto_schema(
    methods=['POST'],
    operation_summary="停止游戏.",
    request_body=GameTerminateSerializer(),
    responses={200: 'HTTP Status'}
)
@api_view(['POST'])
def terminate_game(request, *args, **kwargs):
    try:
        if request.method == 'POST':
            serializer = GameTerminateSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            games_crud_service.GameTerminate().abort_game(game_id=serializer.validated_data.get('game_id'))
            response = {"code": "200", "data": "","message":'', "total": ""}
            return Response(response)
    except Exception as e:
        response = {"code": "400","data" :'',"message": {"err_msg": u"error:{}".format(e)}, "total": ""}
        return Response(response)
    return Response(status=status.HTTP_200_OK)





class GameStatusSerializer(serializers.Serializer):
    game_id = serializers.IntegerField(
        label="game id ",
        help_text="game id",
    )

class GameStatusResponseSerializer(serializers.Serializer):
    game_id = serializers.IntegerField(
        read_only=True,
        label="game id",
        help_text="game id",
    )
    game_name = serializers.CharField(
        read_only=True,
        label="game name",
        help_text="game name",
    )
    player = serializers.CharField(
        read_only=True,
        label="game player",
        help_text="game player",
    )
    puzzle_date = serializers.CharField(
        read_only=True,
        label="puzzle_date",
        help_text="puzzle_date",
    )
    puzzle_duration = serializers.DurationField(
        read_only=True,
        label="puzzle duration",
        help_text="puzzle duration",
    )
    puzzle_cell = serializers.ListField(
        read_only=True,
        label="puzzle cell status",
        help_text="puzzle cell satus",
    )


@swagger_auto_schema(
    methods=['POST'],
    operation_summary="获取游戏详细信息.",
    request_body=GameStatusSerializer(),
    responses={200: GameStatusResponseSerializer()}
)
@api_view(['POST'])
def get_game_info_by_game_id(request, *args, **kwargs):
    try:
        if request.method == 'POST':
            serializer = GameStatusSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            game_info = games_crud_service.GameStatus().info(game_id=serializer.validated_data.get('game_id'))

            if game_info is not None:
                serializer = GameStatusResponseSerializer(
                    game_info)
                response = {"code": "200", "data": serializer.data,"message":'', "total": ""}
                return Response(response)
            else:
                response = {"code": "400", "data": '', "message": {"please check game id"}, "total": ""}
                return Response(response)
    except Exception as e:
        response = {"code": "400","data" :'',"message": {"err_msg": u"error:{}".format(e)}, "total": ""}
        return Response(response)
    return Response(status=status.HTTP_200_OK)


