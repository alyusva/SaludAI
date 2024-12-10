from . import mongo, db
from datetime import datetime
from bson.objectid import ObjectId

# MongoDB: Guardar cita
def save_appointment(username, date, time):
    collection = mongo.db.appointments
    collection.insert_one({
        'username': username,
        'date': date,
        'time': time,
        'created_at': datetime.utcnow()
    })

# MongoDB: Obtener citas
def get_user_appointments(username):
    collection = mongo.db.appointments
    return list(collection.find({'username': username}))

# MongoDB: Cancelar cita
from bson.objectid import ObjectId

def cancel_appointment(username, appointment_id):
    try:
        collection = mongo.db.appointments
        # Convertir appointment_id a ObjectId
        object_id = ObjectId(appointment_id)
        print('El id de la cita es: ', object_id)
        result = collection.delete_one({'_id': object_id, 'username': username})
        
        if result.deleted_count > 0:
            print("Cita eliminada exitosamente.")
        else:
            print("No se encontró ninguna cita con ese ID y username.")
    except Exception as e:
        print("Error al eliminar la cita:", e)


class ChatLog(db.Model):
    __tablename__ = 'chat_logs'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    prompt = db.Column(db.Text, nullable=False)
    response = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())
    username = db.Column(db.Text, nullable = False)
