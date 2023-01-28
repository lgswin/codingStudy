import tkinter as tk
from datetime import datetime, timedelta

images = ["assets/11.png", "assets/12.png", "assets/13.png", "assets/14.png", "assets/15.png", "assets/16.png",
          "assets/17.png", "assets/18.png", "assets/19.png", "assets/20.png" \
    , "assets/21.png", "assets/22.png", "assets/23.png", "assets/24.png", "assets/25.png", "assets/26.png",
          "assets/27.png", "assets/28.png", "assets/29.png", "assets/30.png"]

words = ("고린도전서 10:13 KRV\n\n사람이 감당할 시험 밖에는 너희에게 당한 것이 없나니 오직 하나님은 미쁘사 너희가 감당치 못할 시험 당함을 허락지 아니하시고 시험 당할 즈음에 또한 피할 길을 내사 너희로 능히 감당하게 하시느니라"\
,"시편 19:14 KRV\n\n나의 반석이시요 나의 구속자이신 여호와여 내 입의 말과 마음의 묵상이 주의 앞에 열납되기를 원하나이다"\
,"역대상 29:11 KRV\n\n여호와여 광대하심과 권능과 영광과 이김과 위엄이 다 주께 속하였사오니 천지에 있는 것이 다 주의 것이로소이다 여호와여 주권도 주께 속하였사오니 주는 높으사 만유의 머리심이니이다"\
,"로마서 5:1 KRV\n\n그러므로 우리가 믿음으로 의롭다 하심을 얻었은즉 우리 주 예수 그리스도로 말미암아 하나님으로 더불어 화평을 누리자"\
,"마태복음 16:24 KRV\n\n이에 예수께서 제자들에게 이르시되 아무든지 나를 따라 오려거든 자기를 부인하고 자기 십자가를 지고 나를 좇을 것이니라"\
,"잠언 16:9 KRV\n\n사람이 마음으로 자기의 길을 계획할지라도 그 걸음을 인도하는 자는 여호와시니라"\
,"고린도전서 10:13 KRV\n\n사람이 감당할 시험 밖에는 너희에게 당한 것이 없나니 오직 하나님은 미쁘사 너희가 감당치 못할 시험 당함을 허락지 아니하시고 시험 당할 즈음에 또한 피할 길을 내사 너희로 능히 감당하게 하시느니라"\
,"시편 19:14 KRV\n\n나의 반석이시요 나의 구속자이신 여호와여 내 입의 말과 마음의 묵상이 주의 앞에 열납되기를 원하나이다"\
,"역대상 29:11 KRV\n\n여호와여 광대하심과 권능과 영광과 이김과 위엄이 다 주께 속하였사오니 천지에 있는 것이 다 주의 것이로소이다 여호와여 주권도 주께 속하였사오니 주는 높으사 만유의 머리심이니이다"\
,"로마서 5:1 KRV\n\n그러므로 우리가 믿음으로 의롭다 하심을 얻었은즉 우리 주 예수 그리스도로 말미암아 하나님으로 더불어 화평을 누리자"\
,"고린도전서 10:13 KRV\n\n사람이 감당할 시험 밖에는 너희에게 당한 것이 없나니 오직 하나님은 미쁘사 너희가 감당치 못할 시험 당함을 허락지 아니하시고 시험 당할 즈음에 또한 피할 길을 내사 너희로 능히 감당하게 하시느니라"\
,"시편 19:14 KRV\n\n나의 반석이시요 나의 구속자이신 여호와여 내 입의 말과 마음의 묵상이 주의 앞에 열납되기를 원하나이다"\
,"역대상 29:11 KRV\n\n여호와여 광대하심과 권능과 영광과 이김과 위엄이 다 주께 속하였사오니 천지에 있는 것이 다 주의 것이로소이다 여호와여 주권도 주께 속하였사오니 주는 높으사 만유의 머리심이니이다"\
,"로마서 5:1 KRV\n\n그러므로 우리가 믿음으로 의롭다 하심을 얻었은즉 우리 주 예수 그리스도로 말미암아 하나님으로 더불어 화평을 누리자"\
,"마태복음 16:24 KRV\n\n이에 예수께서 제자들에게 이르시되 아무든지 나를 따라 오려거든 자기를 부인하고 자기 십자가를 지고 나를 좇을 것이니라"\
,"잠언 16:9 KRV\n\n사람이 마음으로 자기의 길을 계획할지라도 그 걸음을 인도하는 자는 여호와시니라"\
,"고린도전서 10:13 KRV\n\n사람이 감당할 시험 밖에는 너희에게 당한 것이 없나니 오직 하나님은 미쁘사 너희가 감당치 못할 시험 당함을 허락지 아니하시고 시험 당할 즈음에 또한 피할 길을 내사 너희로 능히 감당하게 하시느니라"\
,"시편 19:14 KRV\n\n나의 반석이시요 나의 구속자이신 여호와여 내 입의 말과 마음의 묵상이 주의 앞에 열납되기를 원하나이다"\
,"역대상 29:11 KRV\n\n여호와여 광대하심과 권능과 영광과 이김과 위엄이 다 주께 속하였사오니 천지에 있는 것이 다 주의 것이로소이다 여호와여 주권도 주께 속하였사오니 주는 높으사 만유의 머리심이니이다"\
,"로마서 5:1 KRV\n\n그러므로 우리가 믿음으로 의롭다 하심을 얻었은즉 우리 주 예수 그리스도로 말미암아 하나님으로 더불어 화평을 누리자")


class TodaysWord():

    def __init__(self, window):
        self.lines = None
        self.data = None

        self.selected_date = datetime.now()

        self.date = str(self.selected_date.year) + "-" + str(self.selected_date.month) + "-" + str(
            self.selected_date.day)
        self.label_time = tk.Label(window, text=self.date, width=30, height=2, fg="black")
        self.label_time.pack(side="top")

        self.lpt = tk.PhotoImage(file="leftarrow.png")
        self.button_left = tk.Button(window, image=self.lpt, bd=0, command=self.on_left_btn_click)
        self.button_left.pack(side="left", fill='y')

        self.rpt = tk.PhotoImage(file="rightarrow.png")
        self.button_right = tk.Button(window, image=self.rpt, bd=0, command=self.on_right_btn_click)
        self.button_right.pack(side="right", fill='y')

        self.image_idx = 0
        self.img = tk.PhotoImage(file=images[self.image_idx])

        self.label_center = tk.Label(window, image=self.img)
        self.label_center.pack(side='top', fill='both')

        self.bpt = tk.PhotoImage(file="label_background.png")
        self.label_bottom_content = tk.Label(window, text=words[0], anchor="nw", justify="left", width=20, height=120, padx=30, wraplength=760, compound="center")
        self.label_bottom_content.pack(fill='both')

        self.label_bottom_content = tk.Label(window, background="yellow", anchor="nw", justify="left", width=10, height=10)
        self.label_bottom_content.pack(fill='both')

    def fileopen(self, index):
        self.lines = [10, 100]
        self.data = []

        with open('words.txt', 'r', encoding='utf-8') as self.f:
            self.data = self.f.readlines()[index:index + 2]
        print(self.data[index], end="")
        print(self.data[index + 1])

    def on_left_btn_click(self):
        self.img = tk.PhotoImage(file=images[self.image_idx])
        self.label_center.configure(image=self.img)

        self.image_idx += 1
        if self.image_idx > 19:
            self.image_idx = 0

        self.selected_date = self.selected_date - timedelta(days=1)
        self.date = str(self.selected_date.year) + "-" + str(self.selected_date.month) + "-" + str(
            self.selected_date.day)
        self.label_time.configure(text=self.date)

    def on_right_btn_click(self):
        self.img = tk.PhotoImage(file=images[self.image_idx])
        self.label_center.configure(image=self.img)

        self.image_idx -= 1
        if self.image_idx < 0:
            self.image_idx = 19

        self.selected_date = self.selected_date + timedelta(days=1)
        self.date = str(self.selected_date.year) + "-" + str(self.selected_date.month) + "-" + str(
            self.selected_date.day)
        self.label_time.configure(text=self.date)


window = tk.Tk()
window.title("Today's word")
window.geometry("1000x600+100+100")
window.resizable(False, False)

TodaysWord(window)
window.mainloop()
