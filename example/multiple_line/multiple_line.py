from nyanplot import read_file,plot,aggregate
file = r"data3.xlsx"
data ,sheetn= read_file(file)
data1 ,std_y = aggregate(data,3)
plot(data1,graph_title = "電流$I$と力$F$の関係",x_label = '電流$I$[A]',y_label = '力$F$[mN]',errorbar = True,std_y = std_y)