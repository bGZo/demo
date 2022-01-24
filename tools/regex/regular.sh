# editor envir: https://rubular.com | a ruby regular expression editor
# title: regex notes
# author: bGZoCg

b.t # b as begining, t as end

loadScript.*lua # string begining with loadScript to lua.
loadScript.*?lua # string begining with loadScript fitstly to lua.

loadScript\((.*?),(.*?)\) # double groups
loadScript($1,id,$2) # add id

# (TO_DATE.*)(\d+-[a-z]+-\d+', ')DD(-MM-YY')
# INSERT INTO EMPLOYEES VALUES( '100','Steven','King','SKING', '515.123.4567' , TO_DATE('17-JUN-87', 'DD-MM-YY'), 'AD_PRES', '24000',NULL, NULL,'90') -->

[^ ] # Character class. any character contained between the square brackets(blank space).
[^ ]* # string interval with blank space(include `\n`)
[^ ]*?@[^ ]*?\.[^ ]* # email
[\w.]+@\w+\.(com|net|edu) #email
  \w vs [^ ]*: [^ ]* include `\n`, former not.

[\u4e00-\u9fa5] # Simplied Chinese
[^\x00-\xff] # Double Bytes

https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*) # url
https?:/{2}\w.+$'# url

\(?\d{3}[-.)]\d{3}[-.]\d{4} # phone number
