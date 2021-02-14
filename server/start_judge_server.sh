#gunicorn --workers 1 --threads 1 --error-logfile /home/oj/qduoj/gunicorn_js.log --time 600 --bind 0.0.0.0:12358 server:server 


ps ux | grep server.py | grep python |awk '{print $2}'|xargs kill -9
python server.py &>s.log &
