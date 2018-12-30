import turtle
import time


# 根据半径，角度，长度，掉头半径画蛇
def draw_snake(rad, angle, len, turn_round_rad):
    for _ in range(len):
        turtle.circle(rad, angle)  # 根据半径和角度画圆
        turtle.circle(-rad, angle)
    turtle.circle(rad, angle / 2)
    turtle.forward(rad / 2)  # 直线前进
    turtle.circle(turn_round_rad, 180)  # 掉头的半径和角度
    turtle.forward(rad)  # 向当前画笔方向移动distance像素长
    turtle.done()

if __name__ == "__main__":
    turtle.setup(width=0.9, height=0.9)  # 画布大小
    turtle.pensize(30)  # 画笔尺寸
    turtle.pencolor("green")  # 画笔颜色
    time.sleep(10)
    turtle.seth(-40)  # 前进的方向，水平向右
    draw_snake(70, 80, 2, 150)
