# labchart_label_column
This is a script that allows ADInstruments LabChart PoweLab users to export their raw data for statistical analyses and populate the label column with values for each data point between label markers. 
This is a somewhat important missing feature for those that want to perform statistical analyses between different experimental cues/stimuli within the same recording session and utilise the marker feature in LabChart.
This script allows you to populate all discrete data records with the marker text.

Ensure that you re using Python 3.x or higher

Ensure that your raw data text file does not have empty lines at the bottom

This script requires 2 modules: 're' (regular expressions) and 'datetime'

I have coded this for efficient memory usage as loading the complete raw file as a dataframe onto memory (e.g. using pandas) is going to make processing terribly inefficient, and often jeopardize the integrity of the raw data (pandas known rounding issues, and data type conflict alerts).

Happy analyzing!

Evangelos
