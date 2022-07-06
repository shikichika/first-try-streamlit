import streamlit as st
import time

st.title('First Streamlit')


st.write('Display Image')

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i +1 }')
    bar.progress(i + 1)
    time.sleep(0.1)


option = st.sidebar.text_input("What do you do in your free time")

condition = st.sidebar.slider('your condition', 0, 100, 50)
"your condition is ", condition

left_column, right_column = st.columns(2)

button = left_column.button('Show right items')

if button:
    right_column.write("Right")


expander = st.expander('reference')
expander.write('Query')


#selectbox
# option = st.selectbox(
#     "what color do u like?",
#     list(range(1, 11))

# )

"Your favorit color is ", option



# if st.checkbox('Show img'):
#     img = Image.open('images/pike.jpeg')
#     img_rotate = img.rotate(270)
#     st.image(img_rotate, caption = 'Pike chan')






# df = pd.DataFrame(
#   np.random.rand(100,2)/[50, 50]+[35.69, 139.70],
#    columns=['lat', 'lon']

# )

# st.map(df)





# df = pd.DataFrame(
#     np.random.rand(20,3),
#     columns=['a', 'b', 'c']
   
# )

# #line chart
# st.line_chart(df)

# #line areachart
# st.area_chart(df)

# #bar chart
# st.bar_chart(df)

#data frame
# st.dataframe(df.style.highlight_max(axis=0))

# #mark down 

# """
# #h1
# ##h2
# ###h3

# ``` python
# import streamlit as st
# import pandas as pd
# import numpy as np
# ```


# """