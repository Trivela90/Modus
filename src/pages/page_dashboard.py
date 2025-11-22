import streamlit as st
import pandas as pd
import altair as alt
from datetime import date

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Finance Tracker",
    page_icon="💸",
    layout="wide"
)

# ---------- GLOBAL STYLE ----------
st.markdown(
    """
    <style>
    body {
        background-color: #050608;
        color: #f5f5f5;
    }
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 1.5rem;
        max-width: 1400px;
    }
    h1, h2, h3, h4 {
        font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }
    .section-title {
        font-size: 1.6rem;
        font-weight: 700;
        margin-bottom: 0.4rem;
    }
    .panel {
        background: #111217;
        border-radius: 0.6rem;
        padding: 0.75rem 0.9rem;
        border: 1px solid #23242c;
    }
    .panel-header {
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #a0a0a0;
        margin-bottom: 0.4rem;
    }
    .small-label {
        font-size: 0.78rem;
        text-transform: uppercase;
        color: #9a9a9a;
        margin-bottom: 0.15rem;
    }
    .account-card {
        background: #151720;
        border-radius: 0.6rem;
        padding: 0.6rem 0.75rem;
        border: 1px solid #262838;
        margin-bottom: 0.35rem;
    }
    .account-name {
        font-size: 0.9rem;
        font-weight: 600;
    }
    .account-balance-label {
        font-size: 0.7rem;
        color: #999;
    }
    .account-balance {
        font-size: 0.9rem;
        font-weight: 600;
    }
    .quick-btn button {
        border-radius: 0.45rem !important;
        border: 1px solid #333645 !important;
        background: #151720 !important;
        color: #f5f5f5 !important;
        font-size: 0.78rem !important;
    }
    .quick-btn button:hover {
        border-color: #565bff !important;
    }
    .budget-name {
        font-size: 0.85rem;
        font-weight: 500;
        margin-bottom: 0.1rem;
    }
    .budget-amount {
        font-size: 0.75rem;
        color: #aaaaaa;
        margin-bottom: 0.2rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- MOCK DATA ----------
expenses = pd.DataFrame(
    [
        ["Groceries", 150.00, "Banco Inter", date(2025, 3, 11)],
        ["Utilities", 86.00, "Banco Inter", date(2025, 3, 10)],
        ["Taxi / Transport", 58.00, "Banco do Brasil", date(2025, 3, 9)],
        ["Eating Out", 125.00, "Nubank", date(2025, 3, 8)],
        ["Subscriptions", 39.90, "Nubank", date(2025, 3, 7)],
        ["Health", 97.50, "Banco Inter", date(2025, 3, 7)],
    ],
    columns=["Category", "Amount (R$)", "Account", "Date"],
)

incomes = pd.DataFrame(
    [
        ["Salary", 4200.00, "Banco Inter", date(2025, 3, 5)],
        ["Freelance", 780.00, "Banco do Brasil", date(2025, 3, 10)],
        ["Cashback", 18.00, "Nubank", date(2025, 3, 8)],
    ],
    columns=["Source", "Amount (R$)", "Account", "Date"],
)

transfers = pd.DataFrame(
    [
        ["Banco Inter", "Nubank", 300.0, date(2025, 3, 3)],
        ["Nubank", "Investments", 150.0, date(2025, 3, 6)],
    ],
    columns=["From", "To", "Amount (R$)", "Date"],
)

accounts = [
    {"name": "Nubank", "balance": 57.41},
    {"name": "Banco do Brasil", "balance": 202.81},
    {"name": "Banco Inter", "balance": 223.33},
]

budgets = [
    {"name": "Investments", "spent": 800.0, "limit": 1000.0},
    {"name": "Entertainment", "spent": 350.0, "limit": 500.0},
    {"name": "Groceries", "spent": 400.0, "limit": 600.0},
]

# ---------- LAYOUT ----------
left_col, center_col, right_col = st.columns([1.0, 2.3, 1.1])

# ========== LEFT SIDEBAR (FAKE) ==========
with left_col:
    st.markdown("<div class='section-title'>Finance Tracker</div>", unsafe_allow_html=True)

    #     st.markdown("<div class='panel'>", unsafe_allow_html=True)
    #     st.markdown("<div class='panel-header'>Quick actions</div>", unsafe_allow_html=True)

    #     quick_labels = [
    #         "➕ New Income",
    #         "➖ New Expense",
    #         "🔁 New Transfer",
    #         "🏦 New Account",
    #         "🏷️ New Category",
    #     ]
    #     for label in quick_labels:
    #         cols = st.columns([1])
    #         with cols[0]:
    #             with st.container():
    #                 st.markdown("<div class='quick-btn'>", unsafe_allow_html=True)
    #                 st.button(label, use_container_width=True)
    #                 st.markdown("</div>", unsafe_allow_html=True)

    #     st.markdown("</div>", unsafe_allow_html=True)

    st.write("")
    with st.container():
        # st.markdown("<div class='panel'>", unsafe_allow_html=True)
        st.markdown("<div class='panel-header'>Budgets</div>", unsafe_allow_html=True)

        for b in budgets:
            progress = min(b["spent"] / b["limit"], 1.0)
            st.markdown(
                f"<div class='budget-name'>{b['name']}</div>"
                f"<div class='budget-amount'>R${b['spent']:.2f} / R${b['limit']:.2f}</div>",
                unsafe_allow_html=True,
            )
            st.progress(progress)
            st.write("")

        # st.markdown("</div>", unsafe_allow_html=True)

# ========== CENTER COLUMN (TABLES) ==========
with center_col:
    # Expenses
    st.markdown("<div class='section-title'>Expenses</div>", unsafe_allow_html=True)
    with st.container():
        # st.markdown("<div class='panel'>", unsafe_allow_html=True)
        st.markdown("<div class='panel-header'>Recent Expenses</div>", unsafe_allow_html=True)
        st.dataframe(
            expenses.sort_values("Date", ascending=False),
            hide_index=True,
            use_container_width=True,
        )
        # st.markdown("</div>", unsafe_allow_html=True)

    st.write("")
    # Incomes
    st.markdown("<div class='section-title'>Incomes</div>", unsafe_allow_html=True)
    with st.container():
        # st.markdown("<div class='panel'>", unsafe_allow_html=True)
        st.markdown("<div class='panel-header'>Recent Incomes</div>", unsafe_allow_html=True)
        st.dataframe(
            incomes.sort_values("Date", ascending=False),
            hide_index=True,
            use_container_width=True,
        )
        # st.markdown("</div>", unsafe_allow_html=True)

    st.write("")
    # Account Transfers
    st.markdown("<div class='section-title'>Account Transfers</div>", unsafe_allow_html=True)
    with st.container():
        # st.markdown("<div class='panel'>", unsafe_allow_html=True)
        st.markdown("<div class='panel-header'>Recent Transfers</div>", unsafe_allow_html=True)
        st.dataframe(
            transfers.sort_values("Date", ascending=False),
            hide_index=True,
            use_container_width=True,
        )
        # st.markdown("</div>", unsafe_allow_html=True)

# ========== RIGHT COLUMN (CHART + ACCOUNTS) ==========
with right_col:
    # Expense chart
    with st.container():
        # st.markdown("<div class='panel'>", unsafe_allow_html=True)
        st.markdown("<div class='panel-header'>Expense chart</div>", unsafe_allow_html=True)

        by_cat = expenses.groupby("Category", as_index=False)["Amount (R$)"].sum()

        if not by_cat.empty:
            chart = (
                alt.Chart(by_cat)
                .mark_arc(innerRadius=60)
                .encode(
                    theta=alt.Theta("Amount (R$):Q", stack=True),
                    color=alt.Color("Category:N", legend=None),
                    tooltip=["Category", "Amount (R$)"],
                )
            )
            st.altair_chart(chart, use_container_width=True)
        else:
            st.write("No data")

        # st.markdown("</div>", unsafe_allow_html=True)

    st.write("")
    # Accounts
    with st.container():
        # st.markdown("<div class='panel'>", unsafe_allow_html=True)
        st.markdown("<div class='panel-header'>Accounts</div>", unsafe_allow_html=True)

        for acc in accounts:
            st.markdown(
                f"""
                <div class="account-card">
                    <div class="account-name">{acc['name']}</div>
                    <div class="account-balance-label">Current balance</div>
                    <div class="account-balance">R${acc['balance']:.2f}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        # st.markdown("</div>", unsafe_allow_html=True)
