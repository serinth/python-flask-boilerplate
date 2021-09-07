from utils.factory import create_app
from utils.config import Config, setConfig
import os

if __name__ == '__main__':
    is_prod = False
    config = Config()

    if os.environ.get('WORK_ENV') == 'PROD':
        config.debug = False 
        is_prod = True
    else:
        config.debug = True
        
    
    setConfig(config)
    app = create_app(config)
    app.run(port=8000, host="0.0.0.0", use_reloader=is_prod)
