# Gomoku_Demo

发现一个有意思的写法, 可能是 Python 的语法糖? 在别的地方不曾见过.

```python
a = 2

if a != 0: 
    color= 1 if(a == 1)  else 2

print(color)

# if self._board[row][col] != EMPTY:
#    ccolor = black_color \
#        if self._board[row][col] == BLACK else white_color
```