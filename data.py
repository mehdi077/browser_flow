from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import requests
import io
from PIL import Image
import base64
from selenium.webdriver.support.ui import WebDriverWait as wait
import json
import re
from flask import Flask, request, jsonify
import threading
from flask_cors import CORS

