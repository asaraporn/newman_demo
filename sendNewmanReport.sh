#!/bin/bash
#!sh ' sendemail -l email.log -f "asaraporn@addtechhub.com" -u "Email Subject 1"  -t "hadsai.g@gmail.com" -s "smtp.gmail.com:587" -o tls=yes -xu "asaraporn@addtechhub.com" -xp "Hadsai.1" -m "Test Send e-mail from project Postman on Docker" '

echo "=== Send Email ==="
sendemail -l email.log -f "asaraporn@addtechhub.com" \
	-u "Email Subject 1"  -t "hadsai.g@gmail.com" \
	-s "smtp.gmail.com:587" \
	-o tls=yes \
	-xu "asaraporn@addtechhub.com" \
	-xp "Hadsai.1"  \
	-o message-file="/tmp/mailbody.txt"
echo "=== End ==="





