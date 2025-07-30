from streamlit.web import cli as stcli
import sys

if __name__ == "__main__":
    sys.argv = ["streamlit", "run", "app.py", "--server.enableCORS=false"]
    sys.exit(stcli.main())
