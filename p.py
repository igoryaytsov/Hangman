import random
import time
import turtle

# Настройки окна
delay = 0.1
score = 0
high_score = 0

wn = turtle.Screen()
wn.title("Игра Змейка на Python")
wn.bgcolor("blue")
wn.setup(width=1000, height=1000)
wn.tracer(0)  # Отключение автоматического обновления экрана

# Голова змейки
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("red")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Еда для змейки
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("green")
food.penup()
food.goto(0, 100)

segments = []

# Табло для счета
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(-200, 460)
pen.write("Счет: 0  Рекорд: 0", align="right", font=("serif", 24, "normal"))


# Функции управления
def go_up():
  if head.direction != "down":
    head.direction = "up"


def go_down():
  if head.direction != "up":
    head.direction = "down"


def go_left():
  if head.direction != "right":
    head.direction = "left"


def go_right():
  if head.direction != "left":
    head.direction = "right"


def move():
  if head.direction == "up":
    y = head.ycor()
    head.sety(y + 20)
  if head.direction == "down":
    y = head.ycor()
    head.sety(y - 20)
  if head.direction == "left":
    x = head.xcor()
    head.setx(x - 20)
  if head.direction == "right":
    x = head.xcor()
    head.setx(x + 20)


# Привязка клавиш (управление стрелками)
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# Главный игровой цикл
while True:
  wn.update()

  # Столкновение со стенами
  if (
      head.xcor() > 490
      or head.xcor() < -490
      or head.ycor() > 490
      or head.ycor() < -490
  ):
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"

    # Удаление сегментов хвоста
    for segment in segments:
      segment.goto(1000, 1000)
    segments.clear()

    # Сброс счета
    score = 0
    pen.clear()
    pen.write(
        f"Счет: {score}  Рекорд: {high_score}",
        align="right",
        font=("serif", 24, "normal"),
    )

  # Поедание еды
  if head.distance(food) < 20:
    x = random.randint(-470, 470)
    y = random.randint(-400, 470)
    food.goto(x, y)

    # Добавление нового сегмента тела
    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape("square")
    new_segment.color("purple")
    new_segment.penup()
    segments.append(new_segment)

    # Увеличение счета
    score += 1
    if score > high_score:
      high_score = score

    pen.clear()
    pen.write(
        f"Счет: {score}  Рекорд: {high_score}",
        align="right",
        font=("serif", 24, "normal"),
    )

  # Движение тела змейки
  for i in range(len(segments) - 1, 0, -1):
    x = segments[i - 1].xcor()
    y = segments[i - 1].ycor()
    segments[i].goto(x, y)

  if len(segments) > 0:
    x = head.xcor()
    y = head.ycor()
    segments[0].goto(x, y)

  move()

  # Столкновение с собственным хвостом
  for segment in segments:
    if segment.distance(head) < 20:
      time.sleep(1)
      head.goto(0, 0)
      head.direction = "stop"
      for s in segments:
        s.goto(1000, 1000)
      segments.clear()
      score = 0
      pen.clear()
      pen.write(
          f"Счет: {score}  Рекорд: {high_score}",
          align="right",
          font=("serif", 24, "normal"),
      )

  time.sleep(delay)
