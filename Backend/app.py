from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn  #pour demarrer le serveur
import snowflake.connector as sc
from dotenv import load_dotenv # pip install python-dotenv  c'est la commande pour creer la commande d'environnement 

