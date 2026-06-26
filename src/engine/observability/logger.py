import logging

def setup_logger():
    # Clear existing handlers if any
    root = logging.getLogger()
    if root.handlers:
        for handler in root.handlers:
            root.removeHandler(handler)

    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        filename='game.log',
        filemode='w'
    )
    
    # Get the logger and ensure it flushes
    logger = logging.getLogger('OregonQuick')
    return logger
