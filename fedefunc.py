from driver import entrypoint

if __name__ == '__main__':
    entrypoint(['--parse-xl', dbutils.widgets.get('--parse-xl')])