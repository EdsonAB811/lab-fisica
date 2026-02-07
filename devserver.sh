source .venv/bin/activate
python -m streamlit run main.py --server.enableCORS False --server.port $PORT
