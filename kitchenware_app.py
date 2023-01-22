import streamlit as st
from PIL import Image
from src.request_sender import streamlit_request


st.set_page_config(layout="wide")
st.title("Kitchenware Classifier")
st.subheader("The problem we will study was introduced by [DataTalksCLub](https://datatalks.club/)"
             " in Kaggle platform [Kaggle Competition](https://www.kaggle.com/competitions/kitchenware-classification/)."
             " You can find the repository here: https://github.com/Kibzik/kitchenware-classification_cv/.")
st.write("#")
st.write("#")

c2, c4 = st.columns(2)

imageList = {
    "Cup": ["0000", "0008", "0015", "2744", "3242", "3247", "8170"],
    "Glass": ["0022", "1239", "3168", "2103", "5788", "7522", "9374"],
    "Plate": ["0019", "0967", "2724", "3135", "4673", "7263", "9168"],
    "Spoon": ["0190", "0848", "1739", "3049", "4366", "6106", "9085"],
    "Fork": ["0136", "1206", "2113", "3833", "5565", "7261", "9271"],
    "Knife": ["0018", "0510", "1742", "2721", "3277", "4770", "8204"],
}

add_selectbox1 = st.sidebar.selectbox(
    "Choose Category?",
    ("Cup", "Glass", "Plate", "Spoon", "Fork", "Knife"),
)

add_selectbox2 = st.sidebar.selectbox(
    "Choose Image?",
    (imageList[add_selectbox1]),
)

img_name = add_selectbox2 + ".jpg"
image = Image.open(f"data/images/{img_name}")
factor = 0.4
x, y = image.size
x, y = int(factor * x), int(factor * y)
image = image.resize((x, y))

label2pred_value = streamlit_request("data/images/" + img_name)

with c2:
    st.write("\n")
    st.write("\n")
    st.image(image, caption=f"This should be a {add_selectbox1}")

with c4:
    st.write("\n\n")
    max_label = max(label2pred_value, key=label2pred_value.get)
    st.header(f"Model tells that it is a :blue[{max_label.upper()}]")
