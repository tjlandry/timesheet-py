import datetime
from datetime import datetime
from datetime import timedelta
from tkinter import *
from tkinter import messagebox


def tick_loop():
    def tick_time():
        now = datetime.now()
        cur_date = now.strftime('%B %d, %Y')
        cur_time = now.strftime('%I:%M:%S%p')
        cur_day = now.strftime('%A')
        now_lbl.configure(text='It is currently {} on {}, {}.'.format(cur_time, cur_day, cur_date))
        now_lbl.after(1000, tick_time)
        clock_lbl.configure(text='Clock In/Out Time: {}'.format(cur_time_round()))
        clock_lbl.after(10000, tick_time)
    tick_time()


def cur_time_round():
    dt = datetime.now()
    round_to = 900
    seconds = (dt - dt.min).seconds
    rounding = (seconds+round_to/2) // round_to * round_to
    rounded_time = dt + timedelta(0, rounding-seconds, -dt.microsecond)
    formatted_rounded_time = rounded_time.strftime('%I:%M%p')
    return formatted_rounded_time


def clock_in():
    answer_in = messagebox.askyesno('Confirm Action', 'Do you want to clock in at {}?'.format(cur_time_round()))
    if answer_in is True:
        print('yeah lemme clock in')


def clock_out():
    answer_out = messagebox.askyesno('Confirm Action', 'Do you want to clock out at {}?'.format(cur_time_round()))
    if answer_out is True:
        print('yeah lemme clock out')


window = Tk()


window.geometry('300x120')
window.title('Timesheet')

frame = Frame(window)
frame.pack()

lf1 = LabelFrame(frame)
lf1.pack(side=TOP, fill=X)

now_lbl = Label(frame)
now_lbl.pack(side=TOP, fill=X)

lf2 = LabelFrame(frame)
lf2.pack(side=TOP, fill=X)

clock_lbl = Label(frame)
clock_lbl.pack(side=TOP, fill=X)

lf3 = LabelFrame(frame)
lf3.pack(side=TOP, fill=X)

clock_out_button = Button(frame, text='Clock Out', command=clock_out, justify=CENTER)
clock_in_button = Button(frame, text='Clock In', command=clock_in, justify=CENTER)

clock_in_button.pack()
clock_out_button.pack()

tick_loop()


window.mainloop()
