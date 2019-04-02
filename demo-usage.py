import mailman

# Params: from_email, password, to_email, subject, email_body
mailman.sendmail('SENDER EMAIL', 'PASSWORD', 'TO EMAIL', 'SUBJECT',
                 'BODY')
