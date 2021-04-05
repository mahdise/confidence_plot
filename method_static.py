import math
import pandas as pd


def create_error_bar_data(list_of_data):
    num_taken = 0
    result = list()
    list_of_data = list(list_of_data)
    for index, value in enumerate(list_of_data):
        if index == num_taken:
            result.append(value)

            num_taken += 60

    return result


def separate_data_according_true_false(data_frame_for_separate, drop_null_value=True):
    if drop_null_value:
        data_frame_for_separate = data_frame_for_separate.dropna()

    num = 0
    data_frame_true = pd.DataFrame()
    data_frame_false = pd.DataFrame()
    time_column = True
    time_column_false = True
    num_true_value = 1
    num_false_value = 1

    for col in data_frame_for_separate.columns:
        if "true" in col:
            value_col = num + 1

            if time_column:
                data_frame_true["true"] = data_frame_for_separate[col]
            data_frame_true[str(num_true_value)] = data_frame_for_separate.iloc[:, [value_col]]

            time_column = False

            num_true_value += 1

        if "false" in col:
            value_col = num + 1

            if time_column_false:
                data_frame_false["false"] = data_frame_for_separate[col]
            data_frame_false[str(num_false_value)] = data_frame_for_separate.iloc[:, [value_col]]

            time_column_false = False

            num_false_value += 1

        num += 1

    return data_frame_true, data_frame_false


def calculate_confidence_st(data_frame, drop_null_values=True):
    ci95_hi_true = list()
    ci95_lo_true = list()
    interval_list_true = list()
    for i in data_frame.index:
        m, c, s = data_frame.loc[i]
        interval = 1.95 * s / math.sqrt(c)
        ci95_hi_true.append(m + 1.95 * s / math.sqrt(c))
        ci95_lo_true.append(m - 1.95 * s / math.sqrt(c))
        interval_list_true.append(interval)

    data_frame['ci95_hi'] = ci95_hi_true
    data_frame['ci95_lo'] = ci95_lo_true
    data_frame['interval'] = interval_list_true

    if drop_null_values:
        data_frame = data_frame.dropna()

    return data_frame
