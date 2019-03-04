from dots import DotsBoxesBoard
from dots import PLAYER1,PLAYER2,EMPTY,MAXSIZE
from sys import stdin, stdout

board = DotsBoxesBoard(7)

class GameController():
    def __init__(self, board):
        self.version = "v0.1"
        self.board = board
        self.commands = {
            "version": self.version_cmd,
            "quit": self.quit_cmd,
            "name": self.name_cmd,
            "boardsize": self.boardsize_cmd,
            "showboard": self.showboard_cmd,
            "clear_board": self.clear_board_cmd,
            "user_guide": self.user_guide_cmd,
            "cmputmov": self.cmputmov_cmd,
            "move": self.move_cmd,
            "legal_moves": self.legal_moves_cmd,
            # add timelimit
            "timelimit": self.timelimit_cmd,
            "solve": self.solvegame

        }
    def version_cmd(self, args):
        print("current version is: "+self.version)

    def quit_cmd(self,args):
        print("Exit the game.")
        exit(1)

    def name_cmd(self,args):
        print("Dots and Boxes.")

    def boardsize_cmd(self,args):
        print("This is a {}x{} game.".format(self.board.width,self.board.length))

    def showboard_cmd(self,args):
    #     print board
        print('----')

    def clear_board_cmd(self,args):
        self.board.reset(self.board.width,self.board.length)

    def user_guide_cmd (self,args):
    #     print user guide
        print('-------')

    def cmputmov_cmd (self,args):
    # a move shall made by computer
        print('-------')

    def color_to_int(self,color):
        """convert character to the appropriate integer code"""
        color_to_int = {"p1": PLAYER1, "p2": PLAYER2, "e": EMPTY}
        return color_to_int[color]
    def move_to_coord(self, point_str, board_size):
        if not 2 <= board_size <= MAXSIZE:
            raise ValueError("board_size out of range")
        s = point_str.lower()
        try:
            col_c = s[0]
            if (not "a" <= col_c <= "z") or col_c == "i":
                raise ValueError
            col = ord(col_c) - ord("a")
            if col_c < "i":
                col += 1
            row = int(s[1:])
            if row < 1:
                raise ValueError
        except (IndexError, ValueError):
            raise ValueError("illegal move: \"{}\" wrong coordinate".format(s))
        if not (col <= board_size and row <= board_size):
            raise ValueError("illegal move: \"{}\" wrong coordinate".format(s))
        return row, col
    def move_cmd (self,args):
        # black player 1, white player 2
        try:
            board_color = args[0].lower()
            board_move = args[1]
            if board_color != "p1" and board_color !="p2":
                self.respond("illegal move: \"{}\" wrong color".format(board_color))
                return
            color = self.color_to_int(board_color)
            coord = self.move_to_coord(args[1], self.board.size)
        #     if coord:
        #         move = coord_to_point(coord[0],coord[1], self.board.size)
        #     else:
        #         self.error("Error executing move {} converted from {}"
        #                    .format(move, args[1]))
        #         return
        #     if not self.board.play_move_gomoku(move, color):
        #         self.respond("illegal move: \"{}\" occupied".format(board_move))
        #         return
        #     else:
        #         self.debug_msg("Move: {}\nBoard:\n{}\n".
        #                         format(board_move, self.board2d()))
        #     self.respond()
        # except Exception as e:
        #     self.respond('{}'.format(str(e)))


    def get_input(self):
        line = stdin.readline()
        while line:
            self.get_cmd(line)
            line = stdin.readline()


    def get_cmd(self, command):
        elements = command.split()
        if not elements:
            return
        command_name = elements[0]; args = elements[1:]
        if self.has_arg_error(command_name, len(args)):
            return
        if command_name in self.commands:
            try:
                self.commands[command_name](args)
            except Exception as e:
                self.debug_msg("Error executing command {}\n".format(str(e)))
                raise e
        else:
            self.debug_msg("Unknown command: {}\n".format(command_name))
            self.error('Unknown command')
            stdout.flush()


