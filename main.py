import sys
from routes import crud, listing

if(sys.argv[1] == 'add'):
    crud.add(sys.argv[2])

elif(sys.argv[1] == 'update'):
    crud.update(sys.argv[2], sys.argv[3])

elif(sys.argv[1] == 'delete'):
    crud.delete(sys.argv[2])

elif(sys.argv[1] == 'mark'):
    crud.mark_status(sys.argv[3], sys.argv[2])

elif(sys.argv[1] == 'list-everything'):
    listing.list_everything()

elif(sys.argv[1] == 'list-done'):
    listing.list_done()

elif(sys.argv[1] == 'list-in-progress'):
    listing.list_in_progress()

elif(sys.argv[1] == 'list-todo'):
    listing.list_todo()

else:
    print("Enter something valid.")