#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import render_template, current_app
from flask import flash, request, redirect, url_for, session

from . import main
from jobs.tasks import add_together


@main.route('/')
def home():
    a = current_app.config['AAA']  # 从配置文件中获取配置项
    return render_template('index.html', a=a)


@main.route('/add', methods=['GET', 'POST'])
def subadd():
    if request.method == 'GET':
        return render_template('add.html')

    if request.form['submit'] == 'Send':
        # send
        result = add_together.delay(12, 23)
        flash('Sending email to {0}'.format(result.wait()))
    else:
        flash('Error info')

    return redirect(url_for('main.subadd'))
