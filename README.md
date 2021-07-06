# To deploy the site on production server you have to do this:

1. Add changes to Git and push them to the Github:
  1.1. git add .
  1.2. git commit -m "message"
  1.3. git push origin HEAD
2. Connect to prod server via Terminal:
  2.1. ssh u1027973@37.140.192.74 (password - w!d3MAwv)
  2.2. source venv/bin/activate
  2.3. cd www/darkpars.ru/darkparser
3. Pull the code from Github:
  3.1. git pull
4. If there are new migrations you must run them first:
  4.1. python manage.py migrate
5. Reload app on server by creating blank file in root folder of the site:
  5.1. /www/darkpars.io/.restart-app