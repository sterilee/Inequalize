import streamlit as st
import math

# Title
st.title("Quadratic Inequality Solver")
st.write("Solve the inequality: ax² + bx + c <sign> 0")

# Inputs
a = st.number_input("Enter a (must be > 0)", value=1.0)
b = st.number_input("Enter b", value=0.0)
c = st.number_input("Enter c", value=0.0)
sign = st.selectbox("Select the inequality sign", ["<", "<=", ">", ">="])

# Solve button
if st.button("Solve"):
    # Check a
    if a <= 0:
        st.error("a must be positive!")
    else:
        delta = b**2 - 4*a*c
        st.write(f"Discriminant Δ = {delta}")

        # Logic for ">"
        if sign == ">":
            if delta < 0:
                st.success("The inequality is true for every real number")
            else:
                x1 = (-b + math.sqrt(delta)) / (2*a)
                x2 = (-b - math.sqrt(delta)) / (2*a)
                if delta == 0:
                    st.info(f"x ≠ {x1}")
                else:
                    if x1 < x2:
                        st.info(f"x < {round(x2, 2)} or x > {round(x1, 2)}")
                    else:
                        st.info(f"x < {round(x1, 2)} or x > {round(x2, 2)}")

        # Logic for ">="
        elif sign == ">=":
            if delta <= 0:
                st.success("The inequality is true for every real number")
            else:
                x1 = (-b + math.sqrt(delta)) / (2*a)
                x2 = (-b - math.sqrt(delta)) / (2*a)
                st.info(f"x ≤ {round(max(x1, x2), 2)} or x ≥ {round(min(x1, x2), 2)}")

        # Logic for "<"
        elif sign == "<":
            if delta <= 0:
                st.info("The inequality is not satisfied for any real number")
            else:
                x1 = (-b + math.sqrt(delta)) / (2*a)
                x2 = (-b - math.sqrt(delta)) / (2*a)
                if x1 < x2:
                    st.info(f"{round(x1,2)} < x < {round(x2,2)}")
                else:
                    st.info(f"{round(x2,2)} < x < {round(x1,2)}")

        # Logic for "<="
        elif sign == "<=":
            if delta < 0:
                st.success("The inequality is true for every real number")
            else:
                x1 = (-b + math.sqrt(delta)) / (2*a)
                x2 = (-b - math.sqrt(delta)) / (2*a)
                if delta == 0:
                    st.info(f"x = {round(x1,2)}")
                else:
                    if x1 < x2:
                        st.info(f"{round(x1,2)} ≤ x ≤ {round(x2,2)}")
                    else:
                        st.info(f"{round(x2,2)} ≤ x ≤ {round(x1,2)}")
