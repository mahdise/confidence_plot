import pandas as pd
import matplotlib.pyplot as plt

from method_static import create_error_bar_data, calculate_confidence_st, separate_data_according_true_false

# Todo create command line and dynamic title


data_frame_delivery_ratio = pd.read_csv("/home/mahdiislam/Mahdi/Riad_/simulation_result/network_200s.csv")


data_frame_true, data_frame_false = separate_data_according_true_false(
    data_frame_for_separate=data_frame_delivery_ratio, drop_null_value=True)

data_frame_true['avg_'] = data_frame_true.iloc[:, 1:].mean(axis=1)
data_frame_false['avg_'] = data_frame_false.iloc[:, 1:].mean(axis=1)

stats_true = data_frame_true.groupby(['true'])['avg_'].agg(['mean', 'count', 'std'])
stats_false = data_frame_false.groupby(['false'])['avg_'].agg(['mean', 'count', 'std'])

stats_true = calculate_confidence_st(data_frame=stats_true, drop_null_values=True)
stats_false = calculate_confidence_st(data_frame=stats_false, drop_null_values=True)

list_of_value_true_as_y = stats_true["mean"]
list_of_key_true_as_x = list(stats_true.index)
interval_true = stats_true["interval"]

y_true_list = create_error_bar_data(list_of_value_true_as_y)
x_true_list = create_error_bar_data(list_of_key_true_as_x)
interval_true_ = create_error_bar_data(interval_true)
custom_interval = [x*10000 for x in interval_true_]

list_of_value_false_as_y = stats_false["mean"]
list_of_key_false_as_x = list(stats_false.index)
interval_false = stats_false["interval"]

y_false_list = create_error_bar_data(list_of_value_false_as_y)
x_false_list = create_error_bar_data(list_of_key_false_as_x)
interval_false_ = create_error_bar_data(interval_false)
custom_interval_false= [x*10000 for x in interval_false_]
# plotting the line 1 points
plt.plot(list_of_key_true_as_x, list_of_value_true_as_y, label="Broadcast Epidemic", color="green")

plt.plot(list_of_key_false_as_x, list_of_value_false_as_y, label="Unicast Epidemic", color="red")

plt.errorbar(
    x_true_list,
    y_true_list,
    yerr=custom_interval,
    linestyle='',
    ecolor="green"
)

plt.errorbar(
    x_false_list,
    y_false_list,
    yerr=custom_interval_false,
    linestyle='',
    ecolor="red"
)

plt.xlabel('simulation time')
# Set the y axis label of the current axis.
plt.ylabel('network overhead in bytes')
# Set a title of the current axes.

plt.title("Network overhead comparison between broadast and unicast epidemic for ")
# show a legend on the plot
plt.legend()
# Display a figure.
plt.show()
