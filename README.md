<!--
 * @Date: 2023-05-10 14:35:55
 * @Author: Bruce
 * @Description: 
-->
# 🦜️🔗 LangChain + <img src="https://user-images.githubusercontent.com/7164864/217935870-c0bc60a3-6fc0-4047-b011-7b4c59488c91.png" alt="Streamlit logo"></img>

## **Quick Start**

```
pip install -r requirements.txt

streamlit run main.py
```

## 📖 Documentation:

Please see [langchain](https://langchain.readthedocs.io/) for full documentation on :

- Getting started (installation, setting up the environment, simple examples)
- How to examples(demos, integrations, helper functions)
- Reference(full API docs)
- Resources(high-level explanation of core concepts)

Please see [streamlit](https://docs.streamlit.io/library/get-started) for full documentation on :

- Getting started
- Understand how that all works

## 👀 Results Show:

<img src="./images/langchain.png">

## 🚀 How to use streamlit

Create a new file `app.py` with the following code:

```python
import streamlit as st
x = st.slider("Select a value")
st.write(x, "squared is ", x * x)
```

Now run it to open the app!

```
$ streamlit run app.py
```

<img src="https://user-images.githubusercontent.com/7164864/215172915-cf087c56-e7ae-449a-83a4-b5fa0328d954.gif" width=300 alt="Little example" style="margin-left:20%"></img>
