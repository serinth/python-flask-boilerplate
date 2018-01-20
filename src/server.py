from utils.factory import create_app
from utils.config import DevelopmentConfig, ProductionConfig
import os

if __name__ == '__main__':
    if os.environ.get('WORK_ENV') == 'PROD':
        app = create_app(ProductionConfig)
        app.run(port=5000, host="0.0.0.0", use_reloader=False)
    else:
        app = create_app(DevelopmentConfig)
        app.run(port=5000, host="0.0.0.0", use_reloader=True)
