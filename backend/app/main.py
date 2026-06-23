from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, RedirectResponse
from sqlalchemy.orm import Session
import qrcode
from io import BytesIO
import base64
import random
import string
import os
from datetime import datetime

from .database import engine, get_db
from .models import Base, URL
from .schemas import URLCreate, URLResponse

Base.metadata.create_all(bind=engine)

app = FastAPI(title="URL Shortener API", version="1.0.0")
