#coding=utf-8

from flask import Flask
from flask_script import Manager, Server
from cas import app

manager = Manager(app)

manager.add_command('start', Server('0.0.0.0', 5000))

if __name__ == '__main__':
    manager.run()
