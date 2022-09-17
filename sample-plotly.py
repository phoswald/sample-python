
import plotly.express as px

fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2])
fig.write_html('figure-1.html', auto_open=True)
fig.write_image('figure-1.png')
