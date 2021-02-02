#!/bin/bash

# DB CONFIG
export DB_HOST="127.0.0.1"
export DB_USER="root"
export DB_PASSWORD="passw0rd"
export DB_NAME="gb_tools"

# FLASK CONFIG
export FLASK_DIR="/home/andre/Dropbox/10_Projetos/breeze/app"
export FLASK_APP="$FLASK_DIR/app.py"
export FLASK_ENV="development"
export FLASK_LOG="$FLASK_DIR/logs/app.log"

start() {
    
    echo -ne "\rStarting breeze..."
    flask run --host=0.0.0.0  2>> $FLASK_LOG >> $FLASK_LOG &
    sleep 1
    if test $? -eq 0
    then
        echo -ne "\rStarting breeze... OK\n"
    else 
        echo -ne "\rStarting breeze... Fail\n"
    fi


}

stop() {

    echo -ne "\rStopping breeze..."
    killall flask >> $FLASK_LOG 2>> $FLASK_LOG &
    sleep 1
    if test $? -eq 0
    then
        echo -ne "\rStopping breeze... OK\n"
    else 
        echo -ne "\rStopping breeze... Fail\n"
    fi
    
}

case $1 in

    --start)
        start
    ;;
    --stop)
        stop
    ;;
    --restart)
        stop
        start
    ;;
    *)
        echo -ne "\n --start : Start app"
        echo -ne "\n  --stop : Stop app\n\n"
    ;;
esac