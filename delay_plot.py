from method_static import create_error_bar_data, calculate_confidence_st, separate_data_according_true_false
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Todo create command line and dynamic title


data_frame_delivery_ratio = pd.read_csv("/home/mahdiislam/Mahdi/Riad_/simulation_result/delay_600s.csv")

true_data_frame = pd.DataFrame()
false_data_frame = pd.DataFrame()

true_value_list = list()
false_value_list = list()
for i in data_frame_delivery_ratio.index:
    run, repe, module_, value = data_frame_delivery_ratio.loc[i]
    num_of_swim = run.split('-')[3:4][0]
    if int(num_of_swim) < 20:
        true_value_list.append(value)

    if int(num_of_swim) > 19:
        false_value_list.append(value)

true_data_frame["true_value"] = true_value_list
false_data_frame["false_value"] = false_value_list

true_mean = np.mean(true_value_list)
false_mean = np.mean(false_value_list)

# Calculate the standard deviation
true_std = np.std(true_value_list)
false_std = np.std(false_value_list)

# calculate interval for true

interval_true = 1.95 * true_std
true_high = true_mean + interval_true
true_low = true_mean - interval_true

# calculate interval for true

interval_false = 1.95 * false_std
false_high = false_mean + interval_false
false_low = false_mean - interval_false

labels = ["broadcast epidemic", "unicast epidemic"]
x_pos = np.arange(len(labels))
CTEs = [true_mean, false_mean]
error = [true_std, false_std]
fig, ax = plt.subplots()
ax.bar(x_pos, CTEs,
       yerr=error,
       align='center',
       alpha=0.5,
       ecolor='black',
       capsize=10,
       color=["green", "red"])

ax.set_ylabel('average delay')
ax.set_xticks(x_pos)
ax.set_xticklabels(labels)
ax.set_title('Average delay comparison between broadcast and unicast epidemic')
ax.yaxis.grid(True)

# Save the figure and show
plt.tight_layout()
# plt.savefig('bar_plot_with_error_bars.png')
plt.show()
