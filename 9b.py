from modules.input import read_input

def calculate_history(row_data):
    history_records = []

    history_records.append(row_data.split(" "))
    while len([record for record in history_records[-1] if record != 0]) > 0:
        new_history = []
        old_history = history_records[-1]
        for val in range(0,len(old_history) - 1):
            new_history.append(int(old_history[val + 1]) - int(old_history[val]))
        history_records.append(new_history)
    print(history_records)
    print()
    final_histories = []
    history_records[-1].insert(0,  0)
    for hist in range(len(history_records) - 1, 0, -1):
        cur_hist = history_records[hist]
        parent_hist = history_records[hist - 1]
        parent_hist.insert(0, int(parent_hist[0]) - int(cur_hist[0]))
        final_histories.append(parent_hist[0])
    print(final_histories)
    return(final_histories[-1])
if __name__ == "__main__":
    game_data = read_input(__file__)

    history_values = []
    for row in game_data:
       current_row = row.strip()

       history_values.append(calculate_history(current_row))
    print(sum(history_values))
