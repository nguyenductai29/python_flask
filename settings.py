DB_HOST = 'localhost'        # Địa chỉ của máy chủ PostgreSQL
DB_NAME = 'python_flask'     # Tên cơ sở dữ liệu PostgreSQL
DB_USER = 'postgres'         # Tên người dùng PostgreSQL
DB_PASSWORD = 'dieuhuyen97'  # Mật khẩu của người dùng PostgreSQL
DB_PORT = 5432               # Cổng kết nối đến PostgreSQL

# Cấu hình kết nối cơ sở dữ liệu PostgreSQL
SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
SQLALCHEMY_TRACK_MODIFICATIONS = False
