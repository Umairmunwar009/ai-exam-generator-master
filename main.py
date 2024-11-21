import openai
import streamlit as st

from app.app import get_app
# 'org-1iW4LWgenoA0HxLv65gCIjKH'
# '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'
OPENAI_TOKEN = "OPENAI_TOKEN"
OPENAI_ORG = "OPENAI_ORG"


def initial_config():
    """
    Initial configuration of OpenAI API and streamlit
    """
    openai.organization = st.secrets[OPENAI_ORG]
    openai.api_key = st.secrets[OPENAI_TOKEN]

    st.set_page_config(
        page_title="Exam generator",
        page_icon=":pencil2:",
    )


def main():
    initial_config()

    app = get_app()
    app.render()


if __name__ == '__main__':
    main()
