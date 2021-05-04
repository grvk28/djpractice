# Django-html webapp
# Sign in,Sign up,Read csv and populate database,update,delete,search,add, download a row of record:
read csv and populate database file:views.py
    function: def i(line 14)

#update,delete,search,add, download record:
   all functions in file
    views.py: update1 (line 101) 
              delete1 (line 107 )
              filter2 (line 125)
              add1 (line 68 )
              download (line 112)


#Run
python manage.py runserver

#Migrate:
python manage.py makemigrations
python manage.py migrate
