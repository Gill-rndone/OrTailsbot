import random
import datetime as dt


# class for each flip (returns result and time stamp for easy database insert)
class coin:
    def __init__(self, result, timestamp):
        self.result = result
        self.timestamp = timestamp


def flip():
    # flip coin
    face = random.choice(["Heads!", "Tails!"])
    # create flip time stamp
    timestamp = dt.datetime.now().strftime("%d/%m/%y | %H:%M:%S")
    post_flip = coin(face, timestamp)
    return post_flip


# gets the average from flips
def average(history):
    h_amount = 0

    # Tally the amount of heads flips
    for x, i in enumerate(history):
        if i[0] == "Heads!":
            h_amount += 1

    flip_amount = len(history)
    if flip_amount == 0:
        results = [0, 0]
        return results

    # Calculates and returns the percentages of results
    if h_amount != 0:
        h_percent = h_amount / flip_amount
        h_percent = h_percent * 100
        t_percent = 100 - h_percent
        results = [round(h_percent, 2), round(t_percent, 2)]
        return results
    else:
        results = [0, 100]
        return results


def return_five(history, is_global):
    # formats the header of the message
    output = "Last 5 flips!\n==============================\n"
    # creates a string which stores the data from each row and adds it to the output string variable
    for x, i in enumerate(history[:5]):
        row = f"| {x + 1} | {i[0]} | {i[2]} | {i[1]} | \n"
        output = output + row

    # includes percentage data from average() function
    f_percent = average(history)
    if not is_global:
        percent_row = f"==============================\n\nServer Total Flip Percentages! (for {len(history)} flips)\n==============================\n| Heads!: {f_percent[0]}% | Tails!: {f_percent[1]}% |\n==============================\n"
    else:
        percent_row = f"==============================\n\nGlobal Total Flip Percentages! (for {len(history)} flips)\n==============================\n| Heads!: {f_percent[0]}% | Tails!: {f_percent[1]}% |\n==============================\n"
    output = output + percent_row
    return output
