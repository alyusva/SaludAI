from redis import Redis
import os

class Config:
    # Clave secreta para la seguridad
    SECRET_KEY = os.environ.get('SECRET_KEY', 'super-secret-key')

    # Configuración de MongoDB
    MONGO_URI = 'mongodb+srv://saludAI:qO7vQxxuHULR8K09@cluster0.ntati.mongodb.net/mi_base_datos?retryWrites=true&w=majority'

    # Configuración de SQLAlchemy (usando MySQL en Railway)
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', 
        'mysql://root:JsWKYllmPDCfJsfitGzrNzydvCHVHJzm@autorack.proxy.rlwy.net:50361/railway')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Configuración de Redis usando la URL proporcionada
    REDIS_URL = os.environ.get('REDIS_URL', 'redis://default:JhYIVoAvPXzpSgweJbxdHLXfxjAwKKLK@autorack.proxy.rlwy.net:30901')
    SESSION_TYPE = 'redis'
    SESSION_PERMANENT = False
    SESSION_USE_SIGNER = True
    SESSION_KEY_PREFIX = 'session:'  # Prefijo para claves relacionadas con sesiones en Redis
    SESSION_REDIS = Redis.from_url(REDIS_URL, decode_responses=False)

    # Clave API para OpenAI
    COHERE_API_KEY = os.environ.get('COHERE_API_KEY', 'gln6JSdxFJihYolBpUu4uUE1ToZdJV1usX894PqG')
