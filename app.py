import psycopg2

connection = psycopg2.connect(
    database="notes_manager",
    user="postgres",
    password="123456",
    host="localhost",
    port=5432
)

cursor = connection.cursor()

#######################################################
# display all notes
#cursor.execute('SELECT * FROM note ORDER BY priority')

#notes = cursor.fetchall()

# for note in notes:
#    print(note)

######################################################
# display one note
#cursor.execute('SELECT * FROM note WHERE id=%s', [3])
#notes = cursor.fetchall()
#for note in notes:
#    print(note)

######################################################
# add new note
#cursor.execute('INSERT INTO note(title, body, priority) VALUES (%s, %s, %s)', ['test', 'test', 3])
#connection.commit()

######################################################
# update note
#cursor.execute('UPDATE note SET title=%s, body=%s, priority=%s WHERE id=%s', ['note one', 'description of note one', 4, 6])
#connection.commit()

######################################################
# delete note
#cursor.execute('DELETE FROM note WHERE id=%s', [6])
#connection.commit()

cursor.close()
connection.close()
