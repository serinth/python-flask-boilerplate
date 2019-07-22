from utils.factory import create_app
from utils.config import DevelopmentConfig, ProductionConfig
import os

if __name__ == '__main__':
    is_prod = False
    if os.environ.get('WORK_ENV') == 'PROD':
        app = create_app(ProductionConfig)
        is_prod = True
    else:
        app = create_app(DevelopmentConfig)
    app.run(port=8080, host="0.0.0.0", use_reloader=is_prod)
