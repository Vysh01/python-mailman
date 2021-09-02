import mailman

# Params: from_email, from_name, password, to_email, subject, email_body, file
mailman.sendmail('senderemail', 'sendername', 'password', 'receiveremail', 'subject',
                 'body', 'filename')
