from dataset import ecom_sales_novo 
import plotly.express as px 
import plotly.io as pio
pio.renderers.default = "browser"

bar_fig = px.bar( 
    data_frame = ecom_sales_novo, 
    x = 'Total Sales (R$)', 
    y = 'Country', 
    orientation = 'h', 
    title = 'Total Sales by Country' 
) 

bar_fig.update_layout({'bargap': 0.5})  
bar_fig.show() 
