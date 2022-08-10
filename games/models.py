from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# class Player(models.Model):
#     user = models.CharField(max_length=20,
#                                     verbose_name="player username",
#                                     help_text="player username",)
#     password = models.CharField(max_length=30,
#                                 verbose_name="player password",
#                                 help_text="player password",)
#
#     created_at = models.DateTimeField(
#         auto_now_add=True,)
#     updated_at = models.DateTimeField(
#         auto_now=True,)
#
#     class Meta:
#         db_table = 'puzzle_player'
#         unique_together = ('user',)

# Not used
class PuzzlePieceTemplate(models.Model):
    class RotateStatusType(models.IntegerChoices):
        DEFALUT = (
            0, 'Default Status')
        DEFAULT_ROTATE_90 = (
            1, 'Default Rotate 90 Degrees'
        )
        DEFAULT_ROTATE_180 = (
            2, 'Default Rotate 180 Degrees'
        )
        DEFAULT_ROTATE_270 = (
            3, 'Default Rotate 270 Degrees'
        )
        FLIP = (
            4, 'Flip status')
        FLIP_ROTATE_90 = (
            5, 'Flip And Rotate 90 Degrees'
        )
        FLIP_ROTATE_180 = (
            6, 'Flip And Rotate 180 Degrees'
        )
        FLIP_ROTATE_270 = (
            7, 'Flip And Rotate 270 Degrees'
        )

    puzzle_num = models.CharField(
        max_length=20,
        verbose_name="puzzle number",
        help_text="puzzle number",
    )
    status_type = models.IntegerField(
        choices=RotateStatusType.choices,
        verbose_name="puzzle display status",
        help_text="puzzle display status",
    )
    shape = models.JSONField(
        verbose_name="puzzle default shape",
        help_text="puzzle deafult shape",
    )
    created_at = models.DateTimeField(
        auto_now_add=True, )
    updated_at = models.DateTimeField(
        auto_now=True, )

    class Meta:
        db_table = 'puzzle_component_template'
        unique_together = ('puzzle_num', 'status_type')


class Calendar(models.Model):
    month = models.IntegerField(
        verbose_name="puzzle month",
        help_text="puzzle month",
    )
    day = models.IntegerField(
        verbose_name="puzzle day",
        help_text="puzzle day",
    )
    created_at = models.DateTimeField(
        auto_now_add=True, )
    updated_at = models.DateTimeField(
        auto_now=True, )

    class Meta:
        db_table = 'puzzle_calendar'
        unique_together = ('month', 'day')


class Game(models.Model):
    class StatusType(models.IntegerChoices):
        ONGOING = (
            1, 'Game Ongoing')
        PASS = (
            2, 'Game Pass'
        )
        ABORT = (
            3, 'Game Abort'
        )

    game_name = models.CharField(
        max_length=20,
        verbose_name="game name",
        help_text="game name",
    )
    puzzle_calendar = models.ForeignKey(
        Calendar,
        related_name='puzzle_calendar',
        on_delete=models.PROTECT,
    )
    player = models.ForeignKey(User,
                               related_name='player',
                               on_delete=models.PROTECT, )
    status = models.IntegerField(
        choices=StatusType.choices,
        verbose_name="game status",
        help_text="game status", )
    cell_status = models.JSONField(
        max_length=100,
        null=True,
        verbose_name="game cell status",
        help_text="game cell status",
    )
    # game_name = models.
    duration = models.DurationField(
        null=True,
        verbose_name="game duration",
        help_text="game duration",
    )
    # dates
    created_at = models.DateTimeField(
        auto_now_add=True, )
    updated_at = models.DateTimeField(
        auto_now=True, )

    class Meta:
        db_table = 'puzzle_game'
#
# class GameHistory(models.Model):
#     game = models.ForeignKey(Game,on_delete=models.PROTECT)
#     player = models.ForeignKey(Player, null=True, blank=True,on_delete=models.PROTECT)
#     game_duration = models.DurationField(
#         verbose_name="game duration",
#         help_text="game duration",
#     )
#     created_at = models.DateTimeField(
#         auto_now_add=True,)
#     updated_at = models.DateTimeField(
#         auto_now=True,)
#     class Meta:
#         db_table = 'puzzle_game_history'
#         unique_together = ('game','player')
