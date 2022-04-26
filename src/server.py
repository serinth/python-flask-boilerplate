import os
from config import Config, setConfig, create_app
from waitress import serve

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
    serve(app, port=8000, host="0.0.0.0")
