import streamlit as st

st.title('Khatra Calculator \n \n -Dagai Trigar')
num1=st.number_input("Enter your first number")
num2=st.number_input("Enter your second number")
choice=Options = st.selectbox(""" What would you like to do ? """,("Add","Subtract","Multiply","Divide","Power","Remainder","No remainder"))
button=st.button("Done")
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def power(x, y):
    return x ** y


def remainder(x, y):
    return x % y


def roundup(x, y):
    return x // y

if button :

    if choice in ('Add', 'Substract', 'Multiply', 'Divide', 'Power', 'No power'):
        try :
            num1 = float(num1)
            num2 = float(num2)
        except ValueError :
            st.write("Invalid input. Please enter a number.")
    if choice == 'Add':
        st.write(num1, "+", num2, "=", add(num1, num2))

    elif choice == 'Subtract':
        st.write(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == 'Multiply':
        st.write(num1, "*", num2, "=", multiply(num1, num2))

    elif choice == 'Divide':
        st.write(num1, "/", num2, "=", divide(num1, num2))

    elif choice == 'Power':
        st.write(num1, "raised to the power of", num2, "is", power(num1, num2))

    elif choice == "Remainder":
        st.write("when", num1, "divides", num2, "the remainder is", remainder(num1, num2))

    elif choice == "No Remainder":
       st.write("When", num1, "divides", num2, "the remainder rounded up is:", roundup(num1, num2))
    else :
        st.write("Invalid Syntax")


