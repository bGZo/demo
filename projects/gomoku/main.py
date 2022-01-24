#!/user/bin/env python
# -*- coding:utf-8 -*-
# edited: bGZoCg
# author: wills
# date: 2021-07-23 16:00:00
# from: https://blog.csdn.net/bigzql/article/details/112386871

import pygame

EMPTY = 0
BLACK = 1
WHITE = 2
# 定义三个常量函数，用来表示白棋，黑棋，以及 空
 
black_color = [0, 0, 0]
# 定义黑色（黑棋用，画棋盘）
white_color = [255, 255, 255]
# 定义白色（白棋用）
 
# 定义棋盘这个类
class RenjuBoard(object):
 
    def __init__(self):
        # self._board = board = [[EMPTY] * 15 for _ in range(15)]
        # 将棋盘每一个交叉点都看作列表的一个元素位，一共有15*15共225个元素
        self._board = [[]] * 15
        self.reset()
    #重置棋盘
    
    def reset(self):
        for row in range(len(self._board)):
            self._board[row] = [EMPTY] * 15
    #定义棋盘上的下棋函数，row表示行，col表示列，is_black表示判断当前点位该下黑棋，还是白棋

    def move(self, row, col, is_black):
        if self._board[row][col] == EMPTY:
            self._board[row][col] = BLACK if is_black else WHITE
            return True
        return False
    # 给棋盘定义一个函数将自己在screen上面画出来，使用pygame.draw()函数。并且顺便将下了的棋子也画出来

    def draw(self, screen):
        for h in range(1, 16):
            pygame.draw.line(screen, black_color, 
                             [40, h * 40], [600, h * 40], 1)
            pygame.draw.line(screen, black_color,
                             [h * 40,40], [h * 40, 600], 1)
            # 1. wait... T_T, range(1,3) is 1,2, not include 3 !!!
            # 2. funtion usage in:
            #    www.pygame.org/docs/ref/draw.html#pygame.draw.line
            #    line(surface, color, start_pos, end_pos, width) 
            # 3. first is vertical direction,
            #    second is horizontal direction.

        pygame.draw.rect(screen, black_color, [36, 36, 568, 568], 3)
        # 1. add outline border
        # 2. rect function in 
        #    www.pygame.org/docs/ref/draw.html#pygame.draw.rect
        #    
        #    rect(surface, color, rect, width=0, border_radius=0, 
        #    border_top_left_radius=-1, border_top_right_radius=-1, 
        #    border_bottom_left_radius=-1,
        #    border_bottom_right_radius=-1) 
        #
        #    rect usage in pygame.Rect in 
        #    www.pygame.org/docs/ref/rect.html#pygame.Rect
        #    Rect((left, top), (width, height)) 
        #    so the really the right distance is 568+36=604, is the
        #    same like 4 to 36.
 
        pygame.draw.circle(screen, black_color, [320, 320], 5, 0)
        pygame.draw.circle(screen, black_color, [160, 160], 3, 0)
        pygame.draw.circle(screen, black_color, [160, 480], 3, 0)
        pygame.draw.circle(screen, black_color, [480, 160], 3, 0)
        pygame.draw.circle(screen, black_color, [480, 480], 3, 0)
        # 1. the five special pos
        # 2. circle usage in
        #    www.pygame.org/docs/ref/draw.html#pygame.draw.circle
        #    circle(surface, color, center, radius, width)

        for row in range(len(self._board)):
            for col in range(len(self._board[row])):
                if self._board[row][col] != EMPTY:
                    ccolor = black_color \
                        if self._board[row][col] == BLACK else white_color
                    # get ccolor in pps
                    pos = [40 * (col + 1), 40 * (row + 1)]
                    pygame.draw.circle(screen, ccolor, pos, 18, 0)
        # traverse all coord and use odd or even number get the next
        # color is white or black, maybe this could optimize

def is_win(board):
    for n in range(15):
        # 判断垂直方向胜利
        flag = 0
        # flag是一个标签，表示是否有连续以上五个相同颜色的棋子
        for b in board._board:
            if b[n] == 1:
                flag += 1
                if flag == 5:
                    print('黑棋胜')
                    return False
            else:
            # else表示此时没有连续相同的棋子，标签flag重置为0
                flag = 0
 
        flag = 0
        for b in board._board:
            if b[n] == 2:
                flag += 1
                if flag == 5:
                    print('白棋胜')
                    return False
            else:
                flag = 0
 
        # 判断水平方向胜利
        flag = 0
        for b in board._board[n]:
            if b == 1:
                flag += 1
                if flag == 5:
                    print('黑棋胜')
                    return False
            else:
                flag = 0
 
        flag = 0
        for b in board._board[n]:
            if b == 2:
                flag += 1
                if flag == 5:
                    print('白棋胜')
                    return False
            else:
                flag = 0
 
        # 判断正斜方向胜利
 
        for x in range(4, 25):
            flag = 0
            for i,b in enumerate(board._board):
                if 14 >= x - i >= 0 and b[x - i] == 1:
                    flag += 1
                    if flag == 5:
                        print('黑棋胜')
                        return False
                else:
                    flag = 0
 
        for x in range(4, 25):
            flag = 0
            for i,b in enumerate(board._board):
                if 14 >= x - i >= 0 and b[x - i] == 2:
                    flag += 1
                    if flag == 5:
                        print('白棋胜')
                        return False
                else:
                    flag = 0
 
        #判断反斜方向胜利
        for x in range(11, -11, -1):
            flag = 0
            for i,b in enumerate(board._board):
                if 0 <= x + i <= 14 and b[x + i] == 1:
                    flag += 1
                    if flag == 5:
                        print('黑棋胜')
                        return False
                else:
                    flag = 0
 
        for x in range(11, -11, -1):
            flag = 0
            for i,b in enumerate(board._board):
                if 0 <= x + i <= 14 and b[x + i] == 2:
                    flag += 1
                    if flag == 5:
                        print('白棋胜')
                        return False
                else:
                    flag = 0
 
    return True
# judge function, judge has the winner out and return false. or 
# return true.

 
def main():
    # 创建棋盘对象
    board = RenjuBoard()

    # 用于判断是下黑棋还是白棋
    is_black = True

    # pygame初始化函数，固定写法
    pygame.init()
    pygame.display.set_caption('Gomoku_Demo') # 改标题

    # pygame.display.set_mode() 表示建立个窗口，左上角为坐标原点，往右为x正向，往下为y轴正向
    screen = pygame.display.set_mode((640,640))

    # 给窗口填充颜色，颜色用三原色数字列表表示
    screen.fill([125,95,24])
    board.draw(screen)  # 给棋盘类发命令，调用draw()函数将棋盘画出来
    pygame.display.flip()  # 刷新窗口显示
 
    running = True

    # while 主循环的标签，以便跳出循环
    while running:
        # 遍历建立窗口后发生的所有事件，固定写法
        for event in pygame.event.get():
            # 根据事件的类型，进行判断
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYUP:
                pass

            # pygame.MOUSEBUTTONDOWN表示鼠标的键被按下
            elif event.type == pygame.MOUSEBUTTONDOWN and \
                    event.button == 1:# button表示鼠标左键
                x, y = event.pos  # 拿到鼠标当前在窗口上的位置坐标

                # 将鼠标的(x, y)窗口坐标，转化换为棋盘上的坐标
                row = round((y - 40) / 40)
                col = round((x - 40) / 40)
                if board.move(row, col, is_black):
                    is_black = not is_black
                    screen.fill([125, 95, 24])
                    board.draw(screen)
                    pygame.display.flip()
                    # 调用判断胜负函数
                    if not is_win(board):
                        #break
                        running = False
    pygame.quit()
 
 
 
if __name__ == '__main__':
    main()

# so why using this stmt, more answer in 
# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
#    you can test whether your script is being run directly or 
#    being imported by something else by testing.