import pickle
from itertools import product
# config
from typing import Dict, Tuple, List
import numpy as np
from operator import itemgetter

initial_instances = {
    "1": [
        {(1, 1), (2, 1), (3, 1), (3, 2), (3, 3)},
        {(3, 1), (3, 2), (3, 3), (2, 3), (1, 3)},
        {(1, 1), (1, 2), (1, 3), (2, 3), (3, 3)},
        {(1, 3), (1, 2), (1, 1), (2, 1), (3, 1)},
    ],
    '2': [
        {(1, 1), (1, 2), (2, 1), (3, 1), (3, 2)},
        {(1, 1), (1, 2), (2, 2), (3, 1), (3, 2)},
        {(1, 1), (2, 1), (2, 2), (2, 3), (1, 3)},
        {(1, 1), (2, 1), (1, 2), (2, 3), (1, 3)},
    ],
    "3": [
        {(1, 3), (2, 1), (2, 2), (2, 3), (3, 1)},
        {(1, 1), (2, 1), (2, 2), (2, 3), (3, 3)},
        {(1, 1), (1, 2), (2, 2), (3, 2), (3, 3)},
        {(3, 1), (1, 2), (2, 2), (3, 2), (1, 3)},
    ],
    "4": [
        {(2, 1), (2, 2), (2, 3), (1, 3), (1, 4)},
        {(1, 1), (1, 2), (2, 2), (2, 3), (2, 4)},
        {(1, 1), (2, 1), (2, 2), (3, 2), (4, 2)},
        {(1, 2), (2, 2), (2, 1), (3, 1), (4, 1)},
        {(1, 2), (2, 2), (3, 2), (3, 1), (4, 1)},
        {(1, 1), (2, 1), (3, 1), (3, 2), (4, 2)},
        {(2, 1), (2, 2), (1, 2), (1, 3), (1, 4)},
        {(1, 1), (1, 2), (1, 3), (2, 3), (2, 4)},
    ],


    "5": [
        {(1, 1), (1, 2), (2, 1), (2, 2), (3, 1), (3, 2)},
        {(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3)},
    ],
    "6": [
        {(1, 1), (2, 1), (3, 1), (2, 2), (3, 2)},
        {(1, 2), (2, 1), (3, 1), (2, 2), (3, 2)},
        {(1, 1), (1, 2), (1, 3), (2, 2), (2, 3)},
        {(2, 1), (1, 2), (1, 3), (2, 2), (2, 3)},
        {(1, 1), (2, 1), (1, 2), (2, 2), (3, 1)},
        {(1, 1), (2, 1), (1, 2), (2, 2), (3, 2)},
        {(1, 1), (2, 1), (1, 2), (2, 2), (1, 3)},
        {(1, 1), (2, 1), (1, 2), (2, 2), (2, 3)},
    ],
    "7": [
        {(1, 1), (1, 2), (1, 3), (1, 4), (2, 3)},
        {(1, 1), (1, 2), (1, 3), (1, 4), (2, 2)},
        {(2, 1), (2, 2), (2, 3), (2, 4), (1, 3)},
        {(2, 1), (2, 2), (2, 3), (2, 4), (1, 2)},
        {(1, 2), (2, 2), (3, 2), (4, 2), (2, 1)},
        {(1, 2), (2, 2), (3, 2), (4, 2), (3, 1)},
        {(1, 1), (2, 1), (3, 1), (4, 1), (2, 2)},
        {(1, 1), (2, 1), (3, 1), (4, 1), (3, 2)},
    ],
    "8": [
        {(2, 1), (2, 2), (2, 3), (2, 4), (1, 4)},
        {(1, 1), (1, 2), (2, 2), (3, 2), (4, 2)},
        {(2, 1), (1, 1), (1, 2), (1, 3), (1, 4)},
        {(1, 1), (2, 1), (3, 1), (4, 1), (4, 2)},
        {(1, 1), (2, 1), (2, 2), (2, 3), (2, 4)},
        {(4, 1), (4, 2), (3, 2), (2, 2), (1, 2)},
        {(1, 1), (1, 2), (1, 3), (1, 4), (2, 4)},
        {(1, 2), (1, 1), (2, 1), (3, 1), (4, 1)},
    ],
}

pickle_piece_conversion = {'1':'F',
                           '2':'A',
                           '3':'C',
                           '4':'D',
                           '5':'B',
                           '6':'G',
                           '7':'H',
                           '8':'E'}

month_conversion = {
    (1, 1): "Jan",
    (1, 2): "Feb",
    (1, 3): "Mar",
    (1, 4): "Apr",
    (1, 5): "May",
    (1, 6): "Jun",
    (2, 1): "Jul",
    (2, 2): "Aug",
    (2, 3): "Sep",
    (2, 4): "Oct",
    (2, 5): "Nov",
    (2, 6): "Dec",
}

# Get all cells and their corresponding characters,get puzzle board coordinate
def get_text_conversion() -> Dict[Tuple[int, int], str]:
    text_conversion = dict()
    for p in product(range(1, 8), range(1, 8)):
        text_conversion[p] = ""
    for coords, month in month_conversion.items():
        text_conversion[coords] = month

    count = 1
    for r in range(3, 8):
        for c in range(1, 8):
            if count < 32:
                text_conversion[(r, c)] = str(count)
            count += 1
    return text_conversion

# open solution dict
with open('calendar_solution_dict.pickle', 'rb') as f:
    solution_pickle = pickle.load(f)

# conversion ,
text_conversion = get_text_conversion()

class Game():
    def get_key_by_value(self, value:str) -> List[Tuple[int,int]]:
        return [list(text_conversion.keys())[list(text_conversion.values()).index(value)]]

    # Get the cell corresponding to the given date, contains two cells
    def get_month_day_cell(self, month:int, day:int) ->List[Tuple[int,int]]:
        month = month_conversion[list(month_conversion.keys())[month-1]]
        month_cell = self.get_key_by_value(month)
        day_cell = self.get_key_by_value(str(day))
        return month_cell + day_cell

    # 7维矩阵
    def get_unoccupied_cell(self,occupied_cell:List[List[int]]) -> List[Tuple[int,int]]:
        cell_list = list(np.array(occupied_cell).flatten())
        base_cell_list = list(text_conversion.keys())
        unoccupied_index = [base_cell_list[x] for (x,y) in enumerate(cell_list) if y == 0]
        return unoccupied_index


    # Judge whether the game passes
    def get_game_status(self,month:int,day:int,occupied_cell:List[List[int]]) ->bool:
        # get calendar cell
        puzzle_calendar_cell = self.get_month_day_cell(month,day)
        unoccupied_cell = self.get_unoccupied_cell(occupied_cell)
        if set(puzzle_calendar_cell) == set(unoccupied_cell):
            return True
        else:
            return False


    # # game solveable
    # def get_calendar_solution_pickle(self):
    #     with open('calendar_solution_dict.pickle','rb') as f:
    #         return pickle.load(f)

    #
    def get_cell_positions(self,occupied_cell:List[List[int]]):
        cell_list = np.array(occupied_cell).flatten()
        pieces = set(i for  i in  set(cell_list) if i > 0)
        cell_occupied = set()
        cell_occupied = set.union(cell_occupied,set(list(text_conversion.keys())[i] for  i ,j in enumerate(cell_list) if j > 0 ))
        return pieces,cell_occupied

    def get_calendar(self,month:int,day:int):
        return '-'.join([list(month_conversion.values())[month-1],str(day).zfill(2)])

    def check_game_solvable(self,month:int,day:int,occupied_cell:List[List[int]],):
        pieces, cell_positions = self.get_cell_positions(occupied_cell)
        base_solutions = solution_pickle.get(self.get_calendar(month,day))
        # get occupied cell
        cell_occupied = set(list(cell_positions))
        # get used piece
        used_piece = [pickle_piece_conversion.get(str(piece)) for  piece in pieces]
        if len(used_piece) == 0:
            return True
        else:
            for solution in base_solutions:
                piece_solutions = itemgetter(*used_piece)(solution)
                piece_solution = set()
                if len(used_piece) == 1:
                    piece_solution = set.union(piece_solution, piece_solutions)
                else:
                    for i in piece_solutions:
                        piece_solution = set.union(piece_solution,i)
                if cell_occupied == piece_solution:
                    return True
                else:
                    continue

    #
    # def all_possible_positions(self):
    #     result = dict()
    #     for letter, variants in initial_instances.items():
    #         result[letter] = list()
    #         letter_rows = letter_cols = 0
    #         for variant in variants:
    #             letter_rows = max([int(n[0]) for n in variant])
    #             letter_cols = max([int(n[1]) for n in variant])
    #             for i in range(7 - letter_rows + 1):
    #                 for j in range(7 - letter_cols + 1):
    #                     result[letter].append({(n[0] + i, n[1] + j) for n in variant})
    #     return result
    #
    # def location_available(self,occupied_cell:List[List[int]]) ->bool:
    #     '''True if cells in variant do not intersect with cell_not_allowed
    #     cells_not_allowed = self.get_unoccupied_cell(occupied_cell)
    #     cell_list = set(np.array(occupied_cell).flatten())
    #     origin_piece = [1,2,3,4,5,6,7,8]
    #     piece_unused = set(origin_piece).difference({i for i in cell_list if i >0})
    #     months_locations = set(month_conversion.keys())
    #     possible_positions = self.all_possible_positions()
    #     for piece in piece_unused:
    #         variants = initial_instances.get(str(piece))
    #         for variant in variants:
    #             if (
    #                     len(set.intersection(months_locations, set.union(set(cells_not_allowed), variant)))
    #                     == 12
    #             ):
    #                 return False
    #
    #             for cell in variant:
    #                 if cell in cells_not_allowed:
    #                     return False
    #         return True


    # def get_unoccupied_cell(self,used_cell: Dict[str,List[Tuple[int,int]]]) ->List[Tuple[int,int]]:
    #     """return  the unoccupied cell"""
    #     base_cell = list(self.text_conversion.keys())
    #     for letter, cells in used_cell.items():
    #         base_cell = list(set(base_cell).difference(set(cells)))
    #     return base_cell

