# quiz-score-histogram.py
# 점수의 빈도를 히스토그램으로 나타내는 프로그램
from graphics import *
import time
import random


def is_score(list_data):
    # 데이터 리스트 요소의 개수와 데이터 리스트에서 0 ~ 10 숫자를 센 개수가 일치하면 점수 데이터라고 판단한다.
    if len(list_data) == len(list(filter(lambda score: int(score)
                             in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], list_data))):
        return True
    else:
        return False


def main():
    # 메인 화면 인터페이스
    main_message = Text(Point(200, 380), "")
    main_message.setSize(12)
    inputbox = Entry(Point(200, 350), 20)
    inputbox.setFill("Snow")
    inputbox.setSize(10)
    inputbox.setStyle("bold")
    inputbox.setTextColor("Gray")
    help_message = Text(Point(200, 200), """
    메모장에 점수를 한 줄에 하나씩 입력하세요.\n\n▼\n
    텍스트 파일을 이 프로그램과 같은 위치에 저장하세요.\n\n▼\n
    텍스트 파일 이름을 예시와 같은 형식으로 입력하세요.\n\n▼\n
    실행 버튼을 누르면 히스토그램 자동으로 생성됩니다.\n\n▼\n
    종료 버튼을 누르면 프로그램이 종료됩니다.
    """)
    help_message.setFill("Orange")
    help_message.setSize(8)
    button_execute = Rectangle(Point(50, 10), Point(190, 50))
    button_execute.setFill("Light Gray")
    button_execute.setOutline("Gray")
    button_execute.setWidth(3)
    button_quit = Rectangle(Point(210, 10), Point(350, 50))
    button_quit.setFill("Light Gray")
    button_quit.setOutline("Gray")
    button_quit.setWidth(3)
    text_execute = Text(Point(120, 30), "실  행")
    text_quit = Text(Point(280, 30), "종  료")
    line = Line(Point(400, -10), Point(400, 400))
    line.setFill("Sky Blue")
    line.setWidth(5)
    histogram_message = Text(Point(600, 200), "HISTOGRAM")
    histogram_message.setFill("Light Gray")
    histogram_message.setSize(20)

    # 그래픽 창 만들기
    win = GraphWin("Quiz Score Histogram", 800, 400)

    try:
        # 로딩 화면 그리기
        win.setBackground("Black")
        loading = Text(Point(400, 190), "LOADING")
        loading.setFill("White")
        loading.setSize(20)
        loading.draw(win)

        # 로딩 박스 그리기
        list_loadingbox = []
        for i in range(0, 9):
            list_loadingbox.append(Text(Point(340 + i * 15, 210), "□"))
            list_loadingbox[-1].setFill("White")
            list_loadingbox[-1].setSize(20)
            list_loadingbox[-1].draw(win)

        # 로딩 박스 채우기
        for i in range(0, 9):
            time.sleep(random.random() / 3)  # 프로그램을 실행할 때마다 로딩 시간 무작위로 설정
            list_loadingbox[i].setText("■")
        time.sleep(0.5)

        # 로딩 화면 지우기
        for i in range(0, 9):
            list_loadingbox[i].undraw()
        loading.undraw()

        while True:
            # 메인 화면 그리기
            win.setCoords(0, 0, 800, 400)
            win.setBackground("Alice Blue")
            main_message.setText("파일 이름을 입력하고 실행하세요.")
            main_message.setFill("Black")
            inputbox.setText("ex: filename.txt")
            line.draw(win)
            main_message.draw(win)
            inputbox.draw(win)
            help_message.draw(win)
            button_execute.draw(win)
            button_quit.draw(win)
            text_execute.draw(win)
            text_quit.draw(win)
            histogram_message.draw(win)

            while True:
                p = win.getMouse()
                # 실행 버튼 클릭하면 프로그램 실행
                if 50 < p.getX() < 190 and 10 < p.getY() < 50:
                    pass
                # 종료 버튼 클릭하면 프로그램 종료
                elif 210 < p.getX() < 350 and 10 < p.getY() < 50:
                    button_quit.setFill("Gray")
                    time.sleep(0.1)
                    button_quit.setFill("Light Gray")
                    time.sleep(0.1)
                    win.close()
                else:
                    continue

                try:
                    # 파일 이름 입력(단, 양쪽 공백과 대소문자 무시)
                    filename = inputbox.getText().strip().lower()

                    # 파일 이름이 처음 값 그대로이면 "파일 이름을 입력하고 실행하세요."
                    if filename == "ex: filename.txt":
                        main_message.setText("")
                        main_message.setTextColor("Black")
                        time.sleep(0.1)
                        main_message.setText("파일 이름을 입력하고 실행하세요.")
                        continue

                    # 파일 데이터 읽기
                    file = open(filename, "r")
                    data = file.read()
                    list_score = data.split("\n")  # 점수 리스트는 엔터를 기준으로 데이터를 나눈 것
                    file.close()

                    # 점수가 아니면 "점수는 0부터 10까지만 입력해야 합니다."
                    if not is_score(list_score):
                        main_message.setText("")
                        main_message.setFill("Tomato")
                        time.sleep(0.1)
                        main_message.setText("점수는 0부터 10까지만 입력해야 합니다.")
                        continue

                # 데이터에 숫자 외에 다른 값이 있으면 "파일에는 숫자를 입력해야 합니다."
                except ValueError:
                    main_message.setText("")
                    main_message.setFill("Tomato")
                    time.sleep(0.1)
                    main_message.setText("파일에는 숫자를 입력해야 합니다.")
                    continue

                # 파일이 존재하지 않으면 "파일을 찾을 수 없습니다."
                except:
                    main_message.setText("")
                    main_message.setFill("Tomato")
                    time.sleep(0.1)
                    main_message.setText("파일을 찾을 수 없습니다.")
                    continue

                break

            # 인터페이스 지우기
            main_message.undraw()
            inputbox.undraw()
            help_message.undraw()
            button_execute.undraw()
            button_quit.undraw()
            text_execute.undraw()
            text_quit.undraw()
            histogram_message.undraw()

            # 성적 리스트 ex) grade[4]는 4점을 받은 학생 수를 의미한다.
            grade = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

            # 점수 빈도를 센 다음 성적 리스트에 넣기
            for num in range(0, 11):
                grade[num] = list_score.count(str(num))

            # 빈도수 최댓값을 올림해서 y축 최댓값 정하기
            max_y10 = divmod(max(grade) + 9, 10)[0] * 10  # ex) 44 → 50, 77 → 80
            max_y20 = divmod(max(grade) + 19, 20)[0] * 20  # ex) 144 → 160, 177 → 180
            max_y50 = divmod(max(grade) + 49, 50)[0] * 50  # ex) 244 → 250, 277 → 300

            # 빈도수 최댓값에 따라 그래픽 창 세로 좌표 바꾸기
            if max(grade) <= 20:
                height_win = 400
            elif max(grade) <= 100:
                height_win = max_y10 * 18 * 10 / 9
            elif max(grade) <= 260:
                height_win = max_y20 * 18 * 10 / 9
            else:
                height_win = max_y50 * 18 * 10 / 9

            x_score = []  # x축(점수)
            y_frequency = []  # y축(빈도)
            bar_list = []  # 막대그래프
            value_list = []  # 빈도수

            # 좌표 재설정
            win.setCoords(0, 0, 800, height_win)

            # 선 새로 그리기
            line.undraw()
            line = Line(Point(400, -10), Point(400, height_win))
            line.setFill("Sky Blue")
            line.setWidth(5)
            line.draw(win)

            # x축, y축 단위 표시
            x_axis = Text(Point(790, height_win * 10 / 400), "(점)")
            x_axis.setSize(7)
            y_axis = Text(Point(420, height_win * 380 / 400), "(명)")
            y_axis.setSize(7)
            x_axis.draw(win)
            y_axis.draw(win)

            # x축(점수) 표시
            for x in range(0, 11):
                x_score.append(Text(Point(470 + x * 30, height_win * 10 / 400), x))
                x_score[-1].setSize(8)
                x_score[-1].draw(win)

            # y축(빈도) 표시
            if max(grade) <= 20:
                for y in range(0, 21):
                    y_frequency.append(Text(Point(440, height_win * 20 / 400 + y * 18), y))
                    y_frequency[-1].setSize(8)
                    y_frequency[-1].draw(win)
            elif max(grade) <= 50:
                for y in range(0, max_y10 + 1, 5):
                    y_frequency.append(Text(Point(440, height_win * 20 / 400 + y * 18), y))
                    y_frequency[-1].setSize(8)
                    y_frequency[-1].draw(win)
            elif max(grade) <= 100:
                for y in range(0, max_y10 + 1, 10):
                    y_frequency.append(Text(Point(440, height_win * 20 / 400 + y * 18), y))
                    y_frequency[-1].setSize(8)
                    y_frequency[-1].draw(win)
            elif max(grade) <= 260:
                for y in range(0, max_y20 + 1, 20):
                    y_frequency.append(Text(Point(440, height_win * 20 / 400 + y * 18), y))
                    y_frequency[-1].setSize(8)
                    y_frequency[-1].draw(win)
            else:
                for y in range(0, max_y50 + 1, 50):
                    y_frequency.append(Text(Point(440, height_win * 20 / 400 + y * 18), y))
                    y_frequency[-1].setSize(8)
                    y_frequency[-1].draw(win)

            # 막대그래프 그리기(막대그래프를 빈도수보다 먼저 그려야 막대그래프가 빈도수를 가리지 않음)
            for bar in range(0, 11):
                if grade[bar] == 0:
                    continue
                else:
                    bar_list.append(Rectangle(Point(460 + bar * 30, height_win * 20 / 400),
                                              Point(480 + bar * 30, height_win * 20 / 400 + grade[bar] * 18)))
                    bar_list[-1].setFill("Light Salmon")
                    bar_list[-1].setWidth(0)
                    bar_list[-1].draw(win)

            # 빈도수 표시(막대그래프가 너무 작으면 값을 표시해도 보이지 않음)
            for value in range(0, 11):
                if 0 <= max(grade) <= 40 and grade[value] == 0:
                    continue
                elif 40 < max(grade) <= 80 and grade[value] <= 1:
                    continue
                elif 80 < max(grade) <= 140 and grade[value] <= 2:
                    continue
                elif 140 < max(grade) <= 200 and grade[value] <= 4:
                    continue
                elif 200 < max(grade) <= 260 and grade[value] <= 6:
                    continue
                elif max(grade) > 260 and grade[value] <= 12:
                    continue
                value_list.append(Text(Point(470 + value * 30, height_win * 14 / 400
                                             + grade[value] * 18), grade[value]))
                value_list[-1].setSize(8)
                value_list[-1].setFill("White Smoke")
                value_list[-1].draw(win)

            # 클릭 메시지 표시
            click_message = Text(Point(200, height_win * 200 / 400), "CLICK")
            click_message.setSize(20)
            click_message.setFill("Light Gray")
            click_message.draw(win)

            # 파일 이름과 점수별 학생 수 출력
            print("<%s>  전체학생수: %s명 / " % (filename, len(list_score)), end="")
            for score, frequency in enumerate(grade):
                if score == 10:
                    print("%s점: %s명" % (score, frequency), end="\n")
                    break
                else:
                    print("%s점: %s명" % (score, frequency), end=" / ")
            print("-" * 180)

            while True:
                # 히스토그램 지우기
                if win.checkMouse():
                    for x in range(0, len(x_score)):
                        x_score[0].undraw()
                        del x_score[0]
                    for y in range(0, len(y_frequency)):
                        y_frequency[0].undraw()
                        del y_frequency[0]
                    for bar in bar_list:
                        bar.undraw()
                    for value in range(0, len(value_list)):
                        value_list[0].undraw()
                        del value_list[0]
                    x_axis.undraw()
                    y_axis.undraw()
                    line.undraw()
                    click_message.undraw()
                    break

                # 클릭 메시지 깜빡깜빡
                else:
                    time.sleep(0.5)
                    click_message.setText("")
                    time.sleep(0.5)
                    click_message.setText("CLICK")

            continue

    # X 버튼을 클릭하면 프로그램 종료
    except GraphicsError:
        print("프로그램이 종료되었습니다.")


main()
