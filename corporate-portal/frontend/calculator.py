import streamlit as st

from apps.calculator.app import *
# Можно добавить этот банк стратегий в калькулятор
mapper = {
    "Сложение": summa,
    "Вычитание": minus,
    "Умножение": mul,
    "Деление": div,
    "Процент": percent
}

st.write("# Калькулятор")
choice = st.selectbox("Выберите операцию:", ["Сложение", "Вычитание", "Умножение", "Деление", "Процент"])
a = st.number_input("Первое число:", value=0)
b = st.number_input("Второе число:", value=0)
result = None
# st.write("Результат:", mapper[choice](a, b))
st.metric(label="Результат", value=mapper[choice](a, b))