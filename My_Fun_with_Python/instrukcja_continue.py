# jeśli instrukcja continue będzie wykonywana w pętli, to nie będą wykonane kolejne instrukcje zawarte w pętli,
# ale po prostu sterowanie przeskoczy do warunku określającego pętlę, czyli na początek pętli

#bez continue

pracownicy = ['Rafael', 'Maria@sales.mojafirma.pl', \
              'Roy', 'Krisitina', 'Jon@mojafirma.com', 'Joanna']

domena = 'mojafirma.pl'
emails = []

for pracownik in pracownicy:
    if '@' in pracownik:
        emails.append(pracownik.lower())
    else:
        email = pracownik.lower() + '@' + domena
        emails.append(email)
        
for email in emails:
    print(email)
    
>>>
rafael@mojafirma.pl
maria@sales.mojafirma.pl
roy@mojafirma.pl
krisitina@mojafirma.pl
jon@mojafirma.com
joanna@mojafirma.pl
>>> 

pracownicy = ['Rafael', 'Maria@sales.mojafirma.pl', \
              'Roy', 'Krisitina', 'Jon@mojafirma.com', 'Joanna']

domena = 'mojafirma.pl'
emails = []

for pracownik in pracownicy:
    if '@' in pracownik:
        emails.append(pracownik.lower())
        continue
    email = pracownik.lower() + '@' + domena
    emails.append(email)

for email in emails:
    print(email)
    
>>>
rafael@mojafirma.pl
maria@sales.mojafirma.pl
roy@mojafirma.pl
krisitina@mojafirma.pl
jon@mojafirma.com
joanna@mojafirma.pl
>>> 
